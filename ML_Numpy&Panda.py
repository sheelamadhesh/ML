# ML Basics:
#import numpy library
import numpy as np
#import panda library
import pandas as pd

# Series Creation - 1D dimentional labeled array capable of holding any datatype
series1 = pd.Series([1,34,35,55,3434,6757,7575])
print(series1)

series2 = pd.Series([40,70,90],index = ['Monday','2','Wednesday'])
print(series2)

#DF Declaration
data = {'City': ['Salem','Chennai','Palani'],
        'Population' : [12132,2324,424224]
        }
print ('dic\n' ,data)
df = pd.DataFrame(data)
print(df)

# Create df using numpy array
array_1 = np.random.randn(2,4)
print (array_1)
print (array_1.mean(),array_1.std())
# With column name
df = pd.DataFrame(array_1,columns=['A','B','C','D'])
print (df)
print(df.shape,df.size)
#Create a DataFrame by reading Data from a CSV File
# Create URL - This is the train csv file from github
csv_url = 'https://raw.githubusercontent.com/agconti/kaggle-titanic/master/data/train.csv'
#load_dataset
df_csv = pd.read_csv(csv_url)
print(df_csv)
print(df_csv.head(5))
#Filtering a Data Frame
print(df_csv.loc[4,1])
#Filtering with loc and iloc methods
#Filtering by Selecting a Subset of Columns
#Filtering by condition