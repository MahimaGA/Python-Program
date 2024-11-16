#Sorting the data in a data frame

import pandas as pd
student_marks =pd.Series({'Vijaya':80,'Rahul':92,'Meghna':67,
                          'Radhika':95,'Shaurya':97})
student_age =pd.Series({'Vijaya':32,'Rahul':28,'Meghna':30,
                          'Radhika':25,'Shaurya':20})
student_df =pd.DataFrame({'Marks':student_marks,'Age':student_age})
print(student_df)
#Sorting the data on the basis of marks in ascending order

print(student_df.sort_values(by=['Marks'])) #by keyword defines
#the field on the basis of which the data is to be sorted

print(student_df.sort_values(by=['Marks'],ascending=False)) #Sorted
#in descending order of Marks



