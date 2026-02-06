#Write a python program which will implement the following..
#Given line of text==Python3 i4s a7n oo8p lan9g
#Extract the digits from this line...
line=input("Enter a line of text:")
digits=list(filter(lambda ch:ch.isdigit(),line))
print("Digits found")
print(",".join(digits))