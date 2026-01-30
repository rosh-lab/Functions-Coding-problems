#Program for calculating total marks of different students who are studing in different classes with different subject with different secured marks....
def findtotalmarks(sno,sname,cls,**submarks): #city="Hyderabad"): #**param written always at last only otherwise gets syntax error
    print("*"*50)
    print("\tStudent Number:{}".format(sno))
    print("\tStudent Name:{}".format(sname))
    print("\tClass:{}".format(cls))
    print("\tSubject\t Marks")
   # print("\tCity:{}".format(city)) #Default args written here which is not correct
    print("*"*50)
    totmarks=0
    for subject,marks in submarks.items():
        print("\t{}\t\t{}".format(subject,marks))
        totmarks=totmarks+marks
    print("Total Marks:{}".format(totmarks))
    print("*"*50)
#MAin program
findtotalmarks(10,"Roshan","X",Tel=60,Eng=70,Hindi=50,Maths=89,Sci=88,Soc=99)# Function call-1
findtotalmarks(20,"Arshad","XII",Sanskrit=99,Eng=89,Maths=75,Physics=60,Chemistry=60)# Function call-2
findtotalmarks(30,"Jemmy","B.tech",OS=50,DBMS=45,NW=48) #Function call-3
findtotalmarks(40,"Brijesh","B.sc") #function call 4
findtotalmarks(40,"Raj","4th",drawing=40)