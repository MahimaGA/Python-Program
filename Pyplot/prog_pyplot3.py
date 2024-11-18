#To plot a square through function using pyplot
import matplotlib.pyplot as plt
def square(x, y):    
    '''
    Objective: To plot a square
    Input Parameters: x, y - lists of x coordinates and y
    coordinates respectively
    Return Value: None
    '''
    
    if (x[1] - x[0]) <= 0:
        return
    plt.plot(x, y, 'ro--')
    
    return square([x[0]+1, x[1]-1, x[2]-1, x[3]+1, x[4]+1],[y[0]+1, y[1]+1, y[2]-1, y[3]-1, y[4]+1])
    
       
def main():
    '''
    Objective: To plot a square based on user input
    Input Parameter: None
    Return Value: None
    '''
    
    size = int(input('Enter size of the square: '))
    x = [0, size, size, 0, 0]
    y = [0, 0, size, size, 0]
    square(x, y)
    plt.title('Square')
    plt.axis([min(x)-1, max(x)+1, min(y)-1, max(y)+1])
    plt.grid()
    plt.show()

    
if __name__ == '__main__':
    main()


    
