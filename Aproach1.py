#Define a function for calculating sum of two numbers..
print("I am before fun def")
def sumop(x,y):# here x and y are called formal parameters
    r=x+y #here r is called local variables or local parameter
    print("I am inside of function definition")
    return r
res=sumop(2,5) #Function call
print("sum=",res)
print("I am after fun def")
print("--------------")
res=sumop(100,200)
print("sum=",res)