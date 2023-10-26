# import logging
# import datetime
# from selenium import webdriver
# from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
#     ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from utilites.utils import utills
# import time
# import string
# import random
#
# # # Configure logger
# # logging.basicConfig(filename='Artemus.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# #
# # # Create a timestamp for the log file name
# # timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
# #
# # # Create the log file name with the timestamp
# # log_file = f"Artemus_{timestamp}.log"
# #
# # # Configure logger
# # logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#
# logging.basicConfig(filename="Art_Query_Log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.info('------------------------------------------------------------New Log Started From Here-----------------------------------------------------------------------')
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
#
# # URL
# driver.get("http://52.54.244.138:8080/ArtemusChb/")
#
# # Maximize page
# driver.maximize_window()
#
# #Login
# driver.find_element(By.ID, "username").send_keys("tnash")
# driver.find_element(By.ID, "password").send_keys("tnash1")
# driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
# time.sleep(5)
#
# #HomePage
# query = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Queries")))
# query.click()
# misc = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,"Miscellaneous")))
# misc.click()
# tariffquery = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Tariff Query']")))
# tariffquery.click()
#
# file = "D:\Artmus Spec\Automation_Artemus\querylist.xlsx"
# rows = utills.getRowCount(file, "Sheet1")
# coloumns = utills.getColumnCount(file, "Sheet1")
#
# #Read data from excel
# for r in range(2, 3):
#     htsno = utills.readData(file, "Sheet1", r, 1).split(",")
#
#     for val1 in zip(htsno):
#         htsInput=driver.find_element(By.ID, "HTSUSNo")
#         htsInput.clear()
#         driver.find_element(By.XPATH,"//span[normalize-space()='HTSUS:']").click()
#         htsInput.send_keys(val1)
#         time.sleep(2)
#
#         try:
#             typhade = driver.find_element(By.XPATH, "//ngb-typeahead-window[@id='ngb-typeahead-0']")
#             if typhade:
#                 time.sleep(1)
#                 htsInput.send_keys(Keys.ENTER)
#         except:
#             print("New HTS found",val1)
#             logging.info("New HTS found %s",(val1))
#
#
#
#         driver.find_element(By.XPATH, "//input[@name='fromDate']").clear()
#         driver.find_element(By.XPATH, "//input[@name='fromDate']").send_keys("2023/08/31")
#         submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="formDiv"]/form/div[3]/div[2]/button')))
#         submit.click()
#         time.sleep(5)
#
#
#         try:
#             notonfile = WebDriverWait(driver, 10).until(
#                 EC.visibility_of_element_located((By.XPATH, "//span[text()='Record Begin Effective Date:']"))).text
#
#             # notonfile=driver.find_element(By.XPATH,"//span[text()='Record Begin Effective Date:']").text
#             print(notonfile)
#             if notonfile:
#                 print("This HTS is queried", val1)
#                 time.sleep(1)
#
#                 # logging.error("This HTS is not on file")
#         except Exception as e:
#             print("This HTS is not on file", val1)
#             logging.error("This HTS is not on file")



#115 to 193 list hai ye start

# import logging
# import datetime
# from selenium import webdriver
# from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
#     ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from utilites.utils import utills
# import time
#
# logging.basicConfig(filename="Art_Query_Log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.info('------------------------------------------------------------New Log Started From Here-----------------------------------------------------------------------')
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
# # URL
# driver.get("http://52.54.244.138:8080/ArtemusChb/")
# # Maximize page
# driver.maximize_window()
#
# #Login
# driver.find_element(By.ID, "username").send_keys("tnash")
# driver.find_element(By.ID, "password").send_keys("tnash1")
# driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
#
# #HomePage
# query = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Queries")))
# query.click()
# misc = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,"Miscellaneous")))
# misc.click()
# tariffquery = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Tariff Query']")))
# tariffquery.click()
# logging.info("Query Section Opened")
# file="D:\Artmus Spec\Automation_Artemus\querylist.xlsx"
# rows=utills.getRowCount(file,"Sheet1")
# #for r in range(2,rows+1):
# for r in range(2,3):
#     htsno=utills.readData(file,"Sheet1",r,1).split(",")
#     for val1 in zip(htsno):
#         htsInput=driver.find_element(By.ID, "HTSUSNo")
#         htsInput.clear()
#         driver.find_element(By.XPATH,"//span[normalize-space()='HTSUS:']").click()
#         htsInput.send_keys(val1)
#         try:
#             time.sleep(2)
#             typhade = driver.find_element(By.XPATH, "//ngb-typeahead-window[@id='ngb-typeahead-0']")
#             if typhade:
#                 htsInput.send_keys(Keys.ENTER)
#         except:
#             print("New HTS found",val1)
#             logging.info("New HTS found %s",(val1))
#
#         driver.find_element(By.XPATH, "//input[@name='fromDate']").clear()
#         driver.find_element(By.XPATH, "//input[@name='fromDate']").send_keys("2023/10/17")
#         submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="formDiv"]/form/div[3]/div[2]/button')))
#         submit.click()
#         time.sleep(5)
#
#         try:
#             notonfile=driver.find_element(By.XPATH,"//span[text()='Narrative Message:']//parent::div//following-sibling::div[normalize-space()='NOT ON FILE OR EXPIRED']")
#             if notonfile:
#                 print("This HTS is not on file", val1)
#                 logging.error("This HTS is not on file %s",(val1))
#         except:
#             print("This HTS is queried", val1)
#             time.sleep(1)

#115 to 193 list hai ye end








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

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=serv_obj)
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions= [NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         ElementClickInterceptedException,
                                                                         ElementNotInteractableException,
                                                                         Exception])

# URL
driver.get("http://52.54.244.138:8080/ArtemusChb/")
# Maximize page
driver.maximize_window()

#Login
driver.find_element(By.ID, "username").send_keys("tnash")
driver.find_element(By.ID, "password").send_keys("tnash1")
driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()

#HomePage
query = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Queries")))
query.click()
misc = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,"Miscellaneous")))
misc.click()
tariffquery = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Tariff Query']")))
tariffquery.click()
file="D:\Artmus Spec\Automation_Artemus\querylist.xlsx"
rows=utills.getRowCount(file,"Sheet1")


for r in range(2,3):
    htsno=utills.readData(file,"Sheet1",r,1).split(",")

    for val1 in zip(htsno):

        # clear input
        htsInput=driver.find_element(By.ID, "HTSUSNo")
        htsInput.clear()

        # Click on outline of input
        htsOutClick = driver.find_element(By.XPATH,"//span[normalize-space()='HTSUS:']")
        htsOutClick.click()

        # Send value
        htsInput.send_keys(val1)

        # try if typehade is available
        try:
            time.sleep(2)
            typhade = driver.find_element(By.XPATH, "//ngb-typeahead-window[@id='ngb-typeahead-0']")
            if typhade:
                htsInput.send_keys(Keys.ENTER)
        except:
            print("New HTS found",val1)

        # Add Date
        driver.find_element(By.XPATH, "//input[@name='fromDate']").clear()
        driver.find_element(By.XPATH, "//input[@name='fromDate']").send_keys("2023/10/17")

        # Submit
        submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="formDiv"]/form/div[3]/div[2]/button')))
        submit.click()
        time.sleep(5)


