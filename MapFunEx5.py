#Program for finding sum of two list objects..
print("Enter numerical values for first list:")
lst1=[float(val) for val in input().split()]
print("Enter numerical values for second list:")
lst2=[float(val) for val in input().split()]
#Logic
if(len(lst1))>len(lst2):
    for i in range(len(lst1)-len(lst2)):
        lst2.append(0.0)
elif(len(lst2)>len(lst1)):
    for i in range(len(lst2)-len(lst1)):
        lst1.append(0.0)
#Now list values becomes equal and add them by using map()
lst3=list(map(lambda x,y:x+y,lst1,lst2))
print("*"*50)
print("First list\t\tSecond list\t\tSum list")
print("*"*50)
for no1,no2,no3 in zip(lst1,lst2,lst3):
    print("{}\t\t\t\t{}\t\t\t\t\t{}".format(no1,no2,no3))
print("*"*50)