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
mywait = WebDriverWait(driver, 30, poll_frequency=2, ignored_exceptions= [NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         ElementClickInterceptedException,
                                                                         ElementNotInteractableException,
                                                                         Exception])

# URL
driver.get("http://3.1.42.248/#/login")


# Maximize page
driver.maximize_window()
time.sleep(3)

login_username = mywait.until(EC.element_to_be_clickable((By.ID, "username")))
login_username.click()
login_username.send_keys("ruchi.dwivedi@giantleapsystems.com")
login_password = mywait.until(EC.element_to_be_clickable((By.ID, "password")))
login_password.click()
login_password.send_keys("123456")
driver.find_element(By.XPATH, "//button[@id='loginBtn']").click()
print("Login Done")
time.sleep(20)


cl1 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Reports']")))
cl1.click()
time.sleep(2)
print("Clicked on Reports")
cl2 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Account Reports']")))
cl2.click()
time.sleep(2)
print("Clicked on Account Reports")
cl3 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Employee Salary Report']")))
cl3.click()
time.sleep(2)
print("Clicked on Employee Salary Report")


Mcl4 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mat-select-value ng-tns-c95-1']")))
Mcl4.click()
time.sleep(2)
print("Opened DRP")

McOptl4 = mywait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Select All']")))
McOptl4.click()
time.sleep(2)
print("Clicked On  DRP all")

driver.find_element(By.XPATH, "//div[@id='mat-select-0-panel']").send_keys(Keys.ENTER)
time.sleep(2)

# overlay_locator = (By.CSS_SELECTOR, ".cdk-overlay-backdrop")
# mywait.until(EC.invisibility_of_element_located(overlay_locator))
# time.sleep(2)
# bodyPart = mywait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='cdk-overlay-backdrop cdk-overlay-transparent-backdrop cdk-overlay-backdrop-showing']")))
# bodyPart.send_keys(Keys.ENTER)
# time.sleep(2)


viewReport = mywait.until(EC.element_to_be_clickable((By.XPATH, "button.btn.btn-sm.btn-block.btn-outline-theme")))
# viewReport.send_keys(Keys.ENTER)
# time.sleep(2)
# print("Clicked On  viewReport")

viewReport.click()
time.sleep(2)
print("Clicked On  viewReport")
