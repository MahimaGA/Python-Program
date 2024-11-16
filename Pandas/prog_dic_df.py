#Data frame as dicitonary

import pandas as pd
df ={'Name':['Rinku','Ritu','Ajay','Pankaj','Aditya'],
          'IP':[78,88,98,90,87]}
print(df)
table =pd.Series(df)
table1 =pd.DataFrame(table)
print(table)
print("Index Value")
print(table1.index)
print("Column Name")
print(table1.columns)
















