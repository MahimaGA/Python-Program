#Population comparison between India and Pakistan

from matplotlib import pyplot as plt
year = [1960, 1970, 1980, 1990, 2000, 2010]
popul_pakistan = [44.91, 58.09, 78.07, 107.7, 138.5, 170.6]
popul_india = [449.48, 553.57, 696.783, 870.133, 1000.4, 1309.1]
 
plt.plot(year, popul_pakistan, color='green')
plt.plot(year, popul_india, color='orange')
plt.xlabel('Countries')
plt.ylabel('Population in million')
plt.title('India v/s Pakistan Population till 2010')
plt.show()



