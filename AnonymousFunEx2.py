#Write a program which will find biggest of two numbers by using anonymous function and check for equality..
#AnonymousFunEx2.py
findmaxtwo=lambda k,v: k if k>v else v if v>k else "Both Values are equal"
#Main program
a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
res=findmaxtwo(a,b)
print("Max({},{})={}".format(a,b,res))