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

logging.basicConfig(filename="Art_7501_1Entry", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')
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
                                                                         Exception])

# URL
driver.get("http://52.54.244.138:8080/ArtemusChb/")


# Maximize page
driver.maximize_window()
# file = "D:\Artmus Spec\Automation_Artemus\TestML.xlsx"
# path = ".//testdata/TestML.xlsx"
path = "D:\Artmus Spec\Automation_Artemus\TestML.xlsx"

def random_invoceGenerator(size=5, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
def random_BillGenerator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
#Read data from excel
for r in range(3, 4):
    i = 0
    i = i - 1
    selectImporterData = utills.readData(path, "Sheet1", r, 140)
    # intlineitmscount = int(lineitmscount)

    # #Login
    usern = utills.readData(path, "Sheet1", r, 5)
    pasw = utills.readData(path, "Sheet1", r, 6)

    vesselsname = utills.readData(path, "Sheet1", r, 15)
    vessellsno = utills.readData(path, "Sheet1", r, 16)
    containerscount = utills.readData(path, "Sheet1", r, 4)
    containerlist = utills.readData(path, "Sheet1", r, 17).split(",")

    # Passing the data in application
    # ----------------------------------

    # Login
    login_username = mywait.until(EC.element_to_be_clickable((By.ID, "username")))
    login_username.click()
    login_username.send_keys(usern)
    login_password = mywait.until(EC.element_to_be_clickable((By.ID, "password")))
    login_password.click()
    login_password.send_keys(pasw)
    driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
    print("Login Done")
    logging.info("Login Done")

    # HomePage
    time.sleep(4)
    Shipment = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Shipments")))
    Shipment.click()
    time.sleep(2)

    # Select Importer
    selectImporterTxt = mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='typeahead-basic']")))
    selectImporterTxt.click()
    selectImporterTxt.send_keys(selectImporterData)
    time.sleep(2)
    selectImporterTxt.send_keys(Keys.ENTER)


    Form7501 = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Form 7501")))
    Form7501.click()
    time.sleep(1)
    print("7501 Form opened")
    logging.info("7501 Form opened")
    try:
        try:
            vesselNametxt = driver.find_element(By.CSS_SELECTOR, "input#vesselName")
            vesselNametxt.send_keys(vesselsname)
        except:
            pass

        vesselFlightNotxt = driver.find_element(By.CSS_SELECTOR, "input#vesselFlightNo")
        vesselFlightNotxt.send_keys(vessellsno)

        try:
            Continer = driver.find_elements(By.XPATH, "// a[contains(text(), 'Add/Edit container')]")
            if Continer:
                driver.find_element(By.XPATH, "// a[contains(text(), 'Add/Edit container')]").click()
                for cont in zip(containerlist):
                    driver.find_element(By.XPATH,
                                        "//app-vessel-container//div[@class='row new-form-row'][1]//div[@class='col-md-4 form-lable'][1]//input[@type='text']").send_keys(
                        cont)
                    time.sleep(1)
                    driver.find_element(By.XPATH,
                                        "//app-vessel-container//div[@class='row new-form-row'][4]//button[normalize-space()='Add new container']").click()
                    time.sleep(1)
                driver.find_element(By.XPATH, "//button[@type='button'][normalize-space()='Save']").click()
        except:
            print("No Container found")
            pass




        # Check if all data filled in Vessel information or not
        if vesselNametxt.get_attribute("value") and vesselFlightNotxt.get_attribute("value"):
            print("----Vessel Done----")
            logging.info("----Vessel Done----")
        else:
            print("!----Vessel Not Done----!")
            logging.error("!----Vessel Not Done----!")

    except Exception as e:
        pass

