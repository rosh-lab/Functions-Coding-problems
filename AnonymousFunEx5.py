#Program for accepting list of values and find max and min ...Without using max() and min() predefined function...
def kvrmax(lst):
    if(len(lst)==0):
        return "Can't find max bcoz list is empty"
    elif(len(set(lst))==1):
        return "All values are equal"
    elif(len(lst)>1):
        maxv=lst[0]
        for val in lst:
            if(val>maxv):
                maxv=val
        return maxv
def kvrmin(lst):
    if(len(lst)==0):
        return "Can't find min bcoz list is empty"
    elif(len(set(lst))==1):
        return "All values are equal"
    elif(len(lst)>1):
        minv=lst[0]
        for val in lst:
            if(val<minv):
                minv=val
        return minv
findmax=lambda lst:kvrmax(lst) #Anonymous function calling normal function
findmin=lambda lst:kvrmin(lst) #Anonymous function calling normal function
#main program
print("Enter list of values separated by space:")
lst=[int(val)for val in input().split()]
maxv=findmax(lst) #Anonymous function call
minv=findmin(lst) #Anonymous function call
print("Max({})={}".format(lst,maxv))
print("Min({})={}".format(lst,minv))
