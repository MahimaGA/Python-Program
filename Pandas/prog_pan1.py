#Creating a Dataframe from a Dictionary
import pandas as pd

df=pd.DataFrame({"Roll no": [1,2,3,4],"Name":["ritu","niti","manu","preeti"]},
                columns=["Roll no","Name"])
print(df)
