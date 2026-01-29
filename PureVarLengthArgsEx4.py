#Program for finding sum of variable length numerical values..
#This program will execute as it is..
def findtotal(eno,name,*vals):
    print("-----------------------")
    print("Student Number:{}".format(eno))
    print("Student Name:{}".format(name))
    s=0
    for val in vals:
        print(val,end=",")
        s=s+val
    print()
    print("Sum={}".format(s))
    print("-----------------")
#Main program..
findtotal(100,"KV",10,20,30,40,50)
findtotal(200,"RK",100,200,300,400)
findtotal(300,"HS",1.2,2.3,3.4)
findtotal(400,"TD",10,2.3,4.4,20,5.6,7.8)
findtotal(500,"VR")