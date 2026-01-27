#Program for calculating sum of two numbers:
#Input==>Taken from function call
#Process==>Done in function body
#output==>Displayed in function call
def sumop(a,b):
    c=a+b
    return c
#Main program starts
print("type of sumop=",type(sumop))
#Get two values from keyboard
k=float(input("Enter first value:"))
v=float(input("Enter second value:"))
res=sumop(k,v)#function call
print("sum ({},{})={}".format(k,v,res))