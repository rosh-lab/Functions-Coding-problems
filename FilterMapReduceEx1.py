#Write a python program which will implement the following..7 cases...
#1.. Accept list of salaries ranges within 0 to 1000..
import functools
def filtermapreduce():
    print("Enter list of salaries ranges from 0 to 1000:")
    oldsal=[float(sal) for sal in input().split() if 0<=float(sal)<=1000]
    print("Given salaries")
    print(oldsal)
#2..Obtain list of salaries ranges from 0 to 500.
    sal0_500=list(filter(lambda sal:0<=sal<=500,oldsal))
    #print(sal0_500)
#3..Obtain list of salaries ranges from 501 to 1000.
    sal501_1000=list(filter(lambda sal:501<=sal<=1000,oldsal))
    #print(sal501_1000)
#4...Give 10% hike to those employees whose sal ranges from 0 to 500
    hikesal0_500=list(map(lambda sal:sal+sal*10/100,sal0_500))
    #print(hikesal0_500)
#5...Give 20% hike to those employees whose sal ranges from 501 to 1000
    hikesal501_1000=list(map(lambda sal:sal+sal*20/100,sal501_1000))
    #print(hikesal501_1000)
    print("-------------------------------------------------------------")
    print("\t\t Sal0-500 \t\t\tHikeSal0-500")
    print("-----------------------------------------------------------------")
    for sal1,sal2 in zip(sal0_500,hikesal0_500):
        print("\t\t{} \t\t\t{}".format(sal1,sal2))
#Find the total salary of employees whose salary ranges from 0 to 500 before and after hike.
    totsal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,sal0_500) #Before hike
    tothikesal0_500=functools.reduce(lambda sal1,sal2:sal1+sal2,hikesal0_500)  #After hike
    print("-----------------------------------------------------------------")
    print("\t\tTotal::{}\t\tTotal::{}".format(totsal0_500,tothikesal0_500))
    print("-----------------------------------------------------------------")
    print("*"*60)
    print("\t\tSal501-1000 \t\t\tHikeSal501-1000")
    print("-----------------------------------------------------------------")
    for sal1, sal2 in zip(sal501_1000, hikesal501_1000):
        print("\t\t{} \t\t\t{}".format(sal1, sal2))
#Find the total salary of employees whose salary ranges from 0 to 500 before and after hike.
    totsal501_1000 = functools.reduce(lambda sal1, sal2: sal1 + sal2, sal501_1000)  # Before hike
    tothikesal501_1000 = functools.reduce(lambda sal1, sal2: sal1 + sal2, hikesal501_1000)  # After hike
    print("-----------------------------------------------------------------")
    print("\t\tTotal::{}\t\tTotal::{}".format(totsal501_1000, tothikesal501_1000))
    print("-----------------------------------------------------------------")
    print("*"*60)
    totoldsal=totsal0_500+totsal501_1000
    totnewsal=tothikesal0_500+tothikesal501_1000
    print("TOTAL OLD SAL={} \t\t\tTOTAL NEW SAL={}".format(totoldsal,totnewsal))
#Main program..
filtermapreduce() #Function call