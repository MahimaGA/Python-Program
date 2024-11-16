#Illustrating the use of pivot_table() method
import pandas as pd
name_dict = { 'INVIGILATOR' : ["Rajesh", "Naveen","Anil","Naveen","Rajesh"],\
              'AMOUNT' : [550,550,550,550,550], }
df = pd.DataFrame(name_dict )
print(df)
pd.pivot_table(df, index = ['INVIGILATOR'],aggfunc="sum")


