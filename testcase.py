from maker_algorithm import makerCache
from maker_algorithm import RequestFile
from maker_algorithm import Node
import sys, random


def simulate_webpage_resource():
  #home page resource A B C
  home_page = [
               Node('A', RequestFile(2018, 'txt', True)),
               Node('B', RequestFile(2019, 'video', True)), 
               Node('C', RequestFile(2020, 'picture', True)),
               Node('Z', RequestFile(2018, 'txt', True)),
               Node('X', RequestFile(2019, 'video', True)), 
               Node('Y', RequestFile(2020, 'picture', True)),
               Node('V', RequestFile(2018, 'txt', True)),
               Node('M', RequestFile(2019, 'video', True)), 
               Node('N', RequestFile(2020, 'picture', True)),
              ]

  # non home page resource D E F G H I,  where D,E are heavy
  non_home_page = [
               Node('D', RequestFile(2019, 'txt', False)),
               Node('E', RequestFile(2020, 'video', False)), 
               Node('F', RequestFile(2016, 'picture', False)),                  
               Node('G', RequestFile(2015, 'picture', False)),                  
               Node('H', RequestFile(2015, 'video', False)), 
               Node('I', RequestFile(2016, 'video', False)), 
               Node('J', RequestFile(2019, 'txt', False)),
               Node('K', RequestFile(2020, 'video', False)), 
               Node('L', RequestFile(2016, 'picture', False)),                  
               Node('O', RequestFile(2015, 'picture', False)),                  
               Node('P', RequestFile(2015, 'video', False)), 
               Node('Q', RequestFile(2016, 'video', False)), 

               Node('D1', RequestFile(2019, 'txt', False)),
               Node('E1', RequestFile(2020, 'video', False)), 
               Node('F1', RequestFile(2016, 'picture', False)),                  
               Node('G1', RequestFile(2015, 'picture', False)),                  
               Node('H1', RequestFile(2015, 'video', False)), 
               Node('I1', RequestFile(2016, 'video', False)), 
               Node('D2', RequestFile(2019, 'txt', False)),
               Node('E2', RequestFile(2020, 'video', False)), 
               Node('F2', RequestFile(2016, 'picture', False)),                  
               Node('G2', RequestFile(2015, 'picture', False)),                  
               Node('H2', RequestFile(2015, 'video', False)), 
               Node('I2', RequestFile(2016, 'video', False)), 
               Node('D3', RequestFile(2019, 'txt', False)),
               Node('E3', RequestFile(2020, 'video', False)), 
               Node('F3', RequestFile(2016, 'picture', False)),                  
               Node('G3', RequestFile(2015, 'picture', False)),                  
               Node('H3', RequestFile(2015, 'video', False)), 
               Node('I3', RequestFile(2016, 'video', False)), 
               Node('D4', RequestFile(2019, 'txt', False)),
               Node('E4', RequestFile(2020, 'video', False)), 
               Node('F4', RequestFile(2016, 'picture', False)),                  
               Node('G4', RequestFile(2015, 'picture', False)),                  
               Node('H4', RequestFile(2015, 'video', False)), 
               Node('I4', RequestFile(2016, 'video', False)), 
               Node('D5', RequestFile(2019, 'txt', False)),
               Node('E5', RequestFile(2020, 'video', False)), 
               Node('F5', RequestFile(2016, 'picture', False)),                  
               Node('G5', RequestFile(2015, 'picture', False)),                  
               Node('H5', RequestFile(2015, 'video', False)), 
               Node('I5', RequestFile(2016, 'video', False)), 
  ]
  pass
  return home_page, non_home_page


def create_test_input():
    test_input = []
    test_home_page, test_non_home_page = simulate_webpage_resource()

    for i in range(0, 200):
      if i%4!=0:  
        test_input.append(test_home_page[random.randint(0,len(test_home_page)-1)])
      else:
        test_input.append(test_non_home_page[random.randint(0,len(test_non_home_page)-1)])
    return test_input



def testor(cache0, argv0, test_input):
    for i in range(0, len(test_input)):
      #print('request page', test_input[i].page_name)
      cache0.request_page(test_input[i].page_name, test_input[i].request_file, argv0)
      #cache0.print()


