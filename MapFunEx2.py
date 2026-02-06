#MapFunEx2.py
oldsal=[100,600,200,300,400,500]
mapobj=map(lambda sal:sal*1.50,oldsal) #Anonymous function
print("Type of mapobj=",type(mapobj))
#Type cast mapobj to list object
newsal=list(mapobj)
print("Old salary=",oldsal)
print("New salary=",newsal)
