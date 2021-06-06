from maker_algorithm import makerCache
import sys

if __name__ == '__main__' :
  import testcase
  if len(sys.argv)!=2 :
    sys.stderr.write('wrong argument nums\n')
    
  if sys.argv[1] != 'random' and sys.argv[1] != 'ml_oracle' and sys.argv[1] !='test':
    sys.stderr.write('wrong argument. You can either random or ml_oracle\n')
    
      
  cache0 = makerCache(30)
  cache1 = makerCache(30)
  #cache0.print()
  #cache1.print()
  #print('start test case')
  test_input = testcase.create_test_input()
  if sys.argv[1] == 'test':
    testcase.testor(cache0, 'random', test_input)
    testcase.testor(cache1, 'ml_oracle', test_input)
    print('random select miss count =', cache0.miss_count)
    print('ml_oracle select miss count =', cache1.miss_count)
  else:
    testcase.testor(cache1, sys.argv[1], test_input)
    print('miss count =', cache1.miss_count)