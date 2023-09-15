from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, filename="test.log", filemode="w")
logger = logging.getLogger()

driver=webdriver.Firefox(service=FirefoxService("C:/Users/firedriver/geckodriver.exe"))
url=("https://atg.party/")
r=driver.get(url)
print(r)
time.sleep(0.2)
# Check HTTP response code
response_code = driver.execute_script("return document.readyState;")
response=logger.info("HTTP response code: {}".format(response_code == "complete"))
print("HTTP_response =",response_code)
#check time
response_time = driver.execute_script("return window.performance.timing.loadEventEnd - window.performance.timing.navigationStart;")
print("HTTP Response Code:", response_code)
print("Page Load Response Time:", response_time, "ms")

time.sleep(0.2)

# Click on LOGIN
#driver.find_element_by_link_text("Packard 255 G2").get_property('href')
login_button = driver.find_element(By.CSS_SELECTOR,"button[class='atg-secondarybtn-tiny outer-header__loginbtn loginbtn_new']")
login_button.click()
time.sleep(0.3)

# Fill in email/password and click Login
email_input = driver.find_element(By.ID,"email_landing")
email_input.send_keys("wiz_saurabh@rediffmail.com")
password_input = driver.find_element(By.ID,"password_landing")
password_input.send_keys("Pass@123")
login_submit_button = driver.find_element(By.XPATH,"//button[@class='landing-signin-btn']")
login_submit_button.click()

time.sleep(0.3)
driver.maximize_window()
# Go to the URL /article
article_url = "http://atg.party/article"
driver.get(article_url)
time.sleep(0.4) 

# Fill in title and description, upload cover image, and click POST
title_input = driver.find_element(By.CLASS_NAME, "title-textarea")
title_input.send_keys("Across The Globe with  my first automation")

#description_input = driver.find_element(By.TAG_NAME,'p')
#description_input.send_keys("this is automation description ATG is an interest based platform for like minded people to connect")

cover_image_input = driver.find_element(By.ID, "cover_image")
cover_image_input.send_keys("C:\\Users\\rinki\\OneDrive\\Desktop\\data_selenium\\image.jpg")  # Replace with the actual path to the cover image file
time.sleep(10)
post_button = driver.find_element(By.XPATH, "//button[@class='atg-primarybtn-tiny header__post-btn']")
post_button.click()
time.sleep(0.5)

# Log the URL of the new page
new_page_url = driver.current_url
print("New Page URL:", new_page_url)
#driver.close()
driver.minimize_window()
time.sleep(0.2)
# Close the browser
driver.quit() 
