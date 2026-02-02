print("Enter list of values separated by comma:")
tup=(int(val) for val in input().split(",")) # Feeling that it is a tuple but not
print("Tuple of elements",tup) #Not printed type
print(type(tup)) #Printed only class generator