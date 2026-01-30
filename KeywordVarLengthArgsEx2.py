#Program for demonstrating the need of keyword variable length arguments..
#This program will execute but takes more development time ..so not recommended
#KeywordVarLengthArgsEx2.py
def dispvalues(sno,sname,marks,cname):#Function def-1
    print(sno,sname,marks,cname)
dispvalues(sno=100,sname="RS",marks=45.67,cname="OUCET")#Function call 1 with 4 keyword var lenargs
print("------------------------------------")
def dispvalues(eno,ename,sal,compname,dsg): #Function def-2
    print(eno,ename,sal,compname,dsg)
dispvalues(eno=1000,ename="TR",sal=5.6,compname="TCS",dsg="HR")#Function call 2 with 5 keyword var len args
print("------------------------------------")
def dispvalues(sid,stname,hb1,hb2,hb3,hb4):# Function def-3
    print(sid,stname,hb1,hb2,hb3,hb4)
dispvalues(sid=200,stname="abc",hb1="sleeping",hb2="Eating",hb3="Chatting",hb4="Roaming")#Function call 3 with 6 keyword var len args
print("--------------------------------")
def dispvalues(tno,tname,sub1):# Function def-4
    print(tno,tname,sub1)
dispvalues(tno=300,tname="Rossum",sub1="PYTHON-JAVA")# Function call 4 with 3 keyword var len args
print("----------------------------")
def dispvalues(cid):#Function def-5
    print(cid)
dispvalues(cid=500) #Function call 5 with 1 keyword var leng args
#Limitation....
# In this program----we have 7 function call-------7function definition
#In genral-----we have n-function calls---we need n-func def---waste of time ,takes more development time..
#SO,,,we need n-function calls to 1 fun definition only..





