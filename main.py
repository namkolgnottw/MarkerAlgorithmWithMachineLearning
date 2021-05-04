from maker_algorithm import makerCache


if __name__ == '__main__' :
  from testcase import testor
  print(__name__)
  cache0 = makerCache(4)
  cache0.print()
  print('start test case')
  testor(cache0)