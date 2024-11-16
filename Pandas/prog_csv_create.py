#Creating a duplicate csv file with selective columns

import pandas as pd
df =pd.read_csv("E:\\Data\\Employee.csv")
df1 = df.to_csv("E:\\Data\\Emp.csv",columns =["Empid",'Name'])











