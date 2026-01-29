#Program for demonstrating positional arguments...
def insertstuddetails(eno,ename,sal):
    print("\t{}\t{}\t{}".format(eno,ename,sal))
#MAin program..
print("*"*50)
print("\t\t ENO \t NAME \tSALARY")
print("*"*50)
insertstuddetails(100,"RS",3.4) #Function call with arguments values which is called Possitional arguments.
insertstuddetails(200,"TR",2.3) #Function call with arguments values which is called Possitional arguments.
insertstuddetails(300,"MR",4.7) #Function call with arguments values which is called Possitional arguments.
insertstuddetails(400,"DR",1.7) #Function call with arguments values which is called Possitional arguments.
print("*"*50)