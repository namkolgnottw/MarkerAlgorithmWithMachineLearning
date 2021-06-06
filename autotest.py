import os,sys 

if __name__ == '__main__':
  if len(sys.argv)!=2:
      print('wrong arguments')
      sys.exit()
  n = int(sys.argv[1])
  df = []
  for i in range (0, n):
    row_data = os.popen('python main.py test')
    s0 = row_data.readline().strip().split(' = ') # random
    s1 = row_data.readline().strip().split(' = ') # ml
    df.append([int(s0[1]), int(s1[1])])

  rand_miss_sum = 0
  ml_miss_sum = 0
  for i in range(0, len(df)) :
    rand_miss_sum += df[i][0]
    ml_miss_sum += df[i][1]
  avg_rand_miss = rand_miss_sum / len(df)
  avg_ml_miss = ml_miss_sum / len(df)
  print('average random method miss :', avg_rand_miss)
  print('average ml_oracle method miss :', avg_ml_miss)