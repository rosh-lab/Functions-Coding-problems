#Program for calculating sum of two numbers:
#Input==>Taken inside of function body
#Process==>Done in function body
#output==>Displayed in function body
def sumop():
    #Input
    a=float(input("Enter first value:"))
    b=float(input("Enter second value:"))
    #Process
    c=a+b
    #Result
    print("sum({},{})={}".format(a,b,c))
#Main program....
sumop()
