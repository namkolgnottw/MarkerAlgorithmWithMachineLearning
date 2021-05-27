# Code you have previously used to load data
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics


def train_model():
  trian_dataset_file_path = 'train.csv'

  data_set = pd.read_csv(trian_dataset_file_path)
  #print(data_set)
  labelencoder = LabelEncoder()
  data_set['file_type'] = labelencoder.fit_transform(data_set['file_type'])
  #print(data_set)
  # Create target object and call it y
  y = data_set.whether_heavy
  # Create X
  features = ['update_year', 'file_type', 'in_home_page']
  X = data_set[features]
  #print(X)
  train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)
  #print(train_X)
  #print(val_X)
  model = DecisionTreeClassifier()

  # Fit Model
  model.fit(train_X, train_y)
  # Make validation predictions and calculate mean absolute error
  val_predictions = model.predict(val_X)
  #print(val_predictions)
  #print(val_y)
  accuracy = metrics.accuracy_score(val_y, val_predictions)
  print('accuracy : ', accuracy, end='\n')
  return model

def file_to_dataframe(request_file):
    file_dict = {'update_year':request_file.update_year, 
                 'file_type':request_file.file_type,
                 'in_home_page':request_file.is_in_homepage
    }

    dataframe = pd.DataFrame(file_dict, index = file_dict.keys())
    return dataframe

def is_heavy(model, file_dataframe):
  labelencoder = LabelEncoder()
  file_dataframe['file_type'] = labelencoder.fit_transform(file_dataframe['file_type'])
  ret_df = model.predict(file_dataframe)
  # print("predict is_heavy =",ret_df)
  ret = ret_df[0]
  # print("predict is_heavy =",ret)
  return ret


# for test model
if __name__=='__main__':
  while 1:
     i = int(input('Run model test enter 1 , exit for 2\n\n'))
     if i==1:
       train_model()
     elif i==2:
       break