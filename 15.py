import datetime

from time import sleep

import requests



# print(datetime.datetime.now())
# sleep(3)
# print(datetime.datetime.now())


def check_if_url_up(url: str):
    response = requests.get(url)
    return response.status_code, response.status_code == 200


print(check_if_url_up("https://api.github.com"))
