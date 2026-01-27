#Program for calculating sum of two numbers:
#Input==>Taken from  function call
#Process==>Done in function body
#output==>Displayed in function body
def sumop(k,v):
    #Process
    r=k+v
    #Result
    print("sum({},{})={}".format(k,v,r))
#Main program
#get two values from keyboard
k=float(input("Enter first value:"))
v=float(input("Enter second value:"))
sumop(k,v)