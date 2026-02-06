#Write a python program which will acept number of days and convert it into number of years and no.of months and left out days,by using anonymous function
convertdays=lambda days:(days//365,(days%365)//30,(days%365)%30)
#MAin program
days=int(input("Enter number of days: "))
years,months,remainingdays=convertdays(days)
print("Years: ",years)
print("Months: ",months)
print("Remaining days: ",remainingdays)