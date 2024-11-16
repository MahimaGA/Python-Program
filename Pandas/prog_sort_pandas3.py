#Sort the dataframe by index in ascending order

import pandas as pd
import numpy as np
#Create a Dictionary of series
d = {'Name':pd.Series(['Jeet','Dheeraj','Suraj','Rohit','Ankit']),
'Age':pd.Series([26,25,25,24,31]),
'Score':pd.Series([87,67,89,55,47])}
#Create a DataFrame
df= pd.DataFrame(d)
df=df.reindex([1,4,3,2,0])
print("Dataframe contents without sorting")
print (df)
df1=df.sort_index() #Ascending order by default
print("Dataframe contents after sorting")
print(df1)


