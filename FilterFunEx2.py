#Program for obtaining +ve and -ve  elements from list of values
#FilterEx2.py
positive=lambda val:True if val>0 else False #Anonymous function def
negative=lambda val:True if val<0 else False #Anonymous function def
#Main program
print("Enter list of values separated by space:")
lst=[int(value) for value in input().split()]
pslist=list(filter(positive,lst))
nglist=tuple(filter(negative,lst))
print("Given values=",lst)
print("list of +ve values=",pslist)
print("list of -ve values=",nglist)