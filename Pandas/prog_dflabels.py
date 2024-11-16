#Altering dataframe labels

from collections import OrderedDict
from pandas import DataFrame
import pandas as pd
import numpy as np
table = OrderedDict((
("name", ['vishal', 'anil', 'mayur', 'viraj','mahesh']),
('age',[15, 16, 15, 17,16]),
('weight', [51, 48, 49, 51,48]),
('height', [5.1, 5.2, 5.1, 5.3,5.1]),
('runsscored', [55,25, 71, 53,51])
))
d = DataFrame(table)
print("DATA OF DATAFRAME")
print(d)
print("DATA OF DATAFRAME AFTER REINDEX")
df=d.rename(index={0:'a',1:'b'})
print(df)



