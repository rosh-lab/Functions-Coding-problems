#Program which will accept a line of text and find length of each word..
import sys
def findwordslength(line):
    if(len(line.strip())==0):
        print("You must enter a line of text")
    elif(line.isdigit()):
        print("You can't enter digits")
    elif( not line.isdigit()):
        print("Can't enter special symbols")
    else:
        words=line.split()
        for ch in words:
            print("{}--->{}".format(ch,len(ch)))
        sys.exit()
#Main program
while(True):
    line=input("Enter a line of text:")
    findwordslength(line)