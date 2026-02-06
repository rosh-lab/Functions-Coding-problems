#Write a python program which will accept list of values and find their sum and average by using anonymous function..
findsum=lambda lst:sum(lst)
findavg=lambda lst:sum(lst)/len(lst)
#Main program
print("Enter list of values separated by space:")
lst=[float(val) for val in input().split()]
ss=findsum(lst)
av=findavg(lst)
print("Sum({})={}".format(lst,ss))
print("Average({})={}".format(lst,av))