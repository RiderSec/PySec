import random


lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = lowercase.upper()
digits = "123456789"
symbols = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
all = ""



upper, lower, nums, syms, = True, True, True, True

# ^^ Change any of these values to false to change the character set of your passwords. ^^



if upper: 
    all += uppercase
if lower:
    all += lowercase
if nums:
    all += digits
if syms:
    all += symbols


length = 20
amount = 10

# ^^ Change these to change the length and amount, as needed. ^^


for x in range(amount):
    password = "".join(random.sample(all,length))
    print(password)
    

