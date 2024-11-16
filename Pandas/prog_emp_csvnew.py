#Copying the contents of Employee.csv to Empnew

import pandas as pd
df =pd.read_csv("E:\\Data\\Employee.csv")
df.to_csv("E:\\Data\\Empnew.csv")
print(df)





































