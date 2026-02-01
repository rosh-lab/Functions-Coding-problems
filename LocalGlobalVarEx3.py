# program for demonstrating how to use local and global varaibles
#LocalGlobalVarEx3.py
lang="Python" #Global varaible must be before function call whether it is before function definition or not.
def learnAI():
    sub1="AI" #here sub1 is called local variable
    print("To develop '{}' based application,we use '{}' programming language".format(sub1,lang))
#lang="Python"  #Excess in all function calls
def learnML():
    sub2="ML" #here sub2 is called local variable
    print("To develop '{}' based application,we use '{}' programming language".format(sub2,lang))
def learnDL():
    sub3="DL" #here sub3 is called local variable
    print("To develop '{}' based application,we use '{}' programming language".format(sub3,lang))
#main program ..
learnAI() #Function call
learnML()
learnDL()