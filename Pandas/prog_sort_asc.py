#Program to sort three inputted numbers in ascending order

n1= int(input("Enter the first number :"))
n2= int(input("Enter the second number :"))
n3= int(input("Enter the third number :"))
min=mid=max = None
if n1 < n2 and n1 < n3:
    if n2 < n3:
        min,mid,max = n1,n2,n3
    else:
        min,mid,max = n1,n3,n2
elif n2 < n1 and n2 < n3:
    if n1 < n3:
        min,mid,max = n2,n1,n3
else:
    if n1 < n2:
        min,mid,max = n3,n1,n2
    else:
        min,mid,max = n3,n2,n1
print("Sorted numbers in ascending order are :",min,mid,max)




        
