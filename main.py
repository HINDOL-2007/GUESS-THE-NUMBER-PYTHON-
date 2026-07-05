import random 
a=random.randint(1,100)
c=10
for i in range(c):
    print("you have", c-i,"chance left")
    b=int(input("Guess a number between 1 to 100 :- "))
    if b>a:
        print("Your number is too high.")
    elif b<a:
        print('Your number is too low')
    elif b==a:
        print("You won the game.")
        break
if b!=a:    
    print("The number is :- ",a)    
    print("You loss") 
else:
    print("congratulations")
