import random
numofguess=0

print("heyy, what is your name ")
name=input()

number=random.randint(1,20)
print("Number i am thinking of is between 1 to 20 ",name)

while numofguess<6:
    print("take a guess. ")
    guess=int(input())


    numofguess=numofguess + 1
    if guess < number :
        print("number is too low ")
    if guess > number :
        print("number is too high ")
    if guess == number :
        break
if guess == number:
    numofguess=str(numofguess)
    print("well done ",name,"you guessed the number in:",numofguess)
if guess != number:
    number = str(number)
    print("wrong! unlucky, the number was :",number)
    
    
