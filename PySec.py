# Author: Rafael Rider / RiderSec



import random


lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()
digits = "123456789"
symbols = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
all = ""
upper, lower, nums, syms, = False, False, False, False
choice1 = None


print("Welcome to PySec!\n")


while choice1 != 0:
    print("Choose which characters PySec will use: ")
    print("1 - All")
    print("2 - Uppercase")
    print("3 - Lowercase")
    print("4 - Numbers")
    print("5 - Symbols")
    print("0 - Continue\n")

    choice1 = input("Input: ")

    try:
        choice1 = int(choice1)
    
        if 0 <= choice1 <= 5:
            match choice1:
                case 1:
                    upper, lower, nums, syms = True, True, True, True
                case 2:
                    upper = True
                case 3:
                    lower = True
                case 4:
                    nums = True
                case 5:
                    syms = True
                case 0:
                    print("Continuing...\n")
                    break
        
        else: 
            print("The input is not between 0 to 5, try again.")

    except ValueError:
        print("Invalid input, enter an integer.") 


if upper: 
    all += uppercase
if lower:
    all += lowercase
if nums:
    all += digits
if syms:
    all += symbols

length = input("How long should the passwords be?: ")

try: 
    length = int(length)

except ValueError:
    print("Invalid input, enter an integer.")

amount = input("How many passwords should the program generate?: ")

try: 
    amount = int(amount)

except ValueError:
    print("Invalid input, enter an integer.")


for x in range(amount):
    password = "".join(random.sample(all,length))
    print(password)
    
