fileName = "names.txt";


def add_name_to_names_file(name):
    with open(fileName, "a") as myfile:
        myfile.write(name + "\n")


def print_names_in_file():
    file = open(fileName);
    for line in file.readlines():
        print(line, end='')


add_name_to_names_file("Muhamad")
add_name_to_names_file("wattad")

print_names_in_file()
