#Program which will accept list of values and find max and min by using anonymous function..
findmax=lambda lst:"All are equal" if len(set(lst))==1 else max(lst)
findmin=lambda lst:"All are equal" if len(set(lst))==1 else min(lst)
#Main program
print("Enter list of values separated by space:")
lst= [int(val) for val in input().split()]
print("Max({})={}".format(lst,findmax(lst)))
print("Min({})={}".format(lst,findmin(lst)))