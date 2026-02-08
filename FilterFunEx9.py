#Given text::Str21i74ng6
#1..Obtain all alphabets and sort them in ascending order...
#2...Obtain all numerical values and separate them even and odd.
text=input("Enter a line of text::")
alphabets=sorted(filter(lambda ch: ch.isalpha(),text))
#2...
numbers=list(map(int,filter(lambda ch:ch.isdigit(),text)))
#Separate even and odd..
even_numbers=list(filter(lambda ch:ch%2==0,numbers))
odd_numbers=list(filter(lambda ch:ch%2!=0,numbers))
print("===============================================")
print("Alphabets in ascending order",alphabets)
print("Even numbers",even_numbers)
print("Odd numbers",odd_numbers)