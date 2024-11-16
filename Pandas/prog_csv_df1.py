#To illustrate pivot_table() function on the dataframe
#generated using .csv file-Employee.csv

import pandas as pd
df =pd.read_csv("E:\\Data\\Employee.csv",skiprows =1,
                names =['E_id','Ename','E_age','Ecity','Esalary'])
print(df)
r=df.pivot_table(df,index=['Ename'],aggfunc="sum")
print(r)































