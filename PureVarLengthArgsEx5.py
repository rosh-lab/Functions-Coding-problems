#Program for finding sum of variable length numerical values..
#This program will execute as it is..
def findtotal(eno,sname,*vals,city="HYD",crs="PYTHON"): #Default always written at last....after *param(Var length )
    print("-----------------------")
    print("Student Number:{}".format(eno))
    print("Student Name:{}".format(sname))
    print("Student City:{}".format(city))
    print("Student Course:{}".format(crs))
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
findtotal(crs="HTML",eno=600,sname="BR",city="USA")
findtotal(700,"MR",-1,-2,-3,-1.55,-3.123,5.66,city="AUS")
#findtotal(crs="JAVA",eno=800,sname="JP",-33,-44,-54,43,-32) # syntax error bcoz positional arguments follow the keyword args
findtotal(800,"JJ",-11,-12,-23,-44,-56,332,-333,crs="JAVA",city="MUM")