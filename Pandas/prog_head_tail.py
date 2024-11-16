#Using head() and tail() functions on series
import pandas as pd
series1 =pd.Series([10,20,30,40,50],index=['a','b','c','d','e'])
print(series1)
print(series1.head(2))   #If no argument is provided then
#by default 5 rows are displayed
print(series1.tail(2))






