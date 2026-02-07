#Write a python program which will find the max value from list of numbers.....by using reduce ()
import functools
print("Enter list of values separated by space:")
values=[float(val) for val in input().split()]
print("Given values:")
print(values)
#Find max by using reduce()
val=functools.reduce(lambda k,v:k if k>v else v,values)
print("max=",val)
#Find min by using reduce()
val=functools.reduce(lambda k,v:k if k<v else v,values)
print("min=",val)
