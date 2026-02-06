#Program for obtaining squares and square roots for list of values.
#MapFunEx3.py
print("Enter list of numerical values:")
lst=[float(val) for val in input().split()]
print("Given list of elements=",lst)
sqrlist=list(map(lambda x: x**2,lst))
sqrroots=list(map(lambda x:round(x**0.5,2),lst))
print("*"*60)
print("Given number\tSquares\t\tSquare roots")
print("*"*60)
for no,sqno,sqrtno in zip (lst,sqrlist,sqrroots):
 print("\t{} \t\t{} \t\t{}".format(no,sqno,sqrtno))
print("*"*60)
