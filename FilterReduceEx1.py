#Program for accepting list of numerical values and find +ve values sum and -ve values sum
import functools
print("Enter list of numerical values separated by space:")
vals=[float(val) for val in input().split()]
print("Given List of values=",vals)
print("============================")
#Filter +ve values..
posvalues=list(filter(lambda k:k>0,vals))
print("Positive values are...")
print(posvalues)
#Positive values sum==
possum=functools.reduce(lambda k,v:k+v,posvalues)
print("Positive values sum={}".format(possum))
print("============================")
#Filter -ve values..
negvalues=list(filter(lambda k:k<0,vals))
print("Negative values are...")
print(negvalues)
#Negative values sum==
negsum=functools.reduce(lambda k,v:k+v,negvalues)
print("Negative values sum={}".format(negsum))
print("============================")