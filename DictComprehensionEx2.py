#Program for accepting list of words and find their length..
#DictComprehensionEx2.py
print("Enter list of words separated by space:")
wordslength={word:len(word) for word in input().split(" ")}
for w,l in wordslength.items():
    print("{}---->{}".format(w,l))
print("-------------OR---------------")
print("Enter list of words separated by space:")
for w,l in {word:len(word) for word in input().split(" ")}.items():
    print("{}---->{}".format(w,l))