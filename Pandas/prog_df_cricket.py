#To perform all the aggregate and statistical functions in Pandas
#on "cricket" dataframe

import pandas as pd
import numpy as np
#Create a Dictionary of series
d = {'Name':pd.Series(['Sachin','Dhoni','Virat','Rohit','Shikhar']),
'Age':pd.Series([26,25,25,24,31]),
'Score':pd.Series([87,67,89,55,47])}
#Create a DataFrame
df= pd.DataFrame(d)
print("Dataframecontents")
print (df)
print(df.count())
print("count age",df[['Age']].count())
print("sum of score",df[['Score']].sum())
print("minimum age",df[['Age']].min())
print("maximum score",df[['Score']].max())
print("mean age",df[['Age']].mean())
print("mode of age",df[['Age']].mode())
print("median of score",df[['Score']].median())





