#Comparing two series
import pandas as pd
a =pd.Series([1,2,7,5,4])
b =pd.Series([4,8,9,5,10])
print("First Series is: ")
print(a)
print("Scond Series is: ")
print(b)
print("Comparing the elements of both the series ")
print("Equals")
print(a == b)
print("Greater than: ")
print(a > b)
print("Less than: ")
print(a < b)
print("Adding two series :")
c = a + b
print(c)
print("subtracting two series: ")
c = a - b
print(c)
print("Product of two series: ")
c = a * b
print(c)
print("Divide series1 by series2 : ")
c = a/b
print(c)




