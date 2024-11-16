# Use of Histogram and hist() method
import pandas as pd
import matplotlib.pyplot as plt
print("\n")
print ( "Dataframe of Values\n")
monthlysale ={'Salesman':["Ankur","Pawan","Jiten","Rahul","Pawan",
                          "Ankur","Karan","Akshit","Mudit","Jiten",
                          "Karan","Rinku"],
              'Sales' : [1000,300,800,900,1000,500,60,1000,900,50,600,450],
              'Quarter' :[1,1,1,2,2,2,3,3,3,4,4,4],
              'District': ['Wazirabad','Sirmore','Dehradun','Solan',
                           'Mandi','Kangra','Chail','Dehradun',
                           'Kangra','Solan','Mandi','Sirmore'] }
df = pd.DataFrame(monthlysale )
df.hist() #hist() by default, creates histogram for all numeric columns
plt.show()







