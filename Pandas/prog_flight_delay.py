# Import the libraries
import matplotlib.pyplot as plt
flights_arr_delay=[-25.0,-18.0,-14.0,-8.0,8.0,11.0,12.0,19.0,20.0,33.0]
# matplotlib histogram
plt.hist(flights_arr_delay, color = 'blue', edgecolor = 'black',
         bins = int(180/5))
# Add labels
plt.title('Histogram of Arrival Delays')
plt.xlabel('Delay (min)')
plt.ylabel('Flights')
plt.show()






