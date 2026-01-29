#Program for demonstrating positional arguments...
def insertstuddetails(sno,sname,marks,crs):
    print("\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs))
#MAin program..
print("*"*50)
print("SNO\t\tNAME\t\tMARKS\tCOURSE")
print("*"*50)
insertstuddetails(100,"RS",3.4,"PYTHON") #Function call with positional arguments
insertstuddetails(200,"TR",2.3,"PYTHON") #Function call with positional arguments
insertstuddetails(300,"MR",4.7,"PYTHON") #Function call with positional arguments
insertstuddetails(400,"DR",1.7,"PYTHON") #Function call with positional arguments
print("*"*50)
#Not recommened process because it takes more space for python course