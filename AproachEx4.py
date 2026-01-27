#Program for calculating sum of two numbers:
#Input==>Taken inside of function body
#Process==>Done in function body
#output==>Displayed in function call
def sumop():
    #take input
    a=float(input("Enter first value:"))
    b=float(input("Enter second value:"))
    #process
    c=a+b
    #Give result back to function call
    return a,b,c #here return statement is not only returning one value but also returns more than one value...
#Main program
k,v,r=sumop()#function call with multi line assignment
print("sum({},{})={}".format(k,v,r))
print("--------------OR---------------------")
res=sumop() #function call with single line assignment
#Here res is an object of <class,tuple>
print("sum({},{})={}".format(res[0],res[1],res[2]))
print("--------------OR--------------------")
print("sum({},{})={}".format(res[-3],res[-2],res[-1]))

