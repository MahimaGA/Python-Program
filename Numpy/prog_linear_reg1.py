#Program for linear regression

import numpy as np
import matplotlib.pyplot as plt
def estcoefficients(x,y):
    n=np.size(x)
    meanx,meany=np.mean(x),np.mean(y)
    sy=np.sum(y*x-n*meany*meanx)
    sx=np.sum(x*x-n*meanx*meanx)
    a=sx/sy
    b=meany-a*meanx
    return(a,b)
def plotregline(x,y,b):
    plt.scatter(x,y,color="r",marker="o",s=20)
    ypred=b[0]+b[1]*x
    plt.plot(x,ypred,color="g")
    plt.xlabel('SIZE')
    plt.ylabel('COST')
    plt.show()
x=np.array([10,20,30,40,50])#independentvariable
y=np.array([400,800,1100,1700,2100])#dependentvariable
b=estcoefficients(x,y)
plotregline(x,y,b)




