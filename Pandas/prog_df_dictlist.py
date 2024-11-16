#Creating data frame by passing a list of dictionaries

import pandas as pd
newstudent =[{'Rinku':67,'Ritu':78,'Ajay':75,'Pankaj':88,'Aditya':92},
             {'Rinku':77,'Ritu':58,'Ajay':87,'Pankaj':65},
             {'Rinku':88,'Ajay':67,'Pankaj':74,'Aditya':70}]

newdf =pd.DataFrame(newstudent)
print(newdf)












