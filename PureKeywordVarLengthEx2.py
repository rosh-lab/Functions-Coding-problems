#Program for Pure keyword variable length arguments..
#Program will execute as it is...
def dispvalues(**ros): # Here first*===>>stores key values and second*==>>stores values of value...
# here **param==>>is called keyword variable length args whose type is dict...
    print("---------------------------")
    print("Number of values in keyword variable length arguments=",len(ros))
    for k,v in ros.items():
        print("{}---->>{}".format(k,v))
    print()
    print("--------------------------------")
#Main program
dispvalues(sno=100,sname="RS",marks=45.67,cname="OUCET")#Function call 1 with 4 keyword var length args
dispvalues(eno=1000,ename="TR",sal=5.6,compname="TCS",dsg="HR")#Function call 2 with 5 keyword var length args
dispvalues(sid=200,stname="abc",hb1="sleeping",hb2="Eating",hb3="Chatting",hb4="Roaming")#Function call 3 with 6 keyword var length args
dispvalues(tno=300,tname="Rossum",sub1="PYTHON-JAVA")# Function call 4 with 3 keyword var length args
dispvalues(cid=500) #Function call 5 with 1 keyword var length args
dispvalues() #Function call 6 with 0 keyword var length args