# program for demonstrating how to use local and global varaibles
#LocalGlobalVarEx2.py
def learnAI():
    sub1="AI" #here sub1 is called local variable
    print("To develop '{}' based application,we use '{}' programming language".format(sub1,lang))
def learnML():
    sub2="ML" #here sub2 is called local variable
    print("To develop '{}' based application,we use '{}' programming language".format(sub2,lang))
lang = "Python"  # Here lang is called global variable
def learnDL():
    sub3="DL" #here sub3 is called local variable
    print("To develop '{}' based application,we use '{}' programming language".format(sub3,lang))
#main program ..
learnAI() #Function call
learnML()
learnDL()
#lang is defined here before function call so execution flow is like...3-line->6-line->9-line->10-line->then    14 ,15,16