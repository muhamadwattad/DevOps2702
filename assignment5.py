# 1
import psutil
import shutil

file_path = "C:/Users/Gaming/OneDrive/Desktop/myname.txt"


def write_name():
    name = "Muhamad Wattad"
    with open(file_path, "w") as f:
        print("Writing name into file")
        f.write(name)


def read_name():
    with open(file_path, "r") as f:
        print(f.readline())


def move_file():
    destination_path = "C:/Users/Gaming/Documents/"
    shutil.move(file_path, destination_path)
    print(f"New Path File: {destination_path}")


def free_space():
    disk_usage = psutil.disk_usage('/')
    empty_space = round(disk_usage.free / (1024 ** 3), 2)
    print(f"Empty Space is: {empty_space}")


write_name()
read_name()
free_space()
move_file()
