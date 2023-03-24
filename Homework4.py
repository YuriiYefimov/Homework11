from random import randint
num = randint(1,10)
print("Welcome! Please try to guess a number from 1 to 10")
innum=input("Please, enter a number from 1 to 10:")
if str(innum).isdigit() and float(innum)>=0 and float(innum)<=10 and float.is_integer(float(innum)):
     if float(innum)==num:
       print("You win!")
     else:
       print("You were close to victory.Try again!")
else:
   print("Incorrect input")

