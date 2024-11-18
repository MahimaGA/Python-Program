#pyplot program-2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
excel_file = 'student.xlsx'
sdetail = pd.read_excel(excel_file)
sdetail.set_index('Name',inplace=True)
ssort=sdetail.sort_values(['marks'],ascending=True)
print(ssort.head())
ssort['marks'].head().plot()            # for line Graph
#ssort['marks'].head().plot(kind="barh")# for Bar chart
#ssort['marks'].head().plot(kind="pie") # for pie chart
plt.show()
