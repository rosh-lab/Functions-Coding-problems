#Write a python program which will implement the following.
#Extract the special symbols from the given line of text..
line=input("Enter a line of text::")
spsymbol=list(filter(lambda ch: not ch.isalnum()and not ch.isspace(),line))
print("Special symbols:",spsymbol)
print(",".join(spsymbol))