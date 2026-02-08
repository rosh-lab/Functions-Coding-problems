#write a python program which will implement the following.....
#1-->Filter all upper case letter and concat them..
#2--->Filter all numerical values and concat them..
#3--->Filter all special symbols and display them..
text=input("Enter a line of text:")
#Filter uppercase letters
uppercase=" ".join(list(filter(lambda ch: ch.isupper(),text)))
print("Uppercase letters:",uppercase)
#Filter Numerical values..
numbers=" ".join(list(filter(lambda ch: ch.isdigit(),text)))
print("Numbers:",numbers)
#Filter symbols..
symbols=" ".join(list(filter(lambda ch: not ch.isalnum(),text)))
print("Symbols:",symbols)