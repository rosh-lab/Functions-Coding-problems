#Program for finding sum of list of values by using reduce()
import functools
#Main program
print("Enter list of values separated by space:")
lst=[float(val) for val in input().split()]
res=functools.reduce(lambda x,y:x+y,lst)
print("Sum ({})={}".format(lst,res))