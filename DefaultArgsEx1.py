#Program for demonstrating Default arguments technique.
def insertstuddetails(sno,sname,marks,crs="PYTHON"): # Function definition with  positional formal parametre & default arguments and it is always recommed to write default argu  after possitional arguments only
    print("\t{}\t\t{}\t\t{}\t\t{}".format(sno,sname,marks,crs))
#MAin program..
print("*"*50)
print("SNO\t\tNAME\t\tMARKS\tCOURSE")
print("*"*50)
insertstuddetails(100,"RS",3.4) #Function call with positional arguments
insertstuddetails(200,"TR",2.3) #Function call with positional arguments
insertstuddetails(300,"MR",4.7) #Function call with positional arguments
insertstuddetails(400,"DR",1.7) #Function call with positional arguments
print("*"*50)