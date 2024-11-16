#Sort the pandas Dataframe on the basis of a single column in ascending order

import pandas as pd
import numpy as np
#Create a Dictionary of series
d = {'Name':pd.Series(['Sachin','Dhoni','Virat','Rohit','Shikhar']),
'Age':pd.Series([26,27,25,24,31]),
'Score':pd.Series([87,89,67,55,47])}
#Create a DataFrame
df= pd.DataFrame(d)
print("Dataframe contents without sorting")
print (df)
df=df.sort_values(by='Score',ascending= 0) #ascending=0 signifies descending order
print("Dataframe contents after sorting")
print(df)









