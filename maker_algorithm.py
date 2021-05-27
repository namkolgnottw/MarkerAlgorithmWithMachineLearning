import random
from ml_oracle import train_model, file_to_dataframe, is_heavy
from probables import CountMinSketch


class RequestFile:
    def __init__(self, update_year, file_type, is_in_homepage):
        self.update_year = update_year
        self.file_type = file_type
        self.is_in_homepage = is_in_homepage

class Node:
    def __init__(self, page_name, request_file):
        self.page_name = page_name
        self.request_file = request_file
        self.marked = False
    
def getHarmonicNumber(k): #k = cache_size
    h = 0
    for i in range(1,k+1):
      h = h + (1 / i)
    return h

class makerCache:
    def __init__(self, size):
        self.phase = 1
        self.round = 1
        self.size = size
        self.cache = []
        self.clean_counter = 0
        self.clean_set = []
        for i in range(0,size):  # init empty cache(list)
            self.cache.append( Node('-', RequestFile(0, 'txt', False) ) )
        self.model = train_model()
        self.cms = CountMinSketch(width=1000, depth=5)
        self.hashtable = {} # single bucket for heavy items
        self.miss_count = 0

    def print(self):
        for i in range(0, self.size) :
            print(self.cache[i].page_name, end=' ')
        print(' ')
        print(' ')
    
    def get_phase(self):
        return self.phase
    
    def isAllSlotTaken(self):
        for i in range(0, self.size):
            if self.cache[i].page_name == '-':
                return False
        return True

    def lookup(self, page_name):
        for i in range(0, self.size):
            if self.cache[i].page_name == page_name:
                return True  # page in the cache
        return False  # page not in cache


    def set_marked(self, page_name):
        for i in range(0, self.size):
            if self.cache[i].page_name == page_name:
                self.cache[i].makred = True
    def is_all_marked(self):
        for i in range(0, self.size):
            if self.cache[i].marked == False:
                return False
        return True

    def reset(self):
        for i in range(0, self.size):
            self.cache[i].marked = False
        self.phase = self.phase+1
        self.clean_counter = 0
        # save current cache as the set of elements that are possibly stale in new phase

    def evict(self, slot_pos):
       self.cache[slot_pos].page_name = '-'
       self.cache[slot_pos].request_file.update_year = 0
       self.cache[slot_pos].request_file.file_type = '-'
       self.cache[slot_pos].request_file.is_in_hompage = False
       self.cache[slot_pos].marked = False

    def fill_in(self, slot_pos, new_page_name, request_file):
       self.cache[slot_pos].page_name = new_page_name
       self.cache[slot_pos].request_file.update_year = request_file.update_year
       self.cache[slot_pos].request_file.file_type = request_file.file_type
       self.cache[slot_pos].request_file.is_in_hompage = request_file.is_in_homepage
       self.cache[slot_pos].marked = True
       file_df = file_to_dataframe(self.cache[slot_pos].request_file)
       is_heavy0 = is_heavy(self.model, file_df)
       if is_heavy0:
           if new_page_name in self.hashtable:
               self.hashtable[new_page_name] = self.hashtable[new_page_name] + 1
           else:
               self.hashtable[new_page_name] = 1
       else:
           self.cms.add(new_page_name)


    def replace(self, slot_pos, new_page_name, request_file):
        self.evict(slot_pos)
        self.fill_in(slot_pos, new_page_name, request_file)

    def select_unmarked(self, mode):
        pos = 0
        unmarked = []
        unmarked_freq = []

        for i in range(0, self.size):
            if self.cache[i].marked == False:
              print(self.cache[i])
              unmarked.append(i)
              unmarked_freq.append(0)

        print('unmarked:', unmarked)
        # rand method
        if mode=='random':
          # print('using random method to select unmarked')
          rand_pos = random.randint(0,len(unmarked)-1)
          print('unmarked len =', len(unmarked))
          print('rand_pos=', rand_pos)
          print('real pos =', unmarked[rand_pos])
          return unmarked[rand_pos]

        elif mode=='ml_oracle':
          # ml method
          # predict all unmarked element (predict time = frequency from count-min sketch)
          # select the lowest frequency unmarked element
          # print('using ml oracle method to select unmarked')
          for i in range(0, len(unmarked)):

              freq = 0
              # data preprocess
              file_df = file_to_dataframe(self.cache[unmarked[i]].request_file)
              is_heavy0 = is_heavy(self.model, file_df)

              if is_heavy0:
                  freq = self.hashtable[self.cache[unmarked[i]].page_name]
                  # print('freq:', freq)
                  unmarked_freq[i] = freq

                  # get from hash table
              else:
                  # not heavy : get from count min sketch
                  freq = self.cms.check(self.cache[unmarked[i]].page_name)
                  # print('freq:', freq)
                  unmarked_freq[i] = freq
          print(unmarked)
          print(unmarked_freq)
          max = 0
          max_pos = 0
          for j in range(0, len(unmarked)):
            if unmarked[j] > max:
                max = unmarked[j]
                max_pos = j
          return max_pos

    def request_page(self, page_name, request_file, mode='random'):
        # print('mode = ', mode)
        # requested page in cache
        if self.lookup(page_name) == True:
            self. set_marked(page_name)# set its marked = true
            file_df = file_to_dataframe(request_file)
            is_heavy0 = is_heavy(self.model, file_df)
            if is_heavy0:
               if page_name in self.hashtable:
                   self.hashtable[page_name] = self.hashtable[page_name] + 1
                   print('freq:', self.hashtable[page_name])
               else:
                   self.hashtable[page_name] = 1
            else:
                self.cms.add(page_name)
                print('freq:', self.cms.check(page_name))

            if self.is_all_marked() == True:
                print('cache is all marked, ready to reset')
                self.print()
                self.reset()
            return True

        # page not in cache, idle slot available
        # a miss occur
        self.miss_count += 1

        if self.isAllSlotTaken() == False:
            for i in range(0, self.size):
                if self.cache[i].page_name == '-':
                    self.replace(i, page_name, request_file)
                    break
            if self.is_all_marked() == True:
                print('cache is all marked, ready to reset')
                self.print()
                self.reset()
            return False
            
        # page not in cache and no idle slot
        replace_pos = self.select_unmarked(mode)
        self.replace(replace_pos, page_name, request_file)
        if self.is_all_marked() == True:
            print('cache is all marked, ready to reset')
            self.print()
            self.reset()
        return False

