#Sort the pandas Dataframe on the basis of Multiple Columns

import pandas as pd
import numpy as np
#Create a Dictionary of series
d = {'Name':pd.Series(['Sachin','Dhoni','Virat','Rohit','Shikhar']),
'Age':pd.Series([26,25,25,24,31]),
'Score':pd.Series([87,67,89,55,47])}
#Create a DataFrame
df= pd.DataFrame(d)
print("Dataframe contents without sorting")
print(df)
#Sorting on the basis of age in ascending order and then on Score in
#descending order
df=df.sort_values(by=['Age', 'Score'],ascending=[True,False])
print("Dataframe contents after sorting")
print(df)





