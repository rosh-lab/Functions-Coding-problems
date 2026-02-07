#Program which will accept list of words and concatenate them by using reduce functions.
import functools
def concatop(x,y):
    return (x+" "+y)
print("Enter list of words separated by comma:")
words=[word for word in input().split(",")]
print("Given words are......")
print(words)
#Code for concatenating words which are present in list...
line=functools.reduce(concatop,words)
print(line)