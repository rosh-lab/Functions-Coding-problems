#program for demonstrating globals()
a=10
b=20
c=30
d=40 #Here a,b,c,d are called global variables
def operations():
    a=100
    b=200 # Here pvm gives the first priority to local variables only and it forgets about global varaibles
    c=300
    d=400 #Here a,b,c,d are called local variables...
    res=a+b+c+d+globals()['a']+globals()['b']+globals()['c']+globals()['d']
    print("sum=",res)
#Main program
operations()