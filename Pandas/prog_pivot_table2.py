#Illustrate pivot_table for all the columns with Filtering

import pandas as pd
sale_dict = {'ITEM_NAME':["NOTEBOOK", "PEN","INKPEN","NOTEBOOK","PEN"],\
              'AMOUNT':[100,50,30,100,50],\
              'QUANTITY':[2,5,3,3,5] }
df = pd.DataFrame(sale_dict )
print(df)
pd.pivot_table(df, index = ['ITEM_NAME','AMOUNT','QUANTITY'], aggfunc='sum')




