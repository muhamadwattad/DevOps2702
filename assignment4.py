# 1

import requests
import json
from time import  sleep
from selenium import webdriver

response = requests.get("https://api.github.com/users/avielb/repos")

if response.status_code != 200:
    print("Failed to get data from API")

responseText = response.text

data = json.loads(responseText)
print(len(data))

if len(data) >= 5:
    print(f"True, There is {len(data)} Repos")
else:
    print(f"False, There is {len(data)} Repos")

# 2


for i in range(0, 0):
    name = input("Enter name: ")
    response = requests.get(f"https://api.agify.io/?name={name}")
    if response.status_code != 200:
        print("Failed to get age from API")
        continue
    data = json.loads(response.text)
    print(f"Name: {name}, Age: {data['age']}")


# UI Testing


def check_title_isEqualed(url, expected):
    driver = webdriver.Chrome(executable_path="C:/Users/Gaming/OneDrive/Desktop/chromedriver/chromedriver")
    driver.get(url)
    sleep(5)
    result = driver.find_element(by="xpath",value= "//title").get_attribute("textContent")
    print(f"Result Is: {result}")
    try:
        assert result == expected
        return True
    except Exception as ex:
        return False


print(check_title_isEqualed("https://www.ycombinator.com/", "Y Combinator"))
print(check_title_isEqualed("https://hub.docker.com/", "Docker Hub Container Image Library | App Containerization"))
