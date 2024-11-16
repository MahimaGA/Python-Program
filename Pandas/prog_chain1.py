#Implementing pipelining/chaining by performing addition and division
#operation one after the other using pipe()

import pandas as pd
import numpy as np
import math
#user defined functions

def adder(adder1,adder2):
    return adder1+adder2

def divide(adder1,adder2):
    return adder1/adder2

#Create a Dictionary of series
d={'science_marks':pd.Series([22,55]),
'english_marks':pd.Series([89,87])}
df=pd.DataFrame(d)
print(df)
df1=df.pipe(adder,5).pipe(divide,2) #Pipelining/Chaining
print(df1)



