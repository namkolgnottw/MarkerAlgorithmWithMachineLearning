from maker_algorithm import makerCache
from maker_algorithm import RequestFile
from maker_algorithm import Node





def testor(cache0):
    test_input = [] # test input
    test_input.append(Node('a', RequestFile(500, 'txt', True)))
    test_input.append(Node('a', RequestFile(500, 'txt', True)))
    test_input.append(Node('b', RequestFile(500, 'txt', True)))
    test_input.append(Node('c', RequestFile(500, 'txt', False)))
    test_input.append(Node('d', RequestFile(500, 'txt', False)))
    test_input.append(Node('e', RequestFile(500, 'txt', False)))
    test_input.append(Node('a', RequestFile(500, 'txt', True)))
    test_input.append(Node('a', RequestFile(500, 'txt', True)))
    test_input.append(Node('c', RequestFile(500, 'txt', False)))
    test_input.append(Node('e', RequestFile(500, 'txt', False)))
    test_input.append(Node('e', RequestFile(500, 'txt', False)))
    test_input.append(Node('kqe', RequestFile(500, 'txt', False)))
    test_input.append(Node('wqer', RequestFile(500, 'txt', False)))
    test_input.append(Node('wqer', RequestFile(500, 'txt', False)))

    for i in range(0, 14):
      print('request page', test_input[i].page_name)
      cache0.request_page(test_input[i].page_name, test_input[i].request_file)
      cache0.print()


