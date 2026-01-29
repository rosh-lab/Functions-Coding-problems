#PRogram for demonstrating the need of variable length arguments.
#This program will not execute as it is bcoz PVM is performing interpretation process and it remembers the latest function definition (bcoz we have family of similar function names with variable/changeability positional args/parameters)
def disp(a,b,c,d,e): #Function definition 1 with 5 formal pos parameters
    print(a,b,c,d,e)
def disp(a,b,c,d): #Function definition 2 with 4 formal pos parameters
    print(a,b,c,d)
def disp(a,b,c): #Function definition 3 with 3 formal pos parameters
    print(a,b,c)
def disp(a,b): #Function definition 4 with 2 formal pos parameters
    print(a,b)
def disp(a): #Function definition 5 with 1 formal pos parameters
    print(a)
def disp(): #Function definition 6 with 0 formal pos parameters
    print("Empty")
def disp(a, b, c, d, e,f):  # Function definition 7 with 6 formal parameters
        print(a, b, c, d, e,f)
#Main program..
disp(10,20,30,40,50) #Function call 1 with 5 arguments...
disp(10,20,30,40) #Function call 2 with 4 arguments...
disp(10,20,30) #Function call 3 with 3 arguments...
disp(10,20) #Function call 2 with 2 arguments...
disp(10) #Function call 1 with 1 arguments...
disp() #Function call 6 with 0 arguments...
disp("TR",2+3j,True,101,102.23,"MR") #Function call 7 with 6 arguments