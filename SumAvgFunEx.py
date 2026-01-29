#Write a program which will accept list of values and find sum and average by using function..
def readvalues():
    nov=int(input("Enter how many values sum and average you want to find:"))
    if(nov<=0):
        return [] # Returning Empty list
    else:
        lst=[] #Create an empty list for appending values
        for i in range(1,nov+1):
            val=float(input("Enter {} value::".format(i)))
            lst.append(val)
        return lst
def findsumavg(lstobj):
    if(len(lstobj)==0):
        print("No values present ..Can't find sum and average")
    else:
        s=0
        for val in lst:
            s=s+val
        else:
            print("------------------------------")
            print("Given list of elements={}".format(lst))
            print("Sum={}".format(s))
            print("Average={}".format(s/len(lst)))
            print("----------------------------")
#Main program
lst=readvalues() #Function call
findsumavg(lst) # Function call