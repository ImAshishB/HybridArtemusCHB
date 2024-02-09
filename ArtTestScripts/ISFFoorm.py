# In this Script, script will be record errors and will be continuing for next script.
import logging
import datetime
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
    ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites.utils import utills
import time
import string
import random


serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=serv_obj)
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         ElementClickInterceptedException,
                                                                         ElementNotInteractableException,
                                                                         Exception])

# URL
driver.get("http://52.54.244.138:8080/ArtemusChb/")

# Maximize page
driver.maximize_window()
file = "D:\Artmus Spec\Automation_Artemus\TestML.xlsx"
rows = utills.getRowCount(file, "Sheet1")
coloumns = utills.getColumnCount(file, "Sheet1")


def random_invoceGenerator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def random_BillGenerator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


# Login
login_username = mywait.until(EC.element_to_be_clickable((By.ID, "username")))
login_username.click()
login_username.send_keys("tnash")
login_password = mywait.until(EC.element_to_be_clickable((By.ID, "password")))
login_password.click()
login_password.send_keys("tnash1")
driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
print("Login Done")

# HomePage
time.sleep(4)
ISF = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "ISF")))
ISF.click()
time.sleep(2)

# Select Importer
selectImporterTxt = mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='typeahead-basic']")))
selectImporterTxt.click()
selectImporterTxt.send_keys("arttest")
time.sleep(3)
selectImporterTxt.send_keys(Keys.ENTER)
time.sleep(1)

FormISF = mywait.until(EC.element_to_be_clickable((By.XPATH, "//a[@id='ISFForm']")))
FormISF.click()
time.sleep(1)
print("ISF Form opened")
# ---------------------------------------------------------------------------------------------------------
