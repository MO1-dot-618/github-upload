"""
zCasino game
by Malika Oubilla

User chooses a number between 0 and 49 and deposits a sum $
if the roulette lands on the same number, user wins x4
if the roulette lands on a number with the same parity, user wins 1.5 $
otherwise, user loses.
"""
print("+----------------------------------------------------------------------+")
print()
print("                              Welcome to zCasino                        ")
print()
print("+----------------------------------------------------------------------+")
print(" User is given a sum of $100")
print(" User chooses a number between 0 and 49 and deposits an amount $")
print("if the roulette lands on the same number, user wins x4")
print("if the roulette lands on a number with the same parity, user wins x1.5 $")
print("otherwise, user loses.")
print()
print("+----------------------------------------------------------------------+")


#variables
balance=100
playagain="yes"

from random import randint
from time import sleep


#A class for custom exceptions handeling
class RefusedValue(Exception):
    """Raised when the value isn't addmited"""
    pass

def get_amount(balance):
    print("+-----------------------+")
    print(" Balance : $", balance)
    while True:
        try:
            amount=int(input("How much do you want to bet? "))
            if amount > balance or amount <= 0:
                raise RefusedValue
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        except RefusedValue:
            print("Oops!  Check your balance and try again...")
    return amount

def get_bet():        
    while True:
        try:
            bet=int(input("What's your bet? (choose a number between 0 and 49)  "))
            if bet > 49 or bet < 0:
                raise RefusedValue
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...")
        except RefusedValue:
            print("You can only choose a number between 0 and 49. Try again...")
    return bet


def turn_wheel():
    ball=randint(0,50)
    print("+-----------------------+")
    print("The wheel is turning...")
    sleep(1) #suspend execution for 2s
    print("      ...")
    sleep(1) 
    print("+-----------------------+")
    print("The number is ...")
    print()
    sleep(1)
    print("     ", ball)
    print()
    print("+-----------------------+")
    return ball


def playZ(balance):
    amount=get_amount(balance)
    print("+-----------------------+")
    print(" Bet amount : $", amount)
    bet=get_bet()
    ball=turn_wheel()

    factor=0.0
    if ball==bet: factor=4.0
    elif ball %2 == bet %2 : factor=1.5
    else: factor=0.0

    balance= balance - amount + amount*factor
    print("You won $", amount*factor, " !!!")
    print("Your new balance is : $", balance)
    return int(balance)

while playagain in ("yes", "YES") and balance >0:
    balance=playZ(balance)
    playagain= input("Do you want to play again? Type yes or no  :  ")

if balance == 0 :
    print("+----------------------------+")            
    print("Opps! You lost all your money!")
    print("+----------------------------+")
    
else:
    print("You started with $100 and now you have $", balance)
    if balance<100:
        print("you lost $", 100 - balance)
    else: print("you won $", balance - 100)

print("+--------------------------------------------------+")
print()
print("+------             End of Game              ------+")
print()
print("+--------------------------------------------------+")  





