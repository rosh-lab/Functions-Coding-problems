#Write a program for calculating area of rectangle by using function.Insure that the length and breadth must be +values...
def areaof():
    while(True):
        #Input
        l=float(input("Enter length:"))
        b=float(input("Enter width:"))
        #process
        if l<=0 or b<=0:
            print("Invalid input...try again")
        else:
           a=(l*b)
           #Output
           print("Area of Rectangle= {}".format(a))
           break
#main program
areaof()