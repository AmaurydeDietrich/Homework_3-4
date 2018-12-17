import math

#Write a program that asks for your name and prints: “Hello <name>!”
def getname ():

    name = input ()
    print ("Hello " + name)


# Write a program that takes 2 numbers as input and prints the rounded up division result
def getroundedup ():
    firstnum = input ()
    secondnum = input ()
    sum = firstnum+secondnum
    print (sum+1)



# Write a program that takes the radius of circle as input and prints the surface of the circle
def circlearea ():
    radius = input ()
    area = (math.pi*radius)**2
    print (area)



# Write a program that behaves like a pocket calculator that can do: (+,-,*,/) of 2 numbers.
# The numbers and the operation is read from the user

def sum ():
    firstnum = input()
    secondnum = input()
    sum = firstnum + secondnum

def substraction ():
    firstnum = input()
    secondnum = input()
    substraction = firstnum - secondnum

def multiplication ():
    firstnum = input()
    secondnum = input()
    multiplication = firstnum * secondnum

def division ():
    firstnum = input()
    secondnum = input()
    division = firstnum / secondnum