# A

x = 4
y = 5

if x > y:
    print("BIG")
elif x < y:
    print("SMALL")
else:
    print("EQUALED")

# B

for i in range(0, 5):
    print(i)

# C

c = 2

if c == 1:
    print("summer")
elif c == 2:
    print("winter")
elif c == 3:
    print("fall")
elif c == 4:
    print("sprint")
else:
    print("Wrong Input")

# D
# The loop will run 10 times, and it will stop when count reaches 11
# 10 will be printed last

# E

age = 23
first_letter = "M"
shekel = 3.60
flew_abroad = True
apartment_number = 0

print(
    f"Age: {age}, firstLetter: {first_letter}, Shekel: {shekel}, FlewAbroad: {flew_abroad}, ApartmentNumber: {apartment_number}")

print(shekel + age)  # 26.6

# F

phoneNumber = input("Enter your PhoneNumber: ")
print(f"phone number: {phoneNumber}")


# G

def printHello():
    print("hello")


def calculate():
    print(5 + 3.2)


printHello()
calculate()


# H

def print_name(name):
    print(name)


def devide_by_two(number):
    print(number / 2)


print_name("Muhamad Wattad")
devide_by_two(10)


# I

def print_sum(number1, number2):
    return number1 + number2


def add_underscore(string1, string2):
    return str(string1) + "_" + str(string2)


print(print_sum(10, 15))

print(add_underscore("asd", 20))

# K


for i in range(1, 6):
    for z in range(0, i):
        print("*", end="")
    print()
print()

# L

for i in range(7):
    for j in range(7):
        if i == j or i == (7 - 1 - j):
            print('X', end='')
        else:
            print(' ', end='')
    print()

# M

n = int(input("enter a number: "))

tempNumber = n

sumOfDigits = 0
while tempNumber > 0:
    carry = tempNumber % 10
    tempNumber = int(tempNumber / 10)
    sumOfDigits += carry

print(f"Sum Of Digits {n} is : {sumOfDigits}")
