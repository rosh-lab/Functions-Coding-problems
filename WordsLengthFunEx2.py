#Program which will accept a line of text and find length of each word..
import sys
def findwordslength(line):
    if(len(line.strip())==0):
        print("You must enter a line of text")
    elif(line.isdigit()):
        print("You can't enter digits")
    else:
        words=line.split()
        d=dict()
        print("*"*50)
        print("*" * 50)
        for word in words:
            d[word]=len(word)
        print("*" * 50)
        print("----------------")
        for word ,wordlen in d.items():
            print("{}---> {}".format(word,wordlen))
        print("----------------------------")
        sys.exit()
#Main program
while(True):
    line=input("Enter a line of text:")
    findwordslength(line)