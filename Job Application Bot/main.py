from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
chrome_path = Service(r"C:\Users\user\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_path)

# ------------------------------Set URL by setting your job serach in linkedin without login-------- #

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3078694126&f_AL" \
      "=true&f_WT=2&geoId=92000000&keywords=marketing%20specialist&location=Worldwide&refresh=true"
PHONE = "Type your phone Number"

# ------------------------------Opening the LinkedIn Website---------------------------------------- #

driver.get(url=URL)
time.sleep(3)         # wait for 3 seconds

# ------------------------------Clicking on signin button------------------------------------------- #

sign_in = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
sign_in.click()
time.sleep(2)

# ------------------------------Filling the login details------------------------------------------- #

email = driver.find_element(By.XPATH, '//*[@id="username"]')
email.send_keys("Type your email")
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("Type your password")
sign = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign.click()
time.sleep(5)

# ------------------------------Finding all job post available------------------------------------------- #

all_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)

# ------------------------------Starts to Apply for job------------------------------------------- #

    # Try to locate the apply button, If it can't locate then skip the job.
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()
        time.sleep(5)

        # If phone field is empty, then fill your phone number.
        phone = driver.find_element(By.CLASS_NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")

        # If the submit_button is a "Next" button, then this is a multiple step application, so skip.
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)
            discard_button = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        # Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
        close_button.click()

    # If already applied to job or job is no longer accepting applications, then skip.
    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)    # wait for 5 seconds.
driver.quit()    # closes the program