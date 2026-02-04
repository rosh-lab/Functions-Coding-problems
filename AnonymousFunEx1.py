#Define a function for calculating sum of two numbers by using normal func and by using anonymous function..
#AnonymousFunEx1.py
def sumop(a,b): #Normal function
    return a+b
addop=lambda k,v:k+v #Anonymous function
#Main program
print("type of sumop=",type(sumop))
res=sumop(100,200) #Normal function call
print("Sum by using Normal Function=",res)
print("------------------------------------")
print("type of addop=",type(addop))
res=addop(1000,2000) #Anonymous function call
print("Sum by using Anonymous Function=",res)
print("-------------------------------")
print("Enter two values:")
a,b=float(input()),float(input())
r=addop(a,b) #Anonymous function call
print("Sum of {},{}--->{}".format(a,b,r))
