# Maximum , Minimum , Mean, Mode , Median and Count of sales Salesman wise
import pandas as pd
print("\n")
print ( "Dataframe of Values\n")
monthlysale = {'Salesman':["Rinku", "Jay","Radhika","Arun","Jay",
                             "Karan","Akshit", "Jay","Karan","Akshit",
                             "Radhika","Karan"],
               'Sales':[1000,300,800,1000,500,60,1000,900,300,1000,900,50],
               'Quarter':[1,1,1,2,2,2,3,3,3,4,4,4],
               'District':['Kangra','Hamirpur','Kangra','Mandi',
                            'Hamirpur','Kangra','Kangra','Hamirpur',
                            'Mandi','Hamirpur','Hamirpur','Kangra'] }
df = pd.DataFrame(monthlysale )
print(df)
# Use of mode() method of DataFrame
print("\n")
print ( "Use of mode() method of DataFrame")
print(df.mode())
print("\n")
print("Use of max,min,mean,median and count\n")
pd.pivot_table(df, index = ['Salesman'], values = ['Sales'],aggfunc= ['max','min','mean','median','count'])








