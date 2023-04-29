from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path="C:/Users/Gaming/OneDrive/Desktop/chromedriver/chromedriver")

driver.get("http://127.0.0.1:5500/index.html")

bill_amount = driver.find_element(by="id", value="billamt")
bill_amount.send_keys("100")
s = driver.find_element(by="xpath", value="//*[@id=\"serviceQual\"]/option[5]")
s.click()

people_amount = driver.find_element(by="xpath", value="//*[@id=\"peopleamt\"]")
people_amount.send_keys("5")

driver.find_element(by="xpath", value="//*[@id=\"calculate\"]").click()

expected = "1.00"
actual = driver.find_element(by="xpath", value="//*[@id=\"tip\"]").text

try:
    assert expected == actual
except Exception as ex:
    print(ex.args)

sleep(5)
driver.close()
