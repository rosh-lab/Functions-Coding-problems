print("Enter list of values separated by comma:")
x=(int(val) for val in input().split(",")) # Here x is called an object of <class,generator>
t=tuple(x) #Typecasting generator object into tuple object.
print("Tuple of elements",t)
print(type(t))