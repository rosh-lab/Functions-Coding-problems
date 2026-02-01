#Program for demonstrating the global keyword....
def incr():
    global a #here global is a keyword
    a=a+1
def modify():
    global a
    a=a*2
#main program..
a=10 # here a is called global variable..
print("In main program---value of a before incr()={}".format(a))
incr() #Function call
print("In main program---value of a after incr()={}".format(a))
modify()#function call..
print("In main program---value of a after modify()={}".format(a))