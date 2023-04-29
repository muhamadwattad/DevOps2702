names = ["Muhamad", "Wattad", "Fore", "Alina", "Alex"]

print(list(range(20, 1, -5)))

# ForEach
# for name in names:
#    print(name, end=',\n')

for name in names:
    name = "xd"  # Name won't change

for name in names:
    print(name, end=',')

for i in range(len(names)):
    names[i] = "xd"  # name will change here

for i in range(len(names)):
    print(names[i])

a = 0
while a < len(names):
    print(names[a])
    a += 1

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 3:
        continue
    if number == 2:
        break
    print(number)
else:
    print("finished successfully")
