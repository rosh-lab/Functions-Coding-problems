##Write a program for calculating area and perimeter of circle by using function.Insure that the radius must be +values...
def areaop():
    while(True):
        #Input
        rad=float(input("Enter radius: "))
        #process
        if(rad<=0):
            print("Invalid input...try again")
        else:
             ac=3.14*rad**2
             pc=2*3.14*rad
             #Output
             print("Area of circle={}".format(ac))
             print("Perimeter of circle={}".format(pc))
             break
#main program
areaop()
print("Program ends here")