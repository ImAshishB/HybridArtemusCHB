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


logging.basicConfig(filename="Art_7501Log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
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
login_username.send_keys("abc")
login_password = mywait.until(EC.element_to_be_clickable((By.ID, "password")))
login_password.click()
login_password.send_keys("abc1")
driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
print("Login Done")
logging.info("Login Done")
time.sleep(4)
Shipment = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Shipments")))
Shipment.click()
time.sleep(2)

impTxt = mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='typeahead-basic']")))
impTxt.click()
impTxt.send_keys("Q IMPORTER")
time.sleep(2)
impTxt.send_keys(Keys.ENTER)



#Read data from excel
for r in range(4, 22):
    i = 0
    i = i - 1
    billCounts = utills.readData(file, "Sheet1", r, 2)
    lineitmscount = utills.readData(file, "Sheet1", r, 3)
    # intlineitmscount = int(lineitmscount)

    # #Login
    usern = utills.readData(file, "Sheet1", r, 5)
    pasw = utills.readData(file, "Sheet1", r, 6)
    #
    # #Form
    entfilltype = utills.readData(file, "Sheet1", r, 7)
    actionC = utills.readData(file, "Sheet1", r, 8)
    trnpmode = utills.readData(file, "Sheet1", r, 9)
    invoicenoEx = utills.readData(file, "Sheet1", r, 10)
    invoicenoData = "Q_" + random_invoceGenerator()

    scacData = utills.readData(file, "Sheet1", r, 11).split(",")
    # billofladdingNo = utills.readData(file, "Sheet1", r, 12).split(",")
    billofladdingNo = random_BillGenerator()
    uomData = utills.readData(file, "Sheet1", r, 13).split(",")
    qtyyData = utills.readData(file, "Sheet1", r, 14).split(",")

    # Passing the data in application
    # ----------------------------------
    # HomePage
    Form7501 = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Form 7501")))
    Form7501.click()
    time.sleep(1)
    print("7501 Form opened")
    logging.info("7501 Form opened")
    #---------------------------------------------------------------------------------------------------------

    # Upper Section
    try:
        ivcnumbertxt= driver.find_element(By.CSS_SELECTOR, "input#invoiceNumber")
        ivcnumbertxt.send_keys(invoicenoData)
        time.sleep(1)
        outclick = driver.find_element(By.XPATH, "//span[normalize-space()='Invoice Number:']")
        outclick.click()
        time.sleep(2)
    except Exception as e:
        print(e)
        logging.error(e)


    # Bill Of lading
    # Vessel Inforrmation
    # Trading Partners
    # Line Items

    try:
        saveButton = mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))
        saveButton.click()
        time.sleep(2)

        msg = driver.find_element(By.TAG_NAME, "body").text

        if 'Form saved succesfully!' in msg:
            formSavedConfirmationMsgButton = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
            formSavedConfirmationMsgButton.click()
            time.sleep(2)
            print("Form Saved Successfully")
            logging.info("----Form Saved Successfully----")
            # logoutButton = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
            # logoutButton.click()
        else:
            driver.save_screenshot(".\\screenshots\\" + "testing_scr.png")  # Screenshot
            logging.info("----Form not Saved----")
            # logoutButton = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
            # logoutButton.click()

    except:
        pass
    All = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "All")))
    All.click()
    time.sleep(1)
logoutButton = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
logoutButton.click()
time.sleep(1)
