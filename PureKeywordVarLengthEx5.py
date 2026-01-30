#Program for calculating total marks of different students who are studing in different classes with different subject with different secured marks....
def findtotalmarks(sno,sname,cls,*vals,city="Hyderabad",**submarks):
    print("*"*50)
    print("Variable length values={}".format(vals))
    print("*"*50)
    print("\tStudent Number:{}".format(sno))
    print("\tStudent Name:{}".format(sname))
    print("\tClass:{}".format(cls))
    print("\tSubject\t Marks")
    print("\tCity:{}".format(city))
    print("*"*50)
    totmarks=0
    for subject,marks in submarks.items():
        print("\t{}\t\t{}".format(subject,marks))
        totmarks=totmarks+marks
    print("Total Marks:{}".format(totmarks))
    print("*"*50)
#MAin program
findtotalmarks(10,"Roshan","X",10,20,30,40,50,Tel=60,Eng=70,Hindi=50,Maths=89,Sci=88,Soc=99)# Function call-1
findtotalmarks(20,"Arshad","XII",100,200,300,400,Sanskrit=99,Eng=89,Maths=75,Physics=60,Chemistry=60)# Function call-2
findtotalmarks(30,"Jemmy","B.tech",1.2,2.3,4.5,OS=50,DBMS=45,NW=48) #Function call-3
findtotalmarks(40,"Brijesh","B.sc",-10,-20,-30,-40) #function call 4
findtotalmarks(40,"Raj","4th",drawing=40) #Function call-5
findtotalmarks(50,"Ram","5th",5,4,3,2,1,arts=40,an=89,city="MUM") #Function call-6
findtotalmarks(60,"Shyam","6th",-5,-3,-4,-7,city="Ap",ex=40,rd=90,gn=47) #Function call-7
findtotalmarks(60,"KV","Trainer") #Function call-8