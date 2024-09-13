# In this Script, script will be record errors and will be continuing for next script.
import logging
import datetime
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
    ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites.utils import utills
import time
serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=serv_obj)
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions= [NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         ElementClickInterceptedException,
                                                                         ElementNotInteractableException,
                                                                          TimeoutException,

                                                                         Exception])

# URL
driver.get("http://52.54.244.138:8080/ArtemusChb/")

# Maximize page
driver.maximize_window()

# Login
login_username = mywait.until(EC.element_to_be_clickable((By.ID, "username")))
login_username.click()
login_username.send_keys("tnash")
login_password = mywait.until(EC.element_to_be_clickable((By.ID, "password")))
login_password.click()
login_password.send_keys("tnash1")
driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
print("Login Done")
SHORT_TIMEOUT = 1  # give time for the loading element to appear
LONG_TIMEOUT = 30  # give time for loading to finish
LOADING_ELEMENT_XPATH = "//body//app-root//app-loader//h3[@class='loadingScreen__text']"
try:
    WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
except TimeoutException:
    pass
Shipment = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Shipments")))
Shipment.click()
time.sleep(2)

# Select Importer
selectImporterTxt = mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='typeahead-basic']")))
selectImporterTxt.click()
selectImporterTxt.send_keys("arttest")
time.sleep(1)
selectImporterTxt.send_keys(Keys.BACKSPACE)
time.sleep(2)
selectImporterTxt.send_keys(Keys.ENTER)
time.sleep(1)

# Open the saved form
driver.find_element(By.XPATH, "(//i[@aria-hidden='true'])[1]").click()
time.sleep(2)

# Copy the saved form
driver.find_element(By.XPATH, "//i[@class='fa fa-copy 2px']").click()
time.sleep(2)
