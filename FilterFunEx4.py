#Program which will accept list of words and obtain only palindrome words by using filter() and anonymous function..
print("Enter list of words separated by space:")
words=[ word for word in input().split()]
print("Given words",words)
#Get palindrome
palwords=list(filter(lambda word:word==word[::-1],words))
print("List of palindrome words",palwords)