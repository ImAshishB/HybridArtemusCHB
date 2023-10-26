# # In this Script, script will be record errors and will be continuing for next script.
# import logging
# import datetime
# from selenium import webdriver
# from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
#     ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.relative_locator import locate_with
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
# logging.basicConfig(filename="Art_7501Log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
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
#
# # Maximize page
# driver.maximize_window()
# file = "D:\Artmus Spec\Automation_Artemus\TestML.xlsx"
# rows = utills.getRowCount(file, "Sheet1")
# coloumns = utills.getColumnCount(file, "Sheet1")
#
# def random_invoceGenerator(size=5, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))
# def random_BillGenerator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))
# #Read data from excel
# for r in range(15, 16):
#     i = 0
#     i = i - 1
#     billCounts = utills.readData(file, "Sheet1", r, 2)
#     lineitmscount = utills.readData(file, "Sheet1", r, 3)
#     # intlineitmscount = int(lineitmscount)
#
#     # #Login
#     usern = utills.readData(file, "Sheet1", r, 5)
#     pasw = utills.readData(file, "Sheet1", r, 6)
#     #
#     # #Form
#     entfilltype = utills.readData(file, "Sheet1", r, 7)
#     actionC = utills.readData(file, "Sheet1", r, 8)
#     trnpmode = utills.readData(file, "Sheet1", r, 9)
#     invoicenoEx = utills.readData(file, "Sheet1", r, 10)
#     invoicenoData = invoicenoEx + random_invoceGenerator()
#
#     scacData = utills.readData(file, "Sheet1", r, 11).split(",")
#     billofladdingNo = random_BillGenerator()
#     uomData = utills.readData(file, "Sheet1", r, 13).split(",")
#     qtyyData = utills.readData(file, "Sheet1", r, 14).split(",")
#
#     scacData2 = "MFUS"
#     billofladdingNo2 = random_BillGenerator()
#     uomData2 = "PKG"
#     qtyyData2 = "50"
#
#     vesselsname = utills.readData(file, "Sheet1", r, 15)
#     vessellsno = utills.readData(file, "Sheet1", r, 16)
#     containerscount = utills.readData(file, "Sheet1", r, 4)
#     containerlist = utills.readData(file, "Sheet1", r, 17).split(",")
#
#     manufacturerdata = utills.readData(file, "Sheet1", r, 18)
#     sellerdata = utills.readData(file, "Sheet1", r, 19)
#     consigneedata = utills.readData(file, "Sheet1", r, 20)
#     buyerdata = utills.readData(file, "Sheet1", r, 21)
#
#     countryOfOrigindata1 = utills.readData(file, "Sheet1", r, 22)
#     release_portdata = utills.readData(file, "Sheet1", r, 23)
#     countryOfExportdata1 = utills.readData(file, "Sheet1", r, 24)
#     ladingportdata = utills.readData(file, "Sheet1", r, 25)
#     grossWeightdata = utills.readData(file, "Sheet1", r, 26)
#     chargedata = utills.readData(file, "Sheet1", r, 27)
#     unladingportdata = utills.readData(file, "Sheet1", r, 28)
#     manifestDescriptiondata = utills.readData(file, "Sheet1", r, 29)
#     arrivaldatedata = utills.readData(file, "Sheet1", r, 30)
#     exportdatedata = utills.readData(file, "Sheet1", r, 31)
#     currencyData = utills.readData(file, "Sheet1", r, 112)
#
#     invoiceTotaldata = utills.readData(file, "Sheet1", r, 32)
#     tariffnodata = utills.readData(file, "Sheet1", r, 33).split(",")
#     htsqty1 = utills.readData(file, "Sheet1", r, 34)
#     htsqty2 = utills.readData(file, "Sheet1", r, 35)
#     addcaseNumberData = utills.readData(file, "Sheet1", r, 111)
#     cvdcaseNumberData = utills.readData(file, "Sheet1", r, 110)
#     linevaluedata = utills.readData(file, "Sheet1", r, 36).split(",")
#     countryOfOrigindata2 = utills.readData(file, "Sheet1", r, 37).split(",")
#     countryOfExportdata2 = utills.readData(file, "Sheet1", r, 38).split(",")
#     partsData = utills.readData(file, "Sheet1", r, 113).split(",")
#
#     # Passing the data in application
#     # ----------------------------------
#
#     # Login
#     login_username = mywait.until(EC.element_to_be_clickable((By.ID, "username")))
#     login_username.click()
#     login_username.send_keys(usern)
#     login_password = mywait.until(EC.element_to_be_clickable((By.ID, "password")))
#     login_password.click()
#     login_password.send_keys(pasw)
#     driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
#     print("Login Done")
#     logging.info("Login Done")
#
#     # HomePage
#     time.sleep(4)
#     Shipment = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Shipments")))
#     Shipment.click()
#     time.sleep(2)
#     Form7501 = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Form 7501")))
#     Form7501.click()
#     time.sleep(1)
#     print("7501 Form opened")
#     logging.info("7501 Form opened")
#     #---------------------------------------------------------------------------------------------------------
#
#     # # Upper Section
#     # Bill Of lading
#     # Vessel Inforrmation
#     # Trading Partners
#     # Line Items
#     try:
#         invoiceTotalTxt = driver.find_element(By.CSS_SELECTOR, "input#invoiceTotal")
#         if currencyData != "EURO":
#             invoiceTotalTxt.send_keys(invoiceTotaldata)
#     except:
#         pass
#
#     try:
#         for valhts, valcorgn, valcexprt, lnvl, partvl in zip(tariffnodata, countryOfOrigindata2,
#                                                                               countryOfExportdata2, linevaluedata, partsData):
#             tariffnotxt = driver.find_element(By.XPATH,"//span[text()='Tariff #1:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @class='form-control ng-untouched ng-pristine ng-valid']")
#             countryOfOriginText2 = driver.find_element(By.XPATH,"//span[text()='Country of Origin:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @required]")
#             countryOfExportText2 = driver.find_element(By.XPATH,"//span[text()='Country of Export:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @required]")
#             linevaluesadd = driver.find_element(By.XPATH,"//span[text()='Line Value (USD):']//parent::div//following-sibling::div/input[@name='linevalue']")
#             addlineitembutton = driver.find_element(By.XPATH, "//button[normalize-space()='Add New Line']")
#             # partTxt = driver.find_element(By.XPATH,"//span[text()='Part:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @class='form-control ng-untouched ng-pristine ng-valid' and @aria-multiline='false']")
#             partTxt = locate_with(By.XPATH, "button").to_left_of({By.XPATH: "//span[text()='Country of Export:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @required]"})
#
#
#             partTxt.click()
#             partTxt.send_keys(partvl)
#             time.sleep(2)
#             partTxt.send_keys(Keys.ENTER)
#             time.sleep(1)
#
#
#             cottonHTS = driver.find_element(By.TAG_NAME, "body").text
#             if 'This tarrif contain Cotton Fee do you want to exempt fees?' in cottonHTS:
#                 driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
#                 time.sleep(1)
#                 print("It is Cotton HTS")
#                 logging.info("It is Cotton HTS")
#
#             #chinaHTS=driver.find_elements(By.XPATH, "//button[normalize-space()='Yes']")
#             chinaHTS = driver.find_element(By.TAG_NAME, "body").text
#             if 'This Tarrif Contain Additional China Tariff' in chinaHTS:
#                 driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
#                 time.sleep(1)
#                 print("It is China HTS")
#                 logging.info("It is China HTS")
#
#
#
#             # Add line value
#             try:
#                 if currencyData == "EURO":
#                     foreignLineValueTxt = driver.find_element(By.XPATH,"//span[text()='Foreign Line Value:']//parent::div//following-sibling::div/input[@name='linevalue']")
#                     foreignLineValueTxt.send_keys(lnvl)
#                     foreignLineValueOutClick = driver.find_element(By.XPATH, "//span[text()='Foreign Line Value:']")
#                     foreignLineValueOutClick.click()
#                     time.sleep(2)
#                     print("foreign Line Value filled")
#                     logging.info("foreign Line Value filled")
#                 else:
#                     NumberOfLineItem = driver.find_element(By.XPATH,"//button[@aria-expanded='true' and @class='btn btn-link']//div[2]").text
#                     linevalueTxt = driver.find_element(By.XPATH,"(//span[text()='Line Value (USD):']//parent::div//following-sibling::div/input[@name='linevalue'])[" + str(NumberOfLineItem) + "]")
#                     linevalueTxt.send_keys(Keys.CONTROL + 'a')
#                     linevalueTxt.send_keys(Keys.BACKSPACE)
#                     linevalueTxt.send_keys(lnvl)
#             except:
#                 pass
#
#             # ADD CVD
#             if entfilltype == "03":
#                 NumberOfLineItem = driver.find_element(By.XPATH,"//button[@aria-expanded='true' and @class='btn btn-link']//div[2]").text
#
#                 showHideAddCVD = driver.find_element(By.XPATH, "(//a[normalize-space()='Show/Hide ADD/CVD'])[" + str(
#                     NumberOfLineItem) + "]")
#                 showHideAddCVD.click()
#                 addInput = driver.find_element(By.XPATH,"(//input[@id='addCaseNumber'])[" + str(NumberOfLineItem) + "]")
#                 addInput.send_keys(addcaseNumberData)
#                 driver.find_element(By.XPATH, "(//span[normalize-space()='ADD Case Number:'])[" + str(
#                     NumberOfLineItem) + "]").click()
#                 time.sleep(1)
#                 cvdInput = driver.find_element(By.XPATH,"(//input[@id='cvdCaseNumber'])[" + str(NumberOfLineItem) + "]")
#                 cvdInput.send_keys(cvdcaseNumberData)
#                 driver.find_element(By.XPATH, "(//span[normalize-space()='CVD Case Number:'])[" + str(
#                     NumberOfLineItem) + "]").click()
#                 time.sleep(1)
#
#
#                 # showHideAddCVD=driver.find_element(By.XPATH,"//a[normalize-space()='Show/Hide ADD/CVD']")
#                 # showHideAddCVD.click()
#                 # addInput= driver.find_element(By.XPATH,"//input[@id='addCaseNumber']")
#                 # addInput.send_keys(addcaseNumberData)
#                 # driver.find_element(By.XPATH,"//span[normalize-space()='ADD Case Number:']").click()
#                 # time.sleep(1)
#                 # cvdInput = driver.find_element(By.XPATH, "//input[@id='cvdCaseNumber']")
#                 # cvdInput.send_keys(cvdcaseNumberData)
#                 # driver.find_element(By.XPATH, "//span[normalize-space()='CVD Case Number:']").click()
#                 # time.sleep(1)
#
#
#             # PGA Form
#
#             DataFilledInLineAItem = tariffnotxt.get_attribute("value") and countryOfOriginText2.get_attribute("value") and countryOfExportText2.get_attribute("value")
#             NumberOfLineItemsDone = driver.find_element(By.XPATH,"//button[@aria-expanded='true' and @class='btn btn-link']//div[2]").text
#
#             # Add new Line Item
#             addlineitembutton.click()
#
#             if DataFilledInLineAItem:
#                 print("Line Item", NumberOfLineItemsDone, "Done")
#             else:
#                 print("Line Item", NumberOfLineItemsDone, " Not Done")
#
#         # Remove next line item if line items are greater than we want
#         try:
#             removeLineItem = mywait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'Remove Line')])[" + str(lineitmscount + 1) + "]")))
#             removeLineItem.click()
#             print("Total Line Items are", lineitmscount)
#             # logging.info("Total Line Items are", lineitmscount)
#         except Exception as e:
#             print(e)
#             logging.error(e)
#
#     except Exception as e:
#         print(e)
#         logging.error(e)
#








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
for r in range(15, 16):
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
    manufacturerdata = utills.readData(file, "Sheet1", r, 18)
    sellerdata = utills.readData(file, "Sheet1", r, 19)
    consigneedata = utills.readData(file, "Sheet1", r, 20)
    buyerdata = utills.readData(file, "Sheet1", r, 21)
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

    # HomePage
    time.sleep(4)
    Shipment = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Shipments")))
    Shipment.click()
    time.sleep(2)
    Form7501 = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Form 7501")))
    Form7501.click()
    time.sleep(1)
    print("7501 Form opened")
    #---------------------------------------------------------------------------------------------------------

    # Trading Partners
    manufacturer = driver.find_element(By.NAME, "manufacturer")
    manufacturer.click()
    manufacturer.send_keys(manufacturerdata)
    manufacturerlist = mywait.until(EC.presence_of_all_elements_located((By.XPATH, "//div//ngb-typeahead-window[@class='dropdown-menu show']//button")))
    for listitem in manufacturerlist:
        if manufacturerdata in listitem.text:
            listitem.click()
            break

    seller = driver.find_element(By.NAME, "seller")
    seller.click()
    seller.send_keys(sellerdata)
    sellerlist = mywait.until(EC.presence_of_all_elements_located(
        (By.XPATH, "//div//ngb-typeahead-window[@class='dropdown-menu show']//button")))
    for listitem in manufacturerlist:
        if "ARTTESTDEMO" in listitem.text:
            listitem.click()
            break

