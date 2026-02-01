# program for demonstrating how to use local and global varaibles
#LocalGlobalVarEx1.py
def learnAI():
    sub1="AI" #here sub1 is called local variable
    print("To develop '{}' based application,we use '{}' programming language".format(sub1,lang))
    # print(sub2,sub3) we cant excess sub2 and sub3 bcz they are local variables in other function
def learnML():
    sub2="ML" #here sub2 is called local variable
    print("To develop '{}' based application,we use '{}' programming language".format(sub2,lang))
    # print(sub1,sub3) we cant excess sub1 and sub3 bcz they are local variables in other function
def learnDL():
    sub3="DL" #here sub3 is called local variable
    print("To develop '{}' based application,we use '{}' programming language".format(sub3,lang))
    # print(sub1,sub2) we cant excess sub1 and sub2 bcz they are local variables in other function
#main program ..
lang="Python" #Here lang is called global variable
learnAI() #Function call
learnML()
learnDL()
#For different multiple function calls we need a common value and it is always written in global variable to reduce memory space..
