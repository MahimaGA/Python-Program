#Concatenating two data frames
import pandas as pd
d1 = {'roll_no': [10,11,12,13,14,15],
      'name':['Ankit','Pihu','Rinku','Yash','Vijay','Nikhil']}
df1 =pd.DataFrame(d1, columns =['roll_no','name'])
print(df1)
d2 ={'roll_no': [1,2,3,4,5,6],
     'name':['Renu','Jatin','Deep','Guddu','Chhaya','Sahil']}
df2 =pd.DataFrame(d2,columns = ['roll_no','name'])
print(df2)





