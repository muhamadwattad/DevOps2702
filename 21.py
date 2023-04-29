import requests

response = requests.post("http://127.0.0.1:5001/whatismyname")


# asd asd asd asd as asd as da sad asd asd
actual = "saved new car"
expected = response.text
assert actual == expected
