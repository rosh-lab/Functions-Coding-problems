##Write a python program which will accept list of values and find their sum and average by using anonymous function..
def findsumavg(lst):
        s=0
        for val in lst:
            s=s+val
        else:
            avg=s/len(lst)
            return s,avg
#Main program
print("Enter list of values separated by space:")
lst=[float(val) for val in input().split()]
if (len(lst) == 0):
    print("List is empty", "Can,t find sum and average")
else:
    ss,av=findsumavg(lst)
    print("Sum({})={}\nAverage({})={}".format(lst,ss,lst,av))