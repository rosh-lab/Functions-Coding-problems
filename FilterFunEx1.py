#Program for obtaining +ve and -ve  elements from list of values
#FilterEx1.py
def positive(val):#Normal function
    if(val>0):
        return True
    else:
        return False
def negative(val):# Normal function..
    return True if val<0 else False
#Main program
lst=[10,20,30,-40,-50,0,-96,-43,75,97,-12]
filterobj2=filter(negative,lst)
print("type of filterobj=",type(filterobj2))
#When we display an object of filter,we are getting its memory address(ID)
#So to get the content of filter object ,we must type cast to any iterable object
pslist=list(filterobj2)
nglist=tuple(filterobj2)
print("Given values=",lst)
print("list of +ve values=",pslist)
print("list of -ve values=",nglist)