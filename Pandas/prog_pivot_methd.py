#Pivoting using pivot() method
#Creating a DataFrame
import pandas as pd
ClassXII_result= {'Name':['Radhika','Sonia','Shaurya','Radhika'],\
                  'Subject':['IP','CS','Maths','Phy'],\
                  'Marks':[98,87,99,87],\
                  'Grade':['A1','A2','A1','B']}
df= pd.DataFrame(ClassXII_result,columns=['Name','Subject','Marks','Grade'])
print(df)







