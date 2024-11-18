import matplotlib.pyplot as plt
# Plot data
stream =['Medical','Non-Medical','Comm with Maths','Comm with IP','Humanities']
no_students = [32,41,55,60,50]
colors = ['red', 'gold', 'yellowgreen', 'blue', 'lightcoral']
# explode 1st slice
explode = (0.1, 0, 0, 0,0)  
# Plot
plt.pie(no_students, explode=explode, labels=stream, colors=colors)
plt.title("Grouping of Students on the basis of Allocated Streams" )
plt.show()






