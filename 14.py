# 1. input for 5 ages from the user.
# 2. print out the biggest age from the user.
# 3. write a function that gets the name as input from the user until the name 'Muhamad' and return a list of those names.

break_out_name = "Muhamad"


def get_names(name_to_break):
    list_of_names = []
    name = ""
    while name.lower() != name_to_break.lower():
        name = input("enter a name: ")
        list_of_names.append(name)
    return [item for item in list_of_names if item.lower() != break_out_name.lower()]


def get_max_age():
    ages = []
    maxAge = "0"
    for i in range(0, 5):
        age = input("enter the age: \n")
        ages.append(age)
        # Way 1
        if age > maxAge:
            maxAge = age
    # Way 1
    print(maxAge)
    # Way 2
    print(max(ages))


# get_max_age()

print(get_names("Muhamad"))
