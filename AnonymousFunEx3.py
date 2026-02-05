#Write a python program which will find max of three numbers by using anonymous function ..
findmaxthree=lambda a,b,c: a if b<=a>=c else b if a<=b>=c else c if a<=c>=b else "All values are equal"
#Main program..
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
res=findmaxthree(a,b,c)
print("Max({},{},{})={}".format(a,b,c,res))