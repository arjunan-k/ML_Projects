import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests

# ------------------------------------------- #
url = 'https://api.quotable.io/random'
r = requests.get(url)
quotes = r.json()
quote = f"{quotes['content']}\n- {quotes['author']}\n#quotes"
# print(quote)
# ------------------------------------------- #

URL = "https://www.linkedin.com/"

USERNAME = ""
PASSWORD = ""

chrome_path = r'chromedriver.exe'
driver = webdriver.Chrome(executable_path=chrome_path)
driver.get(url=URL)
sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()
email = driver.find_element_by_id("username")
email.send_keys(USERNAME)
password = driver.find_element_by_id("password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)
Start_a_post = driver.find_element_by_xpath("/html/body/div[5]/div[3]/div/div/div[2]/div/div/main/div[1]/div/div[1]/button")
Start_a_post.click()
time.sleep(2)
message = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]")
message.click()
message.send_keys(quote)
post = driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div/div/div[2]/div[2]/div[3]/button")
time.sleep(2)
post.send_keys(Keys.ENTER)
driver.close()
