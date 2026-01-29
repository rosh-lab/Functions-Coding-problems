#Write a program for generating multiplication table for a given number...
import sys
def multable(n):
    if(n<=0):
        print("{} is invalid input".format(n))
    else:
        print("-------------------------")
        print("Multiplication table for {}".format(n))
        print("---------------------------")
        for i in range(1,11):
            print("{} x {} = {}".format(n,i,n*i))
        print("---------------")
        sys.exit()
#Main program..
while(True):
    try:
        multable(int(input("Enter a number to generate mul table:")))
    except ValueError:
        print("Don't enter alnums,str,symbols and floats.")
