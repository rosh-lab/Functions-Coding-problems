#Write a python program which will accept a word or numerical value and decide whether it is palindrome or not by using anonymous function.
findpalindrome=lambda value:"Palindrome" if value==value[::-1] else "Not Palindrome"
#Main program
value=input("Enter a word or a numerical value which you want:").upper()
res=findpalindrome(value)
print("{} is {}".format(value,res))