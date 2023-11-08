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
#Read data from excel
for r in range(10, 11):
    i = 0
    i = i - 1
    selectImporterData = utills.readData(file, "Sheet1", r, 140)
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
    invoicenoData = invoicenoEx + random_invoceGenerator()

    scacData = utills.readData(file, "Sheet1", r, 11).split(",")
    billofladdingNo = random_BillGenerator()
    uomData = utills.readData(file, "Sheet1", r, 13).split(",")
    qtyyData = utills.readData(file, "Sheet1", r, 14).split(",")

    scacData2 = "MFUS"
    scacData3 = "tk"
    billofladdingNo2 = random_BillGenerator()
    uomData2 = "PKG"
    qtyyData2 = "50"

    vesselsname = utills.readData(file, "Sheet1", r, 15)
    vessellsno = utills.readData(file, "Sheet1", r, 16)
    containerscount = utills.readData(file, "Sheet1", r, 4)
    containerlist = utills.readData(file, "Sheet1", r, 17).split(",")

    manufacturerdata = utills.readData(file, "Sheet1", r, 18)
    sellerdata = utills.readData(file, "Sheet1", r, 19)
    consigneedata = utills.readData(file, "Sheet1", r, 20)
    buyerdata = utills.readData(file, "Sheet1", r, 21)

    countryOfOrigindata1 = utills.readData(file, "Sheet1", r, 22)
    release_portdata = utills.readData(file, "Sheet1", r, 23)
    countryOfExportdata1 = utills.readData(file, "Sheet1", r, 24)
    ladingportdata = utills.readData(file, "Sheet1", r, 25)
    grossWeightdata = utills.readData(file, "Sheet1", r, 26)
    chargedata = utills.readData(file, "Sheet1", r, 27)
    unladingportdata = utills.readData(file, "Sheet1", r, 28)
    manifestDescriptiondata = utills.readData(file, "Sheet1", r, 29)
    arrivaldatedata = utills.readData(file, "Sheet1", r, 30)
    exportdatedata = utills.readData(file, "Sheet1", r, 31)
    currencyData = utills.readData(file, "Sheet1", r, 112)

    invoiceTotaldata = utills.readData(file, "Sheet1", r, 32)
    tariffnodata = utills.readData(file, "Sheet1", r, 33).split(",")
    htsqty1 = utills.readData(file, "Sheet1", r, 34)
    htsqty2 = utills.readData(file, "Sheet1", r, 35)
    addcaseNumberData = utills.readData(file, "Sheet1", r, 111)
    cvdcaseNumberData = utills.readData(file, "Sheet1", r, 110)
    linevaluedata = utills.readData(file, "Sheet1", r, 36).split(",")
    countryOfOrigindata2 = utills.readData(file, "Sheet1", r, 37).split(",")
    countryOfExportdata2 = utills.readData(file, "Sheet1", r, 38).split(",")
    # partsData = utills.readData(file, "Sheet1", r, 113).split(",")

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
    #---------------------------------------------------------------------------------------------------------

    # # Upper Section
    try:
        entryfillingtypecode = driver.find_element(By.ID, "entryFilingTypeCode")
        entryfillingtypecode.click()
        entryfillingtypecode.send_keys(entfilltype)
        entryfillingtypecode.send_keys(Keys.ENTER)

        actionCode = driver.find_element(By.ID, "actionCode")
        actionCode.click()
        actionCode.send_keys(actionC)
        actionCode.send_keys(Keys.ENTER)

        # if trnpmode != 11:
        #     modeOfTransport = driver.find_element(By.ID, "modeOfTransport")
        #     modeOfTransport.click()
        #     modeOfTransport.send_keys(trnpmode)
        #     modeOfTransport.send_keys(Keys.ENTER)
        #
        modeOfTransport = driver.find_element(By.ID, "modeOfTransport")
        modeOfTransport.click()
        modeOfTransport.send_keys(trnpmode)
        modeOfTransport.send_keys(Keys.ENTER)

        ivcnumbertxt= driver.find_element(By.CSS_SELECTOR, "input#invoiceNumber")
        ivcnumbertxt.send_keys(invoicenoData)
        time.sleep(1)
        outclick = driver.find_element(By.XPATH, "//span[normalize-space()='Invoice Number:']")
        outclick.click()
        time.sleep(2)

        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("Invoice Number Not Added")
            logging.info("Invoice Number Not Added")
        except NoAlertPresentException:
            pass

        # Check if all data filled in upper part or not
        if ivcnumbertxt.get_attribute("value"):
            print("----Upper Part Done----")
            logging.info("----Upper Part Done----")
        else:
            print("!----Upper Part Not Done----!")
            logging.error("!----Upper Part Not Done----!")

    except Exception as e:
        print(e)
        logging.error(e)


    # Vessel Inforrmation
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



# #Save the form
#     try:
    #     saveButton = mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))
    #     saveButton.click()
    #     time.sleep(2)
    #
    #     msg = driver.find_element(By.TAG_NAME, "body").text
    #
    #     if 'Form saved succesfully!' in msg:
    #         formSavedConfirmationMsgButton = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
    #         formSavedConfirmationMsgButton.click()
    #         time.sleep(2)
    #         print("Form Saved Successfully")
    #         logging.info("----Form Saved Successfully----")
    #         logoutButton = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
    #         logoutButton.click()
    #     else:
    #         driver.save_screenshot(".\\screenshots\\" + "testing_scr.png")  # Screenshot
    #         logging.info("----Form not Saved----")
    #         logoutButton = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
    #         logoutButton.click()
    # except:
    #     pass
