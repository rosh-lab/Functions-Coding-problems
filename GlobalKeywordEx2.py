def update1():
    global a,b
    a=a+1
    b=b+1
def update2():
    global a,b
    a=a*2
    b=b*2
def update3():
    #No need to write global keyword because here we are just accessing global var values a and b..
    c=a+10
    d=b+10
    print("Local c={} Local d={}".format(c,d))
def update4():
    global a
    a=a+b
#Main program
a,b=10,20 #Multiline assingnment
print("Main program before update1() a={} b={}".format(a,b))
update1()
print("Main program after update1() a={} b={}".format(a,b))
update2()
print("Main program after update2() a={} b={}".format(a,b))
update3()
print("Main program after update3() a={} b={}".format(a,b))
update4()
print("Main program after update4() a={} b={}".format(a,b))