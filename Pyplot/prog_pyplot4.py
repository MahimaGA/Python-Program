#Program to plot frequency of marks using Line Chart
import matplotlib.pyplot as plt

def fnplot(list1):
	plt.plot(list1)
	plt.title("Marks Line Chart")
	plt.xlabel("Value")
	plt.ylabel("Frequency")
	plt.show()

list1=[50,50,50,65,65,75,75,80,80,90,90,90,90]
fnplot(list1)




