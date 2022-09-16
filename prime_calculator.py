import math
import sys


### asks you to enter a number to be used for the equations ###
number = input("what is your number, nerd? ")
### i is the number used in a mod equation ###
i = 2
### getting the square to use in the equations###
squareroot = math.sqrt(float(number))
### simple code for special numbers that arent either prime nor composite like 1 or 0 ###
if float(number) == 2:
    print("prime.")
    sys.exit()
if float(number) == 1:
    print("niether.")
    sys.exit()
if float(number) == 0:
    print("you are a terrible human bieng and you deserve pain.")
    sys.exit()
### defining x to make a while loop (simple loop that causes a loop as long as something is true) can be substituted by other loops ###
x = 1
while x == 1:
### checking to see if there is a remainder of any division possibility that is less than the square root of a number and stating the number isnt prime if there is no remainder ###
    if float(number)%float(i) == 0:
        print("not prime")
        sys.exit()
### if there is a remainder the variable that the number is divided by is increased by 1 and the variable is checked to see if it has xeeded the square root of the number that was inputed ###
    else:
        i = i+1
    if float(i)>float(squareroot):
### if the number has exeeded the square root of the number than the loop is broken ###
        break
### if the loop is broken via the variable exeeding the square root of the number the number is labled as a prime ###
print("prime")
