# ------------------------------------Process Started------------------------------------- #

# Including the packages of selenium.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time


class GoogleForms:      # Creating a class.

    # Creating a method with 3 answer parameters.

    @staticmethod
    def fill_form(a1, a2, a3):

        google_forms = "Use the google form link you created."
        chrome_path = Service(r"C:\Users\user\chromedriver_win32\chromedriver.exe")
        driver = webdriver.Chrome(service=chrome_path)
        driver.get(url=google_forms)
        time.sleep(5)

        # Filling question 1 using selenium.

        q1 = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]')
        q1.click()
        time.sleep(2)
        q1updated = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div'
                                                  '/div[2]/div/div[1]/div/div[1]/input')
        q1updated.send_keys(a1)

        # Filling question 2 using selenium.

        q2 = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]')
        q2.click()
        time.sleep(2)
        q2updated = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]'
                                                  '/div/div[1]/div/div[1]/input')
        q2updated.send_keys(a2)

        # Filling question 3 using selenium.

        q3 = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]')
        q3.click()
        time.sleep(2)
        q3updated = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div'
                                                  '[2]/div/div[1]/div/div[1]/input')
        q3updated.send_keys(a3)

        # Clicking the submit button after filling.

        submit = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]'
                                               '/div[1]/div[1]/div/span/span')

        submit.click()
        time.sleep(5)
        driver.quit()

# ------------------------------------Process Finished------------------------------------ #