#Program for demonstrating the need of keyword variable length arguments..
#This program will not execute as it is bcoz PVM is performing interpretation process and it remembers the latest function definition (bcoz we have family of similar function names with keyword  variable length positional args/parameters)
#KeywordVarLengthArgsEx1.py
def dispvalues(sno,sname,marks,cname):#Function def-1
    print(sno,sname,marks,cname)
def dispvalues(eno,ename,sal,compname,dsg): #Function def-2
    print(eno,ename,sal,compname,dsg)
def dispvalues(sid,stname,hb1,hb2,hb3,hb4):# Function def-3
    print(sid,stname,hb1,hb2,hb3,hb4)
def dispvalues(tno,tname,sub1):# Function def-4
    print(tno,tname,sub1)
def dispvalues(cid):#Function def-5
    print(cid)
#Main program
dispvalues(sno=100,sname="RS",marks=45.67,cname="OUCET")#Function call 1 with 4 keyword var length args
dispvalues(eno=1000,ename="TR",sal=5.6,compname="TCS",dsg="HR")#Function call 2 with 5 keyword var length args
dispvalues(sid=200,stname="abc",hb1="sleeping",hb2="Eating",hb3="Chatting",hb4="Roaming")#Function call 3 with 6 keyword var length args
dispvalues(tno=300,tname="Rossum",sub1="PYTHON-JAVA")# Function call 4 with 3 keyword var length args
dispvalues(cid=500) #Function call 5 with 1 keyword var length args