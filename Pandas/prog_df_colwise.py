#Implementing iteritems()-displaying dataframe contents columnwise
import pandas as pd
total_sales ={2015:{'Qtr1':34500,'Qtr2':45000,'Qtr3':50000,'Qtr4':39000},
              2016:{'Qtr1':44500,'Qtr2':65000,'Qtr3':70000,'Qtr4':49000},
              2017:{'Qtr1':44500,'Qtr2':65000,'Qtr3':70000,'Qtr4':49000}}
df= pd.DataFrame(total_sales)   #Converting data series into Data frame
for (col,colSeries) in df.iteritems():  #displaying column-wise data
    print("Column Index :",col)
    print("Containing :")
    print(colSeries)




    



    










                    
