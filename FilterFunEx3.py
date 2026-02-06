#Program for obtaining +ve and -ve  elements from list of values
#FilterEx2.py
#Main program
print("Enter list of values separated by space:")
lst=[int(value) for value in input().split()]
pslist=list(filter(lambda val:True if val>0 else False,lst))
nglist=tuple(filter(lambda val:True if val<0 else False,lst))
print("Given values=",lst)
print("list of +ve values=",pslist)
print("list of -ve values=",nglist)