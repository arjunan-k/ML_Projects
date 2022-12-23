from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# ------------------Internet speed check URL------------------- #

SPEED_URL = "https://www.speedtest.net/"
PROMISED_DOWNLOAD = 1000
PROMISED_UPLOAD = 500

# ------------------Twitter URL-------------------------------- #

TWITTER_URL = "https://twitter.com/home"
USERNAME = "Type your email/username"
PASSWORD = "Type your password"

# ------------------Opening internet speed check website------- #

chrome_path = Service(r"C:\Users\user\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_path)
driver.get(url=SPEED_URL)

# ------------------Clicking the go button--------------------- #

time.sleep(3)
# If you want to scroll down. 540 is half of vertical screen 1080.
driver.execute_script(script="window.scrollTo(0, 540)")
time.sleep(2)
go = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
go.click()
time.sleep(60)

# ------------------Saving the data from site------------------ #

download = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/'
                                         'div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
print(download)

upload = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]'
                                       '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
print(upload)

service_provider = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]'
                                                 '/div/div[3]/div/div/div[2]/div[4]/div/div'
                                                 '/div[1]/div[2]/div[2]/a').text
print(service_provider)

# ------------------Setting the tweet condition---------------- #

if float(download) < PROMISED_DOWNLOAD and float(upload) < PROMISED_UPLOAD:

    # ------------------Opening Twitter------------------ #

    driver.get(url=TWITTER_URL)
    time.sleep(7)

    # ------------------Filling the twitter sign in------ #

    username = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/'
                                             'div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]')
    username.click()
    time.sleep(5)
    username1 = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]'
                                              '/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
    username1.send_keys(USERNAME)
    next1 = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/'
                                          'div[2]/div[2]/div/div/div/div[6]/div')
    next1.click()
    time.sleep(3)
    password = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/d'
                                             'iv/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
    password.send_keys(PASSWORD)
    log_in = driver.find_element(By.XPATH, '/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/'
                                           'div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
    log_in.click()

    # ------------------Tweeting and submitting---------- #

    time.sleep(7)
    tweet = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]'
                                          '/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div/'
                                          'label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
    tweet.click()
    time.sleep(2)
    tweet.send_keys(f"Hey {service_provider}, why is my internet speed is {download}down/{upload}up, if I am paying for"
                    f" {PROMISED_DOWNLOAD}down/{PROMISED_UPLOAD}up. Please fix it.")
    button = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/'
                                           'div[2]/div[1]/div/div/div/div[2]/div[3]/'
                                           'div/div/div[2]/div[3]/div/span/span')
    button.click()

time.sleep(10)
driver.quit()
# ------------------Process finished--------------------------- #
