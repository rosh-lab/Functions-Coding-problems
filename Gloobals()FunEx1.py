a=10
b=20 #here a and b are called programmer defined global varaiables..
def operations():
    d=globals() #Here globals() returns dictionary..
    print(len(d))
    print("----------------------")
    print("Invisible global variables")
    for gvn,gvv in d.items():
        print("{}---->{}".format(gvn,gvv))
    print("-----------------------")
    print("Programmer defined global variables Information- Way 1")
    print("-------------------------------")
    print("value of a=",d.get('a'))
    print("value of b=",d.get('b'))
    print("---------------------------------")
    print("Programmer defined global variables Information- Way 2")
    print("-------------------------------")
    print("value of a=", d['a'])
    print("value of b=", d['b'])
    print("---------------------------------")
    print("Programmer defined global variables Information- Way 3")
    print("-------------------------------")
    print("value of a=", globals()['a'])
    print("value of b=", globals()['b'])
    print("---------------------------------")
    print("Programmer defined global variables Information- Way 4")
    print("-------------------------------")
    print("value of a=",globals().get('a'))
    print("value of b=", globals().get('b'))
    print("---------------------------------")
#Main program
operations()