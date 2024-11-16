#Progam for computing Variance

import pandas as pd
import numpy as np
#Create a Dictionary of series
d = {'Name':pd.Series(['Sachin','Dhoni','Virat','Rohit','Shikhar']),
'Age':pd.Series([26,25,25,24,31]),
'Score':pd.Series([87,67,89,55,47])}
#Create a DataFrame
df= pd.DataFrame(d)
print("Dataframecontents")
print(df)
print(df.var())




