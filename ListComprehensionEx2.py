#Program for accepting only +ve values from the keyboard even the user enters -ve values or zeros.
print("Enter list of numerical values separated by space:")
pslist=[int(value) for value in input().split() if int(value)>0]
print("List of +ve values=",pslist)
