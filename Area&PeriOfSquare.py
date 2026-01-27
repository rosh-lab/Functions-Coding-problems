#Write a program for calculating area and perimeterof square by using function.Insure that the side must be +values..
def areaop():
    while(True):
        #Input
        s=float(input("Enter the side: "))
        #process
        if s<=0:
            print("Invalid input...try again")
        else:
            area=s*s
            perimeter=4*s
        #Output
            print("Area of square={}".format(area))
            print("Perimeter of square={}".format(perimeter))
            break
#main program
areaop()