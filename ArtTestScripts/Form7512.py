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
Form7512 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Form 7512')]")))
Form7512.click()
time.sleep(2)

# Select Importer
selectImporterTxt = mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='typeahead-basic']")))
selectImporterTxt.click()
selectImporterTxt.send_keys("ARTTEST")
time.sleep(3)
selectImporterTxt.send_keys(Keys.ENTER)
time.sleep(1)

OpenForm7512 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//div[normalize-space()='Form 7512']")))
OpenForm7512.click()
time.sleep(1)
print("7512 Form opened")
# ---------------------------------------------------------------------------------------------------------

driver.find_element(By.XPATH, "//input[@id='importCarrierIRS']").send_keys("58-123456009")

scac = mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='scac']")))
scac.click()
scac.send_keys("MFUS")
time.sleep(2)
scac.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, "//a[normalize-space()='Get Next']").click()
time.sleep(2)

PortofArrival = mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='portOfArrival']")))
PortofArrival.click()
PortofArrival.send_keys("NORFOLK, VA")
time.sleep(2)
PortofArrival.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, "//input[@id='value']").send_keys('464')


mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='billOfLading']"))).send_keys("MFUS4333")


PortofLading = mywait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='card-body']//input[@id='typeahead-basic']")))
PortofLading.click()
PortofLading.send_keys("NORFOLK")
time.sleep(2)
PortofLading.send_keys(Keys.ENTER)

driver.find_element(By.XPATH, "(//button[@type='submit'][normalize-space()='Save'])[1]").click()