print("Enter list of values separated by comma:")
d={int(val):int(val)**2 for val in input().split(",")} # Dict comprehension technique..
print("Dict of elements",d)
print(type(d))
for k,v in d.items():
    print("{}---->{}".format(k,v))