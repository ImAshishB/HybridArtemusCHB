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
from selenium.webdriver.firefox.options import Options
import string
from selenium.webdriver import FirefoxOptions
from selenium.webdriver import Firefox
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

# serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options, service=serv_obj)
# mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions= [NoSuchElementException,
#                                                                          ElementNotVisibleException,
#                                                                          ElementNotSelectableException,
#                                                                          ElementClickInterceptedException,
#                                                                          ElementNotInteractableException,
#                                                                          Exception])
#

firefox_options = Options()
firefox_options.log.level = "trace"  # Set log level to trace
driver = webdriver.Firefox(options=firefox_options)

#options = FirefoxOptions()
#options.add_experimental_option("detach", True)

#driver = Firefox(options=options)

#driver = webdriver.Firefox(Service='C:\Drivers\geckodriver-v0.33.0-win-aarch64\geckodriver.exe')
# URL
driver.get("http://52.54.244.138:8080/ArtemusChb/")
#driver.get("http://www.google.com")
# driver.refresh()
# titl=driver.title
# print(titl)
i=0
i=i+1
try:
    while True:
        time.sleep(20)
        titl = driver.title
        print(titl)

        driver.refresh()
        print(i)


except KeyboardInterrupt:
    pass

finally:
    driver.quit()