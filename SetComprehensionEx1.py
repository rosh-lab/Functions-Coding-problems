print("Enter list of values separated by comma:")
set={int(val) for val in input().split(",")} # Set comprehension technique..
print("List of elements",set)
print(type(set))