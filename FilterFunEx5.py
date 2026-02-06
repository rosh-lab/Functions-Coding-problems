#Write a python program which will accept list of words and obtain those words whose length ranges from 3 to 4..
print("Enter list of words separated by comma:")
words=[word for word in input().split(",")]
print("Given words=",words)
words34=list(filter(lambda word:word.isalpha() and 3<=len(word)<=4,words))
#Words that lies between 3 or 4..
print("Words34=",words34)