#PRogram for demonstrating the need of variable length arguments.
#This program will execute as it is..
def disp(a,b,c,d,e): #Function definition 1 with 5 formal pos parameters
    print(a,b,c,d,e)
disp(10,20,30,40,50) #Function call 1 with 5 arguments...
print("-----------------------------------------------------------")
def disp(a,b,c,d): #Function definition 2 with 4 formal pos parameters
    print(a,b,c,d)
disp(10,20,30,40) #Function call 2 with 4 arguments...
print("----------------------------------------------")
def disp(a,b,c): #Function definition 3 with 3 formal pos parameters
    print(a,b,c)
disp(10,20,30) #Function call 3 with 3 arguments...
print("-"*50)
def disp(a,b): #Function definition 4 with 2 formal pos parameters
    print(a,b)
disp(10,20) #Function call 2 with 2 arguments...
print("-"*50)
def disp(a): #Function definition 5 with 1 formal pos parameters
    print(a)
disp(10) #Function call 1 with 1 arguments...
print("-"*50)
def disp(): #Function definition 6 with 0 formal pos parameters
    print("Empty")
disp() #Function call 6 with 0 arguments...
print("-"*50)
def disp(a, b, c, d, e,f):  # Function definition 7 with 6 formal parameters
        print(a, b, c, d, e,f)
disp("TR",2+3j,True,101,102.23,"MR") #Function call 7 with 6 argument
print("-"*50)
#Limitation....
# In this program----we have 7 function call-------7function definition
#In genral-----we have n-function calls---we need n-func def---waste of time ,takes more development time..
#SO,,,we need n-function calls to 1 fun definition only..





