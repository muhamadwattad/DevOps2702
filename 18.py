import requests
from requests.exceptions import MissingSchema as MissingText


def get_age():
    current_age = int(input("Get Age: "))
    if current_age < 0:
        raise BaseException("Age can not be negative", current_age)
    print(current_age)


# try:
#    get_age()
# except BaseException as e:
#   print(e.args)


try:
    x=4
    response = requests.get("asdasdsadasd")

except MissingText as ex:
    print("Caught In Exception")
