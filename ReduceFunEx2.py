#Program for finding sum of list of values by using reduce() second way
import functools
def operations(k,v):
    return(k+v)
#Main program
print("Enter list of values separated by space:")
lst=[float(val) for val in input().split()]
res=functools.reduce(operations,lst)
print("Sum ({})={}".format(lst,res))