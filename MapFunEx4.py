#Program for finding sum of two list objects..
print("Enter numerical values for first list:")
lst1=[float(val) for val in input().split()]
print("Enter numerical values for second list:")
lst2=[float(val) for val in input().split()]
lst3=list(map(lambda x,y:x+y,lst1,lst2))
print("*"*50)
print("First list\t\tSecond list\t\tSum list")
print("*"*50)
for no1,no2,no3 in zip(lst1,lst2,lst3):
    print("{}\t\t\t{}\t\t\t{}".format(no1,no2,no3))
print("*"*50)