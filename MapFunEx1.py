#MapFunEx1.py
def hike(sal): #Normal function
    return(sal+sal*(50/100))
#main program
oldsal=[100,600,200,300,400,500]
mapobj=map(hike,oldsal)
print("Type of mapobj=",type(mapobj))
#Type cast mapobj to list object
newsal=list(mapobj)
print("Old salary=",oldsal)
print("New salary=",newsal)
