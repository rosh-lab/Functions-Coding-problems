#Program for demonstrating the keyword arguments..
def disp(a,b,c,d):
    print("{}\t{}\t{}\t{}".format(a,b,c,d))
#Main program,..
print("*"*50)
print("A\tB\tC\tD")
print("*"*50)
disp(10,20,30,40) #Function call with positional arguments
disp(d=40,b=20,a=10,c=30) #Function call with keyword arguments
disp(a=10,d=40,c=30,b=20) #Function call with keyword arguments
disp(10,20,d=40,c=30) #Function call with positional argumnts then keyword arguments
#disp(d=40,c=30,20,10) # Gives syntax error bcz always write first positional args then only go for keyword
#disp(a=10,d=40,c=30,b1=20) #Function call with keyword arguments but invalid gives type error bcz b1 is not there..
print("*"*50)
