#Iterable object with function example1.py
def dispvalues(obj):
    print("type of obj=",type(obj))
    print("Number of value={}".format(len(obj)))
    print("--------------------------")
    if (type(obj)==dict):
        for key,value in obj.items():
            print("{}---->{}".format(key,value))
    else:
         for val in obj:
             print("{}".format(val))
    print("--------------------------")
#MAin program
lst=[10,"Rossum",34.56,2+3j,True]
dispvalues(lst) #Function call taking list object
tpl=(100,"Travis",34.56,56,"Python","Gnome")
dispvalues(tpl) #Function call with tuple object
st={10,20,30,40,50,60,70,80}
dispvalues(st) #Function call with set object
dispvalues(()) #Function call taking empty tuple object
dispvalues([]) #Function call taking empty list object
dispvalues({}) #Function call taking empty dict object
dispvalues(set()) #Function call taking empty set object
d={10:"Python",20:"Java",30:"Django",40:"Html"}
dispvalues(d)