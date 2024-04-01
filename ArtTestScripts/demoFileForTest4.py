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
import string
import random

# # Configure logger
# logging.basicConfig(filename='Artemus.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
# # Create a timestamp for the log file name
# timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
#
# # Create the log file name with the timestamp
# log_file = f"Artemus_{timestamp}.log"
#
# # Configure logger
# logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

logging.basicConfig(filename="Art_7501_MEntry", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')
logging.info('------------------------------------------------------------New Log Started From Here-----------------------------------------------------------------------')
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


file = "D:\Artmus Spec\Automation_Artemus\TestML.xlsx"
rows = utills.getRowCount(file, "Sheet1")
coloumns = utills.getColumnCount(file, "Sheet1")
driver.maximize_window()
for r in range(3, 7):
    i = 0
    i = i - 1
    driver.get("http://52.54.244.138:8080/ArtemusChb/")


    billCounts = utills.readData(file, "Sheet1", r, 2)
    lineitmscount = utills.readData(file, "Sheet1", r, 3)
    testCasesNumber = utills.readData(file, "Sheet1", r, 10)

    # #Login
    usern = utills.readData(file, "Sheet1", r, 5)
    pasw = utills.readData(file, "Sheet1", r, 6)

    # Login
    login_username = mywait.until(EC.element_to_be_clickable((By.ID, "username")))
    login_username.click()
    login_username.send_keys("tnash")
    login_password = mywait.until(EC.element_to_be_clickable((By.ID, "password")))
    login_password.click()
    login_password.send_keys("tnash1")
    driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
    print("Login Done")
    logging.info("Login Done")
    SHORT_TIMEOUT = 1  # give time for the loading element to appear
    LONG_TIMEOUT = 30  # give time for loading to finish
    LOADING_ELEMENT_XPATH = "//body//app-root//app-loader//h3[@class='loadingScreen__text']"
    try:
        WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
    except TimeoutException:
        pass

    driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
    print("LogOut Done")
    logging.info("LogOut Done")
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + 'w')


    driver.get("http://3.1.42.248/#/login")
    time.sleep(4)
    print("ediary link opened")

print("Done")
time.sleep(6)
driver.close()
