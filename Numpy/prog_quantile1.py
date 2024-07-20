#Program on Quantile
import pandas as pd
import numpy as np
df= pd.DataFrame(np.array([[1, 1], [2, 10], [3, 100], [4, 1000]]),columns=['a', 'b'])
print(df)
print(df.quantile(0.5))  #50% quantile or median











