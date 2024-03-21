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
logging.info("Login Done")
SHORT_TIMEOUT = 1  # give time for the loading element to appear
LONG_TIMEOUT = 30  # give time for loading to finish
LOADING_ELEMENT_XPATH = "//body//app-root//app-loader//h3[@class='loadingScreen__text']"
try:
    WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
except TimeoutException:
    pass
Shipment = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Shipments")))
Shipment.click()
time.sleep(2)

# Select Importer
for r in range(3, 4):
    selectImporterData = utills.readData(file, "Sheet1", r, 140)
    selectImporterTxt = mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='typeahead-basic']")))
    selectImporterTxt.click()
    selectImporterTxt.send_keys(selectImporterData)
    time.sleep(2)
    selectImporterTxt.send_keys(Keys.ENTER)

for r in range(9, 21):
    i = 0
    i = i - 1
    billCounts = utills.readData(file, "Sheet1", r, 2)
    lineitmscount = utills.readData(file, "Sheet1", r, 3)
    testCasesNumber = utills.readData(file, "Sheet1", r, 10)
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
    # billofladdingNo = utills.readData(file, "Sheet1", r, 12).split(",")
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

    # Passing the data in application
    # ----------------------------------
    # HomePage
    Form7501 = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Form 7501")))
    Form7501.click()
    time.sleep(1)
    print("7501 Form opened")
    logging.info("7501 Form opened")
    print("Test Case no : ",testCasesNumber, " Started")
    # logging.info("Test Case no : ",testCasesNumber, " Started")
    #---------------------------------------------------------------------------------------------------------

    # Upper Section
    try:
        entryfillingtypecode = driver.find_element(By.ID, "entryFilingTypeCode")
        entryfillingtypecode.click()
        entryfillingtypecode.send_keys(entfilltype)
        entryfillingtypecode.send_keys(Keys.ENTER)

        actionCode = driver.find_element(By.ID, "actionCode")
        actionCode.click()
        actionCode.send_keys(actionC)
        actionCode.send_keys(Keys.ENTER)

        if trnpmode != 11:
            modeOfTransport = driver.find_element(By.ID, "modeOfTransport")
            modeOfTransport.click()
            modeOfTransport.send_keys(trnpmode)
            modeOfTransport.send_keys(Keys.ENTER)

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


    # Bill Of lading
    try:
        if billCounts ==2:
            billCounts = billCounts - 1
            for i in range(billCounts):
                driver.find_element(By.XPATH, "//button[normalize-space()='Add a Bill']").click()
                time.sleep(1)
            for val_SCAC, val_UOM, val_BL_QTY in zip(scacData, uomData, qtyyData):  # button #val_BL  billofladdingNo
                scaccodeTxt = mywait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='scac']")))
                billTxt = driver.find_element(By.XPATH,
                                              "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='billOfLading']")
                uomvTxt = mywait.until(EC.element_to_be_clickable(
                    (By.XPATH, "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='uom']")))
                quantityTxt = driver.find_element(By.XPATH,
                                                  "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='quantity']")

                # scaccodeTxt.click()
                # scaccodeTxt.send_keys(val_SCAC)
                # time.sleep(2)
                # scaccodeTxt.send_keys(Keys.ENTER)
                if trnpmode == 40 or trnpmode == 41:
                    scaccodeTxt.click()
                    scaccodeTxt.send_keys(scacData3)
                    time.sleep(2)
                    scaccodeTxt.send_keys(Keys.ENTER)
                else:
                    scaccodeTxt.click()
                    scaccodeTxt.send_keys(scacData2)
                    time.sleep(2)
                    scaccodeTxt.send_keys(Keys.ENTER)

                billTxt.click()
                billTxt.send_keys(billofladdingNo)
                outclick = driver.find_element(By.XPATH, "// span[normalize-space()='Split Shipment:']")
                outclick.click()
                time.sleep(2)

                billalert = driver.find_elements(By.XPATH,
                                                 "//div[@class='swal2-popup swal2-modal swal2-icon-warning animate__animated animate__fadeInDown']//button[text()='OK']")
                if billalert:
                    time.sleep(1)
                    driver.find_element(By.XPATH,
                                        "//div[@class='swal2-popup swal2-modal swal2-icon-warning animate__animated animate__fadeInDown']//button[text()='OK']").click()
                    print("This Bill Number is already Used in another Entry")
                    time.sleep(1)

                uomvTxt.click()
                time.sleep(1)
                uomvTxt.send_keys(val_UOM)
                time.sleep(2)
                uomvTxt.send_keys(Keys.ENTER)

                quantityTxt.send_keys(val_BL_QTY)

                # Check if all data filled in Bill of lading or not
                DataFilledInBillOfLading = scaccodeTxt.get_attribute("value") and uomvTxt.get_attribute(
                    "value") and billTxt.get_attribute("value") and quantityTxt.get_attribute("value")
                if DataFilledInBillOfLading:
                    print("----Bill Of Lading Done----")
                else:
                    print("!----Bill Of Lading Not Done----!")
        elif billCounts ==1:
            scaccodeTxt = mywait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='scac']")))
            billTxt = driver.find_element(By.XPATH,
                                          "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='billOfLading']")
            uomvTxt = mywait.until(EC.element_to_be_clickable(
                (By.XPATH, "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='uom']")))
            quantityTxt = driver.find_element(By.XPATH,
                                              "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='quantity']")

            if  trnpmode == 40 or trnpmode == 41:
                scaccodeTxt.click()
                scaccodeTxt.send_keys(scacData3)
                time.sleep(2)
                scaccodeTxt.send_keys(Keys.ENTER)
            else:
                scaccodeTxt.click()
                scaccodeTxt.send_keys(scacData2)
                time.sleep(2)
                scaccodeTxt.send_keys(Keys.ENTER)

            billTxt.click()
            billTxt.send_keys(billofladdingNo2)
            outclick = driver.find_element(By.XPATH, "// span[normalize-space()='Split Shipment:']")
            outclick.click()
            time.sleep(2)

            billalert = driver.find_elements(By.XPATH,
                                             "//div[@class='swal2-popup swal2-modal swal2-icon-warning animate__animated animate__fadeInDown']//button[text()='OK']")
            if billalert:
                time.sleep(1)
                driver.find_element(By.XPATH,
                                    "//div[@class='swal2-popup swal2-modal swal2-icon-warning animate__animated animate__fadeInDown']//button[text()='OK']").click()
                print("This Bill Number is already Used in another Entry")
                time.sleep(1)

            uomvTxt.click()
            time.sleep(1)
            uomvTxt.send_keys(uomData2)
            time.sleep(2)
            uomvTxt.send_keys(Keys.ENTER)

            quantityTxt.send_keys(qtyyData2)

            # Check if all data filled in Bill of lading or not
            DataFilledInBillOfLading = scaccodeTxt.get_attribute("value") and uomvTxt.get_attribute(
                "value") and billTxt.get_attribute("value") and quantityTxt.get_attribute("value")
            if DataFilledInBillOfLading:
                print("----Bill Of Lading Done----")
            else:
                print("!----Bill Of Lading Not Done----!")

    except Exception as e:
        print(e)


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


    # Trading Partners
    try:
        manufacturer = driver.find_element(By.NAME, "manufacturer")
        manufacturer.click()
        manufacturer.send_keys(manufacturerdata)
        time.sleep(2)
        manufacturer.send_keys(Keys.ENTER)
        time.sleep(1)

        seller = driver.find_element(By.NAME, "seller")
        seller.click()
        seller.send_keys(sellerdata)
        time.sleep(2)
        seller.send_keys(Keys.ENTER)
        time.sleep(1)

        consignee = driver.find_element(By.XPATH, "//input[@name='consignee']")
        consignee.click()
        consignee.send_keys(consigneedata)
        time.sleep(2)
        consignee.send_keys(Keys.ENTER)
        time.sleep(1)

        buyer = driver.find_element(By.XPATH, "//input[@name='buyer']")
        buyer.click()
        buyer.send_keys(buyerdata)
        time.sleep(2)
        buyer.send_keys(Keys.ENTER)
        time.sleep(1)

        # Check if all data filled in Trading Partner 1 or not
        if manufacturer.get_attribute("value") and buyer.get_attribute("value") and consignee.get_attribute("value") and seller.get_attribute("value"):
            print("----Trading Partner 1 Done----")
            logging.info("----Trading Partner 1 Done----")
        else:
            print("!----Trading Partner 1 Not Done----!")
            logging.error("!----Trading Partner 1 Not Done----!")

    except Exception as e:
        print(e)
        logging.error(e)

    try:
        countryOfOriginText1 = driver.find_element(By.XPATH,"//div[@class='formBorderBill']//div[@class='row new-form-row'][1]//div[@class='col-md-3 form-lable'][2]//input[@id='typeahead-basic']")
        countryOfOriginText1.click()
        countryOfOriginText1.send_keys(countryOfOrigindata1)
        time.sleep(2)
        countryOfOriginText1.send_keys(Keys.ENTER)

        release_port = driver.find_element(By.NAME, "releasePort")
        release_port.click()
        release_port.send_keys(release_portdata)
        time.sleep(2)
        release_port.send_keys(Keys.ENTER)

        if currencyData == "EURO":
            selectCurrency = driver.find_element(By.XPATH, "//div[@class='formBorderBill']//input[@name='currency']")
            selectCurrency.click()
            selectCurrency.send_keys(Keys.CONTROL, 'a')
            selectCurrency.send_keys(Keys.DELETE)
            time.sleep(1)
            selectCurrency.send_keys(currencyData)
            time.sleep(2)
            selectCurrency.send_keys(Keys.ENTER)
            driver.find_element(By.XPATH, "//div[@class='formBorderBill']//span[contains(text(),'Currency:')]").click()

        countryOfExportText1 = driver.find_element(By.XPATH,"//div[@class='formBorderBill']//div[@class='row new-form-row'][2]//div[@class='col-md-3 form-lable'][2]//input[@id='typeahead-basic']")
        countryOfExportText1.click()
        countryOfExportText1.send_keys(countryOfExportdata1)
        time.sleep(2)
        countryOfExportText1.send_keys(Keys.ENTER)

        ladingportText = driver.find_element(By.XPATH,"//div[@class='formBorderBill']//div[@class='row new-form-row'][4]//div[@class='col-md-3 form-lable'][1]//input[@id='typeahead-basic']")
        ladingportText.click()
        ladingportText.send_keys(ladingportdata)
        time.sleep(2)
        ladingportText.send_keys(Keys.ENTER)

        weight = driver.find_element(By.ID, "grossWeight")
        weight.clear()
        weight.send_keys(grossWeightdata)

        charges = driver.find_element(By.NAME, "charges")
        charges.clear()
        charges.send_keys(chargedata)

        # driver.find_element(By.ID,"usStateCode").send_keys("MN")

        unladingportText = driver.find_element(By.XPATH,"//div[@class='formBorderBill']//div[@class='row new-form-row'][5]//div[@class='col-md-3 form-lable'][1]//input[@id='typeahead-basic']")
        unladingportText.click()
        unladingportText.send_keys(unladingportdata)
        time.sleep(2)
        unladingportText.send_keys(Keys.ENTER)

        driver.find_element(By.NAME, "manifestDescription").send_keys(manifestDescriptiondata)

        arrivaldate = driver.find_element(By.XPATH, "//input[@name='arrivalDate']")
        arrivaldate.send_keys(arrivaldatedata)
        exportdate = driver.find_element(By.XPATH, "//input[@name='exportDate']")
        exportdate.send_keys(exportdatedata)

        # Check if all data filled in Trading Partner 2 or not
        if countryOfOriginText1.get_attribute("value") and countryOfExportText1.get_attribute("value") and ladingportText.get_attribute("value") and unladingportText.get_attribute("value")\
                and release_port.get_attribute("value") and charges.get_attribute("value") and weight.get_attribute("value")\
                and arrivaldate.get_attribute("value") and exportdate.get_attribute("value"):
            print("----Trading Partner 2 Done----")
            logging.info("----Trading Partner 2 Done----")
        else:
            print("!----Trading Partner 2 Not Done----!")
            logging.error("!----Trading Partner 2 Not Done----!")

    except Exception as e:
        print(e)
        logging.error(e)

    # Line Items
    try:
        invoiceTotalTxt = driver.find_element(By.CSS_SELECTOR, "input#invoiceTotal")
        if currencyData != "EURO":
            invoiceTotalTxt.send_keys(invoiceTotaldata)
    except:
        pass

    try:
        for valhts, valcorgn, valcexprt, lnvl in zip(tariffnodata, countryOfOrigindata2,
                                                                              countryOfExportdata2, linevaluedata):
            tariffnotxt = driver.find_element(By.XPATH,"//span[text()='Tariff #1:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @class='form-control ng-untouched ng-pristine ng-valid']")
            countryOfOriginText2 = driver.find_element(By.XPATH,"//span[text()='Country of Origin:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @required]")
            countryOfExportText2 = driver.find_element(By.XPATH,"//span[text()='Country of Export:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @required]")
            linevaluesadd = driver.find_element(By.XPATH,"//span[text()='Line Value (USD):']//parent::div//following-sibling::div/input[@name='linevalue']")
            addlineitembutton = driver.find_element(By.XPATH, "//button[normalize-space()='Add New Line']")

            countryOfOriginText2.click()
            countryOfOriginText2.send_keys(valcorgn)
            time.sleep(2)
            countryOfOriginText2.send_keys(Keys.ENTER)
            time.sleep(1)

            countryOfExportText2.click()
            countryOfExportText2.send_keys(valcexprt)
            time.sleep(2)
            countryOfExportText2.send_keys(Keys.ENTER)
            time.sleep(1)

            tariffnotxt.click()
            tariffnotxt.send_keys(valhts)
            time.sleep(2)
            tariffnotxt.send_keys(Keys.ENTER)
            time.sleep(1)

            cottonHTS = driver.find_element(By.TAG_NAME, "body").text
            if 'This tarrif contain Cotton Fee do you want to exempt fees?' in cottonHTS:
                driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
                time.sleep(1)
                print("It is Cotton HTS")
                logging.info("It is Cotton HTS")

            #chinaHTS=driver.find_elements(By.XPATH, "//button[normalize-space()='Yes']")
            chinaHTS = driver.find_element(By.TAG_NAME, "body").text
            if 'This Tarrif Contain Additional China Tariff' in chinaHTS:
                driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
                time.sleep(1)
                print("It is China HTS")
                logging.info("It is China HTS")



            # Add line value
            try:
                if currencyData == "EURO":
                    foreignLineValueTxt = driver.find_element(By.XPATH,"//span[text()='Foreign Line Value:']//parent::div//following-sibling::div/input[@name='linevalue']")
                    foreignLineValueTxt.send_keys(lnvl)
                    foreignLineValueOutClick = driver.find_element(By.XPATH, "//span[text()='Foreign Line Value:']")
                    foreignLineValueOutClick.click()
                    time.sleep(2)
                    print("foreign Line Value filled")
                    logging.info("foreign Line Value filled")
                else:
                    NumberOfLineItem = driver.find_element(By.XPATH,"//button[@aria-expanded='true' and @class='btn btn-link']//div[2]").text
                    linevalueTxt = driver.find_element(By.XPATH,"(//span[text()='Line Value (USD):']//parent::div//following-sibling::div/input[@name='linevalue'])[" + str(NumberOfLineItem) + "]")
                    linevalueTxt.send_keys(Keys.CONTROL + 'a')
                    linevalueTxt.send_keys(Keys.BACKSPACE)
                    linevalueTxt.send_keys(lnvl)
            except:
                pass

            # ADD CVD
            if entfilltype == "03":

                NumberOfLineItem = driver.find_element(By.XPATH,"//button[@aria-expanded='true' and @class='btn btn-link']//div[2]").text

                showHideAddCVD = driver.find_element(By.XPATH, "(//a[normalize-space()='Show/Hide ADD/CVD'])[" + str(NumberOfLineItem) + "]")
                showHideAddCVD.click()
                addInput = driver.find_element(By.XPATH,"(//input[@id='addCaseNumber'])[" + str(NumberOfLineItem) + "]")
                addInput.send_keys(addcaseNumberData)
                driver.find_element(By.XPATH, "(//span[normalize-space()='ADD Case Number:'])[" + str(NumberOfLineItem) + "]").click()
                time.sleep(1)
                cvdInput = driver.find_element(By.XPATH,"(//input[@id='cvdCaseNumber'])[" + str(NumberOfLineItem) + "]")
                cvdInput.send_keys(cvdcaseNumberData)
                driver.find_element(By.XPATH, "(//span[normalize-space()='CVD Case Number:'])[" + str(NumberOfLineItem) + "]").click()
                time.sleep(1)

            # PGA Form
            try:
                EP5descriptionData = utills.readData(file, "Sheet1", r, 40)
                EP5desclaimerdata = utills.readData(file, "Sheet1", r, 41)

                EP5 = driver.find_elements(By.XPATH,
                                           "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='EP5']")
                if EP5:
                    driver.find_element(By.XPATH,
                                        "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='EP5']").click()

                    # driver.find_element(By.XPATH, "//div[@class='col-md-3']//a[normalize-space()='EP5']").click()

                    time.sleep(1)

                    # PG01
                    commercialDescription = driver.find_element(By.XPATH,
                                                                "//label[normalize-space()='Commercial Description:']//parent::div//following-sibling::div//input[@id='commercialDescription']")
                    commercialDescription.click()
                    commercialDescription.send_keys(EP5descriptionData)

                    desclaimer = driver.find_element(By.XPATH,
                                                     "//label[text()='Disclaimer:']//parent::div//following-sibling::div//select[@name='disclaimer']")
                    desclaimer.click()
                    desclaimer.send_keys(EP5desclaimerdata)
                    desclaimer.send_keys(Keys.ENTER)

                    # Check if values are fille in PGA or not
                    EP5Attributes = commercialDescription.get_attribute("value")

                    saveAndClose = driver.find_element(By.XPATH, "//button[normalize-space()='Save & Close']")
                    saveAndClose.click()
                    time.sleep(2)

                    try:
                        alertDataIsValidMSG = driver.find_element(By.XPATH,
                                                                  "//div[normalize-space()='1. The Data is Valid...']")
                        if alertDataIsValidMSG:
                            alertDataIsValid = driver.find_element(By.XPATH,
                                                                   "//button[@type='button'][normalize-space()='Save & Close']")
                            alertDataIsValid.click()
                    except Exception as e:
                        print("Error while saving form")
                        logging.error("Error while saving form")
                    time.sleep(1)
                    driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()

                    if EP5Attributes:
                        print("EP5 Filled")
                        logging.info("EP5 Filled")

                    time.sleep(1)
                    maximizeQtySection = mywait.until(EC.element_to_be_clickable((By.XPATH, "//button//span[normalize-space()=" + valhts + "]")))
                    maximizeQtySection.click()
                    time.sleep(1)


                # EP7
                EP7descriptionData = utills.readData(file, "Sheet1", r, 43)
                EP7pgaLineValueData = utills.readData(file, "Sheet1", r, 44)

                EP7individualQualifierdata = utills.readData(file, "Sheet1", r, 45)
                EP7mailOrFaxdata = utills.readData(file, "Sheet1", r, 46)
                EP7individualNameData = utills.readData(file, "Sheet1", r, 47)
                EP7telephoneNoData = utills.readData(file, "Sheet1", r, 48)

                EP7entityRoleCodeData = utills.readData(file, "Sheet1", r, 49)
                EP7declarationCodeData = utills.readData(file, "Sheet1", r, 50)
                EP7declarationCertificationData = utills.readData(file, "Sheet1", r, 51)
                EP7dateSignatureData = utills.readData(file, "Sheet1", r, 52)

                EP7 = driver.find_elements(By.XPATH,
                                           "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='EP7']")
                if EP7:
                    driver.find_element(By.XPATH,
                                        "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='EP7']").click()
                    # driver.find_element(By.XPATH, "//div[@class='col-md-3']//a[normalize-space()='EP7']").click()

                    # driver.find_element(By.XPATH,"//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='EP7']").click()
                    time.sleep(1)

                    # PG01
                    commercialDescription = driver.find_element(By.XPATH,
                                                                "//label[normalize-space()='Commercial Description:']//parent::div//following-sibling::div//input[@id='commercialDescription']")
                    commercialDescription.click()
                    commercialDescription.send_keys(EP7descriptionData)

                    pgaLineValue = driver.find_element(By.XPATH,
                                                       "//label[text()='PGA Line Value:']//parent::div//following-sibling::div//input[@name='pgaLineValue']")
                    pgaLineValue.send_keys(EP7pgaLineValueData)
                    time.sleep(2)

                    # PG21
                    individualQualifier = driver.find_element(By.XPATH,
                                                              "//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic']")
                    individualQualifier.send_keys(EP7individualQualifierdata)
                    time.sleep(2)
                    individualQualifier.send_keys(Keys.ENTER)

                    mailOrFax = driver.find_element(By.XPATH,
                                                    "//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email']")
                    mailOrFax.send_keys(EP7mailOrFaxdata)

                    individualName = driver.find_element(By.XPATH,
                                                         "//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName']")
                    individualName.send_keys(EP7individualNameData)

                    telephoneNo = driver.find_element(By.XPATH,
                                                      "//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo']")
                    telephoneNo.send_keys(EP7telephoneNoData)

                    # addNewQualifier = driver.find_element(By.XPATH, "//div//button[normalize-space()='Add New Individual']")
                    # addNewQualifier.click()

                    # PG22
                    entityRoleCode = driver.find_element(By.XPATH,
                                                         "//span[text()='Entity Role Code:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic']")
                    entityRoleCode.send_keys(EP7entityRoleCodeData)
                    time.sleep(2)
                    entityRoleCode.send_keys(Keys.ENTER)

                    declarationCode = driver.find_element(By.XPATH,
                                                          "//span[text()='Declaration Code:']//parent::div//following-sibling::div/input[@name='declarationCode']")
                    declarationCode.send_keys(EP7declarationCodeData)

                    declarationCertification = driver.find_element(By.XPATH,
                                                                   "//span[text()='Declaration Certification:']//parent::div//following-sibling::div/select[@name='declarationCertification']")
                    declarationCertification.send_keys(EP7declarationCertificationData)
                    time.sleep(2)
                    declarationCertification.send_keys(Keys.ENTER)

                    dateSignature = driver.find_element(By.XPATH,
                                                        "//span[text()='Date Signature:']//parent::div//following-sibling::div//input[@name='dateSignature']")
                    dateSignature.send_keys(EP7dateSignatureData)

                    driver.find_element(By.XPATH, "//span[normalize-space()='Date Signature:']").click()

                    # Check if values are fille in PGA or not
                    EP7Attributes = commercialDescription.get_attribute("value") and pgaLineValue.get_attribute(
                        "value") and individualName.get_attribute("value") and entityRoleCode.get_attribute(
                        "value") and dateSignature.get_attribute("value")

                    saveAndClose = driver.find_element(By.XPATH, "//button[normalize-space()='Save & Close']")
                    saveAndClose.click()
                    time.sleep(2)

                    try:
                        alertDataIsValidMSG = driver.find_element(By.XPATH,
                                                                  "//div[normalize-space()='1. The Data is Valid...']")
                        if alertDataIsValidMSG:
                            alertDataIsValid = driver.find_element(By.XPATH,
                                                                   "//button[@type='button'][normalize-space()='Save & Close']")
                            alertDataIsValid.click()
                    except Exception as e:
                        print("Error while saving form")
                        logging.error("Error while saving form")
                    time.sleep(1)
                    driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()
                    if EP7Attributes:
                        print("EP7 Filled")
                        logging.error("EP7 Filled")
                    # time.sleep(1)
                    maximizeQtySection = mywait.until(
                        EC.element_to_be_clickable((By.XPATH, "//button//span[normalize-space()=" + valhts + "]")))
                    maximizeQtySection.click()
                    time.sleep(1)

                # FD1

                FD1agencyProcessingCodeData = utills.readData(file, "Sheet1", r, 54)
                FD1pgaLineValueData = utills.readData(file, "Sheet1", r, 55)
                FD1descriptionData = utills.readData(file, "Sheet1", r, 56)

                FD1EntityMF = utills.readData(file, "Sheet1", r, 58)
                FD1EntityDEQ = utills.readData(file, "Sheet1", r, 59)
                FD1EntityFD1 = utills.readData(file, "Sheet1", r, 60)
                FD1EntityDFP = utills.readData(file, "Sheet1", r, 61)
                FD1EntityPNS = utills.readData(file, "Sheet1", r, 62)
                FD1EntityIM = utills.readData(file, "Sheet1", r, 63)
                FD1EntityPNT = utills.readData(file, "Sheet1", r, 64)
                FD1EntityFSV = utills.readData(file, "Sheet1", r, 65)
                FD1EntityUC = utills.readData(file, "Sheet1", r, 66)
                FD1EntityPK = utills.readData(file, "Sheet1", r, 67)

                FD1individualQualifierData1 = utills.readData(file, "Sheet1", r, 68)
                FD1mailOrFaxData1 = utills.readData(file, "Sheet1", r, 69)
                FD1individualNameData1 = utills.readData(file, "Sheet1", r, 70)
                FD1telephoneNoData1 = utills.readData(file, "Sheet1", r, 71)

                FD1individualQualifierData2 = utills.readData(file, "Sheet1", r, 98)
                FD1mailOrFaxData2 = utills.readData(file, "Sheet1", r, 99)
                FD1individualNameData2 = utills.readData(file, "Sheet1", r, 100)
                FD1telephoneNoData2 = utills.readData(file, "Sheet1", r, 101)

                FD1individualQualifierData3 = utills.readData(file, "Sheet1", r, 102)
                FD1mailOrFaxData3 = utills.readData(file, "Sheet1", r, 103)
                FD1individualNameData3 = utills.readData(file, "Sheet1", r, 104)
                FD1telephoneNoData3 = utills.readData(file, "Sheet1", r, 105)

                FD1individualQualifierData4 = utills.readData(file, "Sheet1", r, 106)
                FD1mailOrFaxData4 = utills.readData(file, "Sheet1", r, 107)
                FD1individualNameData4 = utills.readData(file, "Sheet1", r, 108)
                FD1telephoneNoData4 = utills.readData(file, "Sheet1", r, 109)

                FD1itemTypeData = utills.readData(file, "Sheet1", r, 73)
                FD1productcodequalifierData = utills.readData(file, "Sheet1", r, 74)
                FD1productcodnumberData = utills.readData(file, "Sheet1", r, 75)
                FD1packagingQualifierData = utills.readData(file, "Sheet1", r, 77)
                FD1unitOfMeasureData = utills.readData(file, "Sheet1", r, 78)
                FD1pg26qtyData = utills.readData(file, "Sheet1", r, 79)

                FD1SpecialUseDesignationData1 = utills.readData(file, "Sheet1", r, 81)
                FD1sourceTypeCodeData1 = utills.readData(file, "Sheet1", r, 82)
                FD1countryCodeData1 = utills.readData(file, "Sheet1", r, 83)

                FD1SpecialUseDesignationData2 = utills.readData(file, "Sheet1", r, 115)
                FD1sourceTypeCodeData2 = utills.readData(file, "Sheet1", r, 116)
                FD1countryCodeData2 = utills.readData(file, "Sheet1", r, 117)

                FD1commodityCharDescripData = utills.readData(file, "Sheet1", r, 85)

                FD1afrmativecodeData1 = utills.readData(file, "Sheet1", r, 87)
                FD1afrmativedescriptionData1 = utills.readData(file, "Sheet1", r, 89)
                FD1afrmativecodeData2 = utills.readData(file, "Sheet1", r, 88)
                FD1afrmativedescriptionData2 = utills.readData(file, "Sheet1", r, 90)
                FD1afrmativedescriptionData3 = utills.readData(file, "Sheet1", r, 120)
                FD1afrmativecodeData3 = utills.readData(file, "Sheet1", r, 119)

                FD1inspLabTestData = utills.readData(file, "Sheet1", r, 92)
                FD1schedTimeOfInspecData = utills.readData(file, "Sheet1", r, 93)
                FD1scheduledDateOfInspectionData = utills.readData(file, "Sheet1", r, 94)
                FD1inspectionorArrivallocationData = utills.readData(file, "Sheet1", r, 95)
                FD1inspectionorArrivallocationCodeData = utills.readData(file, "Sheet1", r, 96)

                FD1containerNumberData = utills.readData(file, "Sheet1", r, 121)

                FD1 = driver.find_elements(By.XPATH,
                                           "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='FD1']")
                if FD1:
                    driver.find_element(By.XPATH,
                                        "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='FD1']").click()
                    time.sleep(1)

                    # agency
                    driver.find_element(By.XPATH, "//li/a[normalize-space()='FOO']").click()
                    time.sleep(1)

                    # PG01
                    agencyProcessingCode = driver.find_element(By.XPATH,
                                                               "//label[normalize-space()='Agency Processing Code:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic']")
                    agencyProcessingCode.click()
                    agencyProcessingCode.send_keys(FD1agencyProcessingCodeData)
                    time.sleep(2)
                    agencyProcessingCode.send_keys(Keys.ENTER)
                    time.sleep(1)

                    commercialDescription = driver.find_element(By.XPATH,
                                                                "//label[normalize-space()='Commercial Description:']//parent::div//following-sibling::div//input[@id='commercialDescription']")
                    commercialDescription.click()
                    commercialDescription.send_keys(FD1descriptionData)

                    pgaLineValue = driver.find_element(By.XPATH,
                                                       "//label[text()='PGA Line Value:']//parent::div//following-sibling::div//input[@name='pgaLineValue']")
                    pgaLineValue.send_keys(FD1pgaLineValueData)
                    time.sleep(2)

                    # PG19,20
                    addEntities = driver.find_element(By.XPATH, "//select[@id='entities']")

                    # FD1
                    addEntities.click()
                    selectFD1 = driver.find_element(By.XPATH, "//option[normalize-space()='FDA Importer 1 - FD1']")
                    selectFD1.click()
                    # DFP
                    selectDFP = driver.find_element(By.XPATH, "//option[normalize-space()='Owner - DFP']")
                    selectDFP.click()
                    # PNS
                    selectPNS = driver.find_element(By.XPATH, "//option[normalize-space()='PN Submitter - PNS']")
                    selectPNS.click()
                    # PNT
                    selectPNT = driver.find_element(By.XPATH, "//option[normalize-space()='PN Transmitter - PNT']")
                    selectPNT.click()
                    # FSV
                    selectFSV = driver.find_element(By.XPATH,
                                                    "//option[normalize-space()='Foreign Supplier Verification Program - FSV']")
                    selectFSV.click()
                    # PK
                    selectPK = driver.find_element(By.XPATH, "//option[normalize-space()='Point Of Contact - PK']")
                    selectPK.click()

                    mf = driver.find_element(By.XPATH,
                                             "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[1]")
                    mf.click()
                    mf.send_keys(FD1EntityMF)
                    time.sleep(2)
                    mf.send_keys(Keys.ENTER)

                    deq = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[2]")
                    deq.click()
                    deq.send_keys(FD1EntityDEQ)
                    time.sleep(2)
                    deq.send_keys(Keys.ENTER)

                    fd1 = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[3]")
                    fd1.click()
                    fd1.send_keys(FD1EntityFD1)
                    time.sleep(2)
                    fd1.send_keys(Keys.ARROW_DOWN)
                    fd1.send_keys(Keys.ENTER)

                    dfp = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[4]")
                    dfp.click()
                    dfp.send_keys(FD1EntityDFP)
                    time.sleep(2)
                    dfp.send_keys(Keys.ARROW_DOWN)
                    dfp.send_keys(Keys.ENTER)

                    pns = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[5]")
                    pns.click()
                    pns.send_keys(FD1EntityPNS)
                    time.sleep(2)
                    pns.send_keys(Keys.ENTER)

                    pnt = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[6]")
                    pnt.click()
                    pnt.send_keys(FD1EntityPNT)
                    time.sleep(2)
                    pnt.send_keys(Keys.ENTER)

                    uc = driver.find_element(By.XPATH,
                                             "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[7]")
                    uc.click()
                    uc.send_keys(FD1EntityUC)
                    time.sleep(2)
                    uc.send_keys(Keys.ARROW_DOWN)
                    uc.send_keys(Keys.ENTER)

                    fsv = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[8]")
                    fsv.click()
                    fsv.send_keys(FD1EntityFSV)
                    time.sleep(2)
                    fsv.send_keys(Keys.ENTER)

                    pk = driver.find_element(By.XPATH,
                                             "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[10]")
                    pk.click()
                    pk.send_keys(FD1EntityPK)
                    time.sleep(2)
                    pk.send_keys(Keys.ENTER)

                    time.sleep(2)

                    # PG21

                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Individual')])[1]").click()
                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Individual')])[1]").click()
                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Individual')])[1]").click()

                    individualQualifierTxt1 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[1]")
                    mailOrFaxTxt1 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[1]")
                    individualNameTxt1 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[1]")
                    telephoneNoTxt1 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[1]")

                    individualQualifierTxt1.click()
                    individualQualifierTxt1.send_keys(FD1individualQualifierData1)
                    time.sleep(2)
                    individualQualifierTxt1.send_keys(Keys.ENTER)
                    mailOrFaxTxt1.send_keys(FD1mailOrFaxData1)
                    individualNameTxt1.send_keys(FD1individualNameData1)
                    telephoneNoTxt1.send_keys(FD1telephoneNoData1)

                    individualQualifierTxt2 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[2]")
                    mailOrFaxTxt2 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[2]")
                    individualNameTxt2 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[2]")
                    telephoneNoTxt2 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[2]")

                    individualQualifierTxt2.click()
                    individualQualifierTxt2.send_keys(FD1individualQualifierData2)
                    time.sleep(2)
                    individualQualifierTxt2.send_keys(Keys.ENTER)
                    mailOrFaxTxt2.send_keys(FD1mailOrFaxData2)
                    individualNameTxt2.send_keys(FD1individualNameData2)
                    telephoneNoTxt2.send_keys(FD1telephoneNoData2)

                    individualQualifierTxt3 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[3]")
                    mailOrFaxTxt3 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[3]")
                    individualNameTxt3 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[3]")
                    telephoneNoTxt3 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[3]")

                    individualQualifierTxt3.click()
                    individualQualifierTxt3.send_keys(FD1individualQualifierData3)
                    time.sleep(2)
                    individualQualifierTxt3.send_keys(Keys.ENTER)
                    mailOrFaxTxt3.send_keys(FD1mailOrFaxData3)
                    individualNameTxt3.send_keys(FD1individualNameData3)
                    telephoneNoTxt3.send_keys(FD1telephoneNoData3)

                    individualQualifierTxt4 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[4]")
                    mailOrFaxTxt4 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[4]")
                    individualNameTxt4 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[4]")
                    telephoneNoTxt4 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[4]")

                    individualQualifierTxt4.click()
                    individualQualifierTxt4.send_keys(FD1individualQualifierData4)
                    time.sleep(2)
                    individualQualifierTxt4.send_keys(Keys.ENTER)
                    mailOrFaxTxt4.send_keys(FD1mailOrFaxData4)
                    individualNameTxt4.send_keys(FD1individualNameData4)
                    telephoneNoTxt4.send_keys(FD1telephoneNoData4)

                    # PG02
                    itemType = driver.find_element(By.XPATH,
                                                   "//label[text()='Item Type:']//parent::div//following-sibling::div/select[@name='itemType']")
                    time.sleep(1)
                    itemType.click()
                    itemType.send_keys(FD1itemTypeData)
                    time.sleep(2)
                    itemType.send_keys(Keys.ENTER)

                    productcodequalifier = driver.find_element(By.XPATH,
                                                               "//label[text()='Product Code Qualifier:']//parent::div//following-sibling::div/select[@name='productCodeQualifier']")
                    productcodequalifier.click()
                    time.sleep(1)
                    productcodequalifier.send_keys(FD1productcodequalifierData)
                    time.sleep(2)
                    productcodequalifier.send_keys(Keys.ENTER)

                    productcodnumber = driver.find_element(By.XPATH,
                                                           "//label[text()='Product Code Number:']//parent::div//following-sibling::div/input[@name='productCodeNumber']")
                    time.sleep(1)
                    productcodnumber.send_keys(FD1productcodnumberData)
                    time.sleep(2)
                    productcodnumber.send_keys(Keys.ENTER)
                    #
                    # PG26
                    packagingQualifier = driver.find_element(By.XPATH,
                                                             "//span[text()='Packaging Qualifier:']//parent::div//following-sibling::div/select[@name='packagingQualifier']")
                    packagingQualifier.click()
                    packagingQualifier.send_keys(FD1packagingQualifierData)
                    packagingQualifier.send_keys(Keys.ENTER)

                    unitOfMeasure = driver.find_element(By.XPATH,
                                                        "//span[text()='Unit of Measure:']//parent::div//following-sibling::div/input[@role='combobox']")
                    unitOfMeasure.send_keys(FD1unitOfMeasureData)
                    time.sleep(3)
                    unitOfMeasure.send_keys(Keys.ENTER)

                    pgaqty = driver.find_element(By.XPATH,
                                                 "//span[text()='Quantity:']//parent::div//following-sibling::div/input[@name='quantity' and@id='quantity' and @maxlength='12']")
                    pgaqty.send_keys(FD1pg26qtyData)

                    # PG04,05,06
                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Constituent')])[1]").click()

                    sourceTypeCodeTxt1 = driver.find_element(By.XPATH,
                                                             "(//label[text()='Source Type Code:']//parent::div//following-sibling::div/select[@name='sourceTypeCode'])[1]")
                    sourceTypeCodeTxt1.click()
                    sourceTypeCodeTxt1Option = driver.find_element(By.XPATH,
                                                                   "//option[normalize-space()='CSH - CSH - Country of Shipment']")
                    sourceTypeCodeTxt1Option.click()

                    specialUseDesignationTxt1 = driver.find_element(By.XPATH,
                                                                    "(//label[text()='Special Use Designation:']//parent::div//following-sibling::div/select[@name='specialUseDesignation'])[1]")
                    specialUseDesignationTxt1.click()
                    specialUseDesignationTxt1.send_keys(FD1SpecialUseDesignationData1)
                    specialUseDesignationTxt1.send_keys(Keys.ENTER)

                    countryCodeTxt1 = driver.find_element(By.XPATH,
                                                          "(//label[text()='Country Code:']//parent::div//following-sibling::div/input[@id='typeahead-basic'])[1]")
                    countryCodeTxt1.send_keys(FD1countryCodeData1)
                    time.sleep(2)
                    countryCodeTxt1.send_keys(Keys.ENTER)

                    specialUseDesignationTxt2 = driver.find_element(By.XPATH,
                                                                    "(//label[text()='Special Use Designation:']//parent::div//following-sibling::div/select[@name='specialUseDesignation'])[2]")
                    specialUseDesignationTxt2.click()
                    specialUseDesignationTxt2.send_keys(FD1SpecialUseDesignationData2)
                    specialUseDesignationTxt2.send_keys(Keys.ENTER)
                    sourceTypeCodeTxt2 = driver.find_element(By.XPATH,
                                                             "(//label[text()='Source Type Code:']//parent::div//following-sibling::div/select[@name='sourceTypeCode'])[2]")
                    sourceTypeCodeTxt2.click()
                    time.sleep(1)
                    sourceTypeCodeTxt2.send_keys(FD1sourceTypeCodeData2)
                    sourceTypeCodeTxt2.send_keys(Keys.ENTER)
                    countryCodeTxt2 = driver.find_element(By.XPATH,
                                                          "(//label[text()='Country Code:']//parent::div//following-sibling::div/input[@id='typeahead-basic'])[2]")
                    countryCodeTxt2.send_keys(FD1countryCodeData2)
                    time.sleep(2)
                    countryCodeTxt2.send_keys(Keys.ENTER)

                    # PG10
                    commodityCharacteristicDescription = driver.find_element(By.XPATH,
                                                                             "//span[text()='Commodity Characteristic Description:']//parent::div//following-sibling::div/input[@name='commodityCharacteristicDescription']")
                    commodityCharacteristicDescription.send_keys(FD1commodityCharDescripData)
                    time.sleep(2)

                    # PG23
                    AddNewInfo_Button = driver.find_element(By.XPATH,
                                                            "//app-affirmation-compliance-list[@class='p-2 ng-valid ng-touched ng-dirty']//button[contains(text(),'Add New Info')]")
                    AddNewInfo_Button.click()
                    AddNewInfo_Button.click()

                    afrmativecodeTxt1 = driver.find_element(By.XPATH, "(//select[@id='affirmationComplianceCode'])[1]")
                    afrmativecodeTxt1.click()
                    afrmativecodeTxt1.send_keys(FD1afrmativecodeData1)
                    afrmativecodeTxt1.send_keys(Keys.ENTER)
                    driver.find_element(By.XPATH, "(//input[@id='description'])[1]").send_keys(
                        FD1afrmativedescriptionData1)

                    afrmativecodeTxt2 = driver.find_element(By.XPATH, "(//select[@id='affirmationComplianceCode'])[2]")
                    afrmativecodeTxt2.click()
                    afrmativecodeTxt2.send_keys(FD1afrmativecodeData2)
                    afrmativecodeTxt2.send_keys(Keys.ENTER)
                    driver.find_element(By.XPATH, "(//input[@id='description'])[2]").send_keys(
                        FD1afrmativedescriptionData2)

                    afrmativecodeTxt3 = driver.find_element(By.XPATH, "(//select[@id='affirmationComplianceCode'])[3]")
                    afrmativecodeTxt3.click()
                    afrmativecodeTxt3.send_keys(FD1afrmativecodeData3)
                    afrmativecodeTxt3.send_keys(Keys.ENTER)
                    driver.find_element(By.XPATH, "(//input[@id='description'])[3]").send_keys(FD1afrmativedescriptionData3)

                    # Opnen PG30
                    driver.find_element(By.XPATH,
                                        "//span[text()='Anticipated Arrival Information - PG30']//parent::div").click()
                    time.sleep(2)

                    inspectionLabTestingStatus = driver.find_element(By.XPATH,
                                                                     "//label[text()='Inspection/Lab Testing Status:']//parent::div//following-sibling::div/select[@name='inspectionTestingStatEntity']")
                    inspectionLabTestingStatus.click()
                    time.sleep(2)
                    inspectionLabTestingStatus.send_keys(FD1inspLabTestData)
                    inspectionLabTestingStatus.send_keys(Keys.ENTER)

                    scheduledTimeOfInspection = driver.find_element(By.XPATH,
                                                                    "//label[text()='Requested or Scheduled Time of Inspection; Time of previous Inspection; Arrival Time:']//parent::div//following-sibling::div/input[@name='scheduledTimeOfInspection']")
                    scheduledTimeOfInspection.send_keys(FD1schedTimeOfInspecData)

                    scheduledDateOfInspection = driver.find_element(By.XPATH,
                                                                    "//label[text()='Requested or Scheduled Date of Inspection; Date of previous Inspection; Arrival Date:']//parent::div//following-sibling::div//input[@name='scheduledDateInspection']")
                    scheduledDateOfInspection.send_keys(FD1scheduledDateOfInspectionData)

                    inspectionorArrivallocation = driver.find_element(By.XPATH,
                                                                      "//label[text()='Inspection or Arrival Location']//parent::div//following-sibling::div//input[@name='inspectionLocation']")
                    inspectionorArrivallocation.send_keys(FD1inspectionorArrivallocationData)

                    inspectionorArrivallocationCode = driver.find_element(By.XPATH,
                                                                          "//label[text()='Inspection or Arrival Location Code::']//parent::div//following-sibling::div/select[@name='arrivalLocationCode']")
                    inspectionorArrivallocationCode.click()
                    time.sleep(2)
                    inspectionorArrivallocationCode.send_keys(FD1inspectionorArrivallocationCodeData)

                    # PG27
                    driver.find_element(By.XPATH, "//input[@id='containerNumber']").send_keys(FD1containerNumberData)

                    # Check if values are fille in PGA or not
                    FD1Attributes = commercialDescription.get_attribute("value") and mf.get_attribute(
                        "value") and productcodequalifier.get_attribute("value")


                    saveAndClose = driver.find_element(By.XPATH, "//button[normalize-space()='Save & Close']")
                    saveAndClose.click()
                    time.sleep(2)

                    try:
                        alertDataIsValidMSG = driver.find_element(By.XPATH,
                                                                  "//div[normalize-space()='1. The Data is Valid...']")
                        if alertDataIsValidMSG:
                            alertDataIsValid = driver.find_element(By.XPATH,
                                                                   "//button[@type='button'][normalize-space()='Save & Close']")
                            alertDataIsValid.click()
                    except Exception as e:
                        print("Error while saving form")
                        logging.error("Error while saving form")

                    time.sleep(1)
                    try:
                        someValidationsError = driver.find_element(By.TAG_NAME, "body").text
                        if 'The Manufacturer record should have an entity number' in someValidationsError:
                            driver.find_element(By.XPATH,
                                                "//button[@type='button'][normalize-space()='Save & Close']").click()
                            time.sleep(1)
                            print("PGA has some validations issues but still PGA form saved")
                    except Exception as e:
                        print("PGA has issues and PGA form saved")
                        print(e)
                        time.sleep(1)
                    driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()
                    if FD1Attributes:
                        print("FD1 Filled")
                        logging.info("FD1 Filled")
                    maximizeQtySection = mywait.until(
                        EC.element_to_be_clickable((By.XPATH, "//button//span[normalize-space()=" + valhts + "]")))
                    maximizeQtySection.click()
                    time.sleep(1)

                # FD2

                FD2 = driver.find_elements(By.XPATH,
                                           "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='FD2']")
                if FD2:
                    driver.find_element(By.XPATH,
                                        "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='FD2']").click()
                    time.sleep(1)

                    # agency
                    driver.find_element(By.XPATH, "//li/a[normalize-space()='FOO']").click()
                    time.sleep(1)

                    # PG01
                    agencyProcessingCode = driver.find_element(By.XPATH,
                                                               "//label[normalize-space()='Agency Processing Code:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic']")
                    agencyProcessingCode.click()
                    agencyProcessingCode.send_keys(FD1agencyProcessingCodeData)
                    time.sleep(2)
                    agencyProcessingCode.send_keys(Keys.ENTER)
                    time.sleep(1)

                    commercialDescription = driver.find_element(By.XPATH,
                                                                "//label[normalize-space()='Commercial Description:']//parent::div//following-sibling::div//input[@id='commercialDescription']")
                    commercialDescription.click()
                    commercialDescription.send_keys(FD1descriptionData)

                    pgaLineValue = driver.find_element(By.XPATH,
                                                       "//label[text()='PGA Line Value:']//parent::div//following-sibling::div//input[@name='pgaLineValue']")
                    pgaLineValue.send_keys(FD1pgaLineValueData)
                    time.sleep(2)

                    # PG19,20
                    addEntities = driver.find_element(By.XPATH, "//select[@id='entities']")

                    # FD1
                    addEntities.click()
                    selectFD1 = driver.find_element(By.XPATH, "//option[normalize-space()='FDA Importer 1 - FD1']")
                    selectFD1.click()
                    # DFP
                    selectDFP = driver.find_element(By.XPATH, "//option[normalize-space()='Owner - DFP']")
                    selectDFP.click()
                    # PNS
                    selectPNS = driver.find_element(By.XPATH, "//option[normalize-space()='PN Submitter - PNS']")
                    selectPNS.click()
                    # PNT
                    selectPNT = driver.find_element(By.XPATH, "//option[normalize-space()='PN Transmitter - PNT']")
                    selectPNT.click()
                    # FSV
                    selectFSV = driver.find_element(By.XPATH,
                                                    "//option[normalize-space()='Foreign Supplier Verification Program - FSV']")
                    selectFSV.click()
                    # PK
                    selectPK = driver.find_element(By.XPATH, "//option[normalize-space()='Point Of Contact - PK']")
                    selectPK.click()

                    mf = driver.find_element(By.XPATH,
                                             "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[1]")
                    mf.click()
                    mf.send_keys(FD1EntityMF)
                    time.sleep(2)
                    mf.send_keys(Keys.ENTER)

                    deq = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[2]")
                    deq.click()
                    deq.send_keys(FD1EntityDEQ)
                    time.sleep(2)
                    deq.send_keys(Keys.ENTER)

                    fd1 = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[3]")
                    fd1.click()
                    fd1.send_keys(FD1EntityFD1)
                    time.sleep(2)
                    fd1.send_keys(Keys.ARROW_DOWN)
                    fd1.send_keys(Keys.ENTER)

                    dfp = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[4]")
                    dfp.click()
                    dfp.send_keys(FD1EntityDFP)
                    time.sleep(2)
                    dfp.send_keys(Keys.ARROW_DOWN)
                    dfp.send_keys(Keys.ENTER)

                    pns = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[5]")
                    pns.click()
                    pns.send_keys(FD1EntityPNS)
                    time.sleep(2)
                    pns.send_keys(Keys.ENTER)

                    pnt = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[6]")
                    pnt.click()
                    pnt.send_keys(FD1EntityPNT)
                    time.sleep(2)
                    pnt.send_keys(Keys.ENTER)

                    uc = driver.find_element(By.XPATH,
                                             "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[7]")
                    uc.click()
                    uc.send_keys(FD1EntityUC)
                    time.sleep(2)
                    uc.send_keys(Keys.ARROW_DOWN)
                    uc.send_keys(Keys.ENTER)

                    fsv = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[8]")
                    fsv.click()
                    fsv.send_keys(FD1EntityFSV)
                    time.sleep(2)
                    fsv.send_keys(Keys.ENTER)

                    pk = driver.find_element(By.XPATH,
                                             "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[10]")
                    pk.click()
                    pk.send_keys(FD1EntityPK)
                    time.sleep(2)
                    pk.send_keys(Keys.ENTER)

                    time.sleep(2)

                    # PG21

                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Individual')])[1]").click()
                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Individual')])[1]").click()
                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Individual')])[1]").click()

                    individualQualifierTxt1 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[1]")
                    mailOrFaxTxt1 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[1]")
                    individualNameTxt1 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[1]")
                    telephoneNoTxt1 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[1]")

                    individualQualifierTxt1.click()
                    individualQualifierTxt1.send_keys(FD1individualQualifierData1)
                    time.sleep(2)
                    individualQualifierTxt1.send_keys(Keys.ENTER)
                    mailOrFaxTxt1.send_keys(FD1mailOrFaxData1)
                    individualNameTxt1.send_keys(FD1individualNameData1)
                    telephoneNoTxt1.send_keys(FD1telephoneNoData1)

                    individualQualifierTxt2 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[2]")
                    mailOrFaxTxt2 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[2]")
                    individualNameTxt2 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[2]")
                    telephoneNoTxt2 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[2]")

                    individualQualifierTxt2.click()
                    individualQualifierTxt2.send_keys(FD1individualQualifierData2)
                    time.sleep(2)
                    individualQualifierTxt2.send_keys(Keys.ENTER)
                    mailOrFaxTxt2.send_keys(FD1mailOrFaxData2)
                    individualNameTxt2.send_keys(FD1individualNameData2)
                    telephoneNoTxt2.send_keys(FD1telephoneNoData2)

                    individualQualifierTxt3 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[3]")
                    mailOrFaxTxt3 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[3]")
                    individualNameTxt3 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[3]")
                    telephoneNoTxt3 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[3]")

                    individualQualifierTxt3.click()
                    individualQualifierTxt3.send_keys(FD1individualQualifierData3)
                    time.sleep(2)
                    individualQualifierTxt3.send_keys(Keys.ENTER)
                    mailOrFaxTxt3.send_keys(FD1mailOrFaxData3)
                    individualNameTxt3.send_keys(FD1individualNameData3)
                    telephoneNoTxt3.send_keys(FD1telephoneNoData3)

                    individualQualifierTxt4 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[4]")
                    mailOrFaxTxt4 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[4]")
                    individualNameTxt4 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[4]")
                    telephoneNoTxt4 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[4]")

                    individualQualifierTxt4.click()
                    individualQualifierTxt4.send_keys(FD1individualQualifierData4)
                    time.sleep(2)
                    individualQualifierTxt4.send_keys(Keys.ENTER)
                    mailOrFaxTxt4.send_keys(FD1mailOrFaxData4)
                    individualNameTxt4.send_keys(FD1individualNameData4)
                    telephoneNoTxt4.send_keys(FD1telephoneNoData4)

                    # PG02
                    itemType = driver.find_element(By.XPATH,
                                                   "//label[text()='Item Type:']//parent::div//following-sibling::div/select[@name='itemType']")
                    time.sleep(1)
                    itemType.click()
                    itemType.send_keys(FD1itemTypeData)
                    time.sleep(2)
                    itemType.send_keys(Keys.ENTER)

                    productcodequalifier = driver.find_element(By.XPATH,
                                                               "//label[text()='Product Code Qualifier:']//parent::div//following-sibling::div/select[@name='productCodeQualifier']")
                    productcodequalifier.click()
                    time.sleep(1)
                    productcodequalifier.send_keys(FD1productcodequalifierData)
                    time.sleep(2)
                    productcodequalifier.send_keys(Keys.ENTER)

                    productcodnumber = driver.find_element(By.XPATH,
                                                           "//label[text()='Product Code Number:']//parent::div//following-sibling::div/input[@name='productCodeNumber']")
                    time.sleep(1)
                    productcodnumber.send_keys(FD1productcodnumberData)
                    time.sleep(2)
                    productcodnumber.send_keys(Keys.ENTER)
                    #
                    # PG26
                    packagingQualifier = driver.find_element(By.XPATH,
                                                             "//span[text()='Packaging Qualifier:']//parent::div//following-sibling::div/select[@name='packagingQualifier']")
                    packagingQualifier.click()
                    packagingQualifier.send_keys(FD1packagingQualifierData)
                    packagingQualifier.send_keys(Keys.ENTER)

                    unitOfMeasure = driver.find_element(By.XPATH,
                                                        "//span[text()='Unit of Measure:']//parent::div//following-sibling::div/input[@role='combobox']")
                    unitOfMeasure.send_keys(FD1unitOfMeasureData)
                    time.sleep(3)
                    unitOfMeasure.send_keys(Keys.ENTER)

                    pgaqty = driver.find_element(By.XPATH,
                                                 "//span[text()='Quantity:']//parent::div//following-sibling::div/input[@name='quantity' and@id='quantity' and @maxlength='12']")
                    pgaqty.send_keys(FD1pg26qtyData)

                    # PG04,05,06
                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Constituent')])[1]").click()

                    sourceTypeCodeTxt1 = driver.find_element(By.XPATH,
                                                             "(//label[text()='Source Type Code:']//parent::div//following-sibling::div/select[@name='sourceTypeCode'])[1]")
                    sourceTypeCodeTxt1.click()
                    sourceTypeCodeTxt1Option = driver.find_element(By.XPATH,
                                                                   "//option[normalize-space()='CSH - CSH - Country of Shipment']")
                    sourceTypeCodeTxt1Option.click()

                    specialUseDesignationTxt1 = driver.find_element(By.XPATH,
                                                                    "(//label[text()='Special Use Designation:']//parent::div//following-sibling::div/select[@name='specialUseDesignation'])[1]")
                    specialUseDesignationTxt1.click()
                    specialUseDesignationTxt1.send_keys(FD1SpecialUseDesignationData1)
                    specialUseDesignationTxt1.send_keys(Keys.ENTER)

                    countryCodeTxt1 = driver.find_element(By.XPATH,
                                                          "(//label[text()='Country Code:']//parent::div//following-sibling::div/input[@id='typeahead-basic'])[1]")
                    countryCodeTxt1.send_keys(FD1countryCodeData1)
                    time.sleep(2)
                    countryCodeTxt1.send_keys(Keys.ENTER)

                    specialUseDesignationTxt2 = driver.find_element(By.XPATH,
                                                                    "(//label[text()='Special Use Designation:']//parent::div//following-sibling::div/select[@name='specialUseDesignation'])[2]")
                    specialUseDesignationTxt2.click()
                    specialUseDesignationTxt2.send_keys(FD1SpecialUseDesignationData2)
                    specialUseDesignationTxt2.send_keys(Keys.ENTER)
                    sourceTypeCodeTxt2 = driver.find_element(By.XPATH,
                                                             "(//label[text()='Source Type Code:']//parent::div//following-sibling::div/select[@name='sourceTypeCode'])[2]")
                    sourceTypeCodeTxt2.click()
                    time.sleep(1)
                    sourceTypeCodeTxt2.send_keys(FD1sourceTypeCodeData2)
                    sourceTypeCodeTxt2.send_keys(Keys.ENTER)
                    countryCodeTxt2 = driver.find_element(By.XPATH,
                                                          "(//label[text()='Country Code:']//parent::div//following-sibling::div/input[@id='typeahead-basic'])[2]")
                    countryCodeTxt2.send_keys(FD1countryCodeData2)
                    time.sleep(2)
                    countryCodeTxt2.send_keys(Keys.ENTER)

                    # PG10
                    commodityCharacteristicDescription = driver.find_element(By.XPATH,
                                                                             "//span[text()='Commodity Characteristic Description:']//parent::div//following-sibling::div/input[@name='commodityCharacteristicDescription']")
                    commodityCharacteristicDescription.send_keys(FD1commodityCharDescripData)
                    time.sleep(2)

                    # PG23
                    AddNewInfo_Button = driver.find_element(By.XPATH,
                                                            "//app-affirmation-compliance-list[@class='p-2 ng-valid ng-touched ng-dirty']//button[contains(text(),'Add New Info')]")
                    AddNewInfo_Button.click()
                    AddNewInfo_Button.click()

                    afrmativecodeTxt1 = driver.find_element(By.XPATH, "(//select[@id='affirmationComplianceCode'])[1]")
                    afrmativecodeTxt1.click()
                    afrmativecodeTxt1.send_keys(FD1afrmativecodeData1)
                    afrmativecodeTxt1.send_keys(Keys.ENTER)
                    driver.find_element(By.XPATH, "(//input[@id='description'])[1]").send_keys(
                        FD1afrmativedescriptionData1)

                    afrmativecodeTxt2 = driver.find_element(By.XPATH, "(//select[@id='affirmationComplianceCode'])[2]")
                    afrmativecodeTxt2.click()
                    afrmativecodeTxt2.send_keys(FD1afrmativecodeData2)
                    afrmativecodeTxt2.send_keys(Keys.ENTER)
                    driver.find_element(By.XPATH, "(//input[@id='description'])[2]").send_keys(
                        FD1afrmativedescriptionData2)

                    afrmativecodeTxt3 = driver.find_element(By.XPATH, "(//select[@id='affirmationComplianceCode'])[3]")
                    afrmativecodeTxt3.click()
                    afrmativecodeTxt3.send_keys(FD1afrmativecodeData3)
                    afrmativecodeTxt3.send_keys(Keys.ENTER)
                    driver.find_element(By.XPATH, "(//input[@id='description'])[3]").send_keys(
                        FD1afrmativedescriptionData3)

                    # Opnen PG30
                    driver.find_element(By.XPATH,
                                        "//span[text()='Anticipated Arrival Information - PG30']//parent::div").click()
                    time.sleep(2)

                    inspectionLabTestingStatus = driver.find_element(By.XPATH,
                                                                     "//label[text()='Inspection/Lab Testing Status:']//parent::div//following-sibling::div/select[@name='inspectionTestingStatEntity']")
                    inspectionLabTestingStatus.click()
                    time.sleep(2)
                    inspectionLabTestingStatus.send_keys(FD1inspLabTestData)
                    inspectionLabTestingStatus.send_keys(Keys.ENTER)

                    scheduledTimeOfInspection = driver.find_element(By.XPATH,
                                                                    "//label[text()='Requested or Scheduled Time of Inspection; Time of previous Inspection; Arrival Time:']//parent::div//following-sibling::div/input[@name='scheduledTimeOfInspection']")
                    scheduledTimeOfInspection.send_keys(FD1schedTimeOfInspecData)

                    scheduledDateOfInspection = driver.find_element(By.XPATH,
                                                                    "//label[text()='Requested or Scheduled Date of Inspection; Date of previous Inspection; Arrival Date:']//parent::div//following-sibling::div//input[@name='scheduledDateInspection']")
                    scheduledDateOfInspection.send_keys(FD1scheduledDateOfInspectionData)

                    inspectionorArrivallocation = driver.find_element(By.XPATH,
                                                                      "//label[text()='Inspection or Arrival Location']//parent::div//following-sibling::div//input[@name='inspectionLocation']")
                    inspectionorArrivallocation.send_keys(FD1inspectionorArrivallocationData)

                    inspectionorArrivallocationCode = driver.find_element(By.XPATH,
                                                                          "//label[text()='Inspection or Arrival Location Code::']//parent::div//following-sibling::div/select[@name='arrivalLocationCode']")
                    inspectionorArrivallocationCode.click()
                    time.sleep(2)
                    inspectionorArrivallocationCode.send_keys(FD1inspectionorArrivallocationCodeData)

                    # PG27
                    driver.find_element(By.XPATH, "//input[@id='containerNumber']").send_keys(FD1containerNumberData)

                    # Check if values are fille in PGA or not
                    FD1Attributes = commercialDescription.get_attribute("value") and mf.get_attribute(
                        "value") and productcodequalifier.get_attribute("value")

                    saveAndClose = driver.find_element(By.XPATH, "//button[normalize-space()='Save & Close']")
                    saveAndClose.click()
                    time.sleep(2)

                    try:
                        alertDataIsValidMSG = driver.find_element(By.XPATH,
                                                                  "//div[normalize-space()='1. The Data is Valid...']")
                        if alertDataIsValidMSG:
                            alertDataIsValid = driver.find_element(By.XPATH,
                                                                   "//button[@type='button'][normalize-space()='Save & Close']")
                            alertDataIsValid.click()
                    except Exception as e:
                        print("Error while saving form")
                        logging.error("Error while saving form")

                    time.sleep(1)
                    try:
                        someValidationsError = driver.find_element(By.TAG_NAME, "body").text
                        if 'The Manufacturer record should have an entity number' in someValidationsError:
                            driver.find_element(By.XPATH,
                                                "//button[@type='button'][normalize-space()='Save & Close']").click()
                            time.sleep(1)
                            print("PGA has some validations issues but still PGA form saved")
                    except Exception as e:
                        print("PGA has issues and PGA form saved")
                        print(e)
                        time.sleep(1)
                    driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()
                    if FD1Attributes:
                        print("FD2 Filled")
                        logging.info("FD2 Filled")
                    maximizeQtySection = mywait.until(
                        EC.element_to_be_clickable((By.XPATH, "//button//span[normalize-space()=" + valhts + "]")))
                    maximizeQtySection.click()
                    time.sleep(1)

                # FD3

                FD3 = driver.find_elements(By.XPATH,
                                           "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='FD3']")
                if FD3:
                    driver.find_element(By.XPATH,
                                        "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='FD3']").click()
                    time.sleep(1)

                    # agency
                    driver.find_element(By.XPATH, "//li/a[normalize-space()='FOO']").click()
                    time.sleep(1)

                    # PG01
                    agencyProcessingCode = driver.find_element(By.XPATH,
                                                               "//label[normalize-space()='Agency Processing Code:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic']")
                    agencyProcessingCode.click()
                    agencyProcessingCode.send_keys(FD1agencyProcessingCodeData)
                    time.sleep(2)
                    agencyProcessingCode.send_keys(Keys.ENTER)
                    time.sleep(1)

                    commercialDescription = driver.find_element(By.XPATH,
                                                                "//label[normalize-space()='Commercial Description:']//parent::div//following-sibling::div//input[@id='commercialDescription']")
                    commercialDescription.click()
                    commercialDescription.send_keys(FD1descriptionData)

                    pgaLineValue = driver.find_element(By.XPATH,
                                                       "//label[text()='PGA Line Value:']//parent::div//following-sibling::div//input[@name='pgaLineValue']")
                    pgaLineValue.send_keys(FD1pgaLineValueData)
                    time.sleep(2)

                    # PG19,20
                    addEntities = driver.find_element(By.XPATH, "//select[@id='entities']")

                    # FD1
                    addEntities.click()
                    selectFD1 = driver.find_element(By.XPATH, "//option[normalize-space()='FDA Importer 1 - FD1']")
                    selectFD1.click()
                    # DFP
                    selectDFP = driver.find_element(By.XPATH, "//option[normalize-space()='Owner - DFP']")
                    selectDFP.click()
                    # PNS
                    selectPNS = driver.find_element(By.XPATH, "//option[normalize-space()='PN Submitter - PNS']")
                    selectPNS.click()
                    # PNT
                    selectPNT = driver.find_element(By.XPATH, "//option[normalize-space()='PN Transmitter - PNT']")
                    selectPNT.click()
                    # FSV
                    selectFSV = driver.find_element(By.XPATH,
                                                    "//option[normalize-space()='Foreign Supplier Verification Program - FSV']")
                    selectFSV.click()
                    # PK
                    selectPK = driver.find_element(By.XPATH, "//option[normalize-space()='Point Of Contact - PK']")
                    selectPK.click()

                    mf = driver.find_element(By.XPATH,
                                             "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[1]")
                    mf.click()
                    mf.send_keys(FD1EntityMF)
                    time.sleep(2)
                    mf.send_keys(Keys.ENTER)

                    deq = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[2]")
                    deq.click()
                    deq.send_keys(FD1EntityDEQ)
                    time.sleep(2)
                    deq.send_keys(Keys.ENTER)

                    fd1 = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[3]")
                    fd1.click()
                    fd1.send_keys(FD1EntityFD1)
                    time.sleep(2)
                    fd1.send_keys(Keys.ARROW_DOWN)
                    fd1.send_keys(Keys.ENTER)

                    dfp = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[4]")
                    dfp.click()
                    dfp.send_keys(FD1EntityDFP)
                    time.sleep(2)
                    dfp.send_keys(Keys.ARROW_DOWN)
                    dfp.send_keys(Keys.ENTER)

                    pns = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[5]")
                    pns.click()
                    pns.send_keys(FD1EntityPNS)
                    time.sleep(2)
                    pns.send_keys(Keys.ENTER)

                    pnt = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[6]")
                    pnt.click()
                    pnt.send_keys(FD1EntityPNT)
                    time.sleep(2)
                    pnt.send_keys(Keys.ENTER)

                    uc = driver.find_element(By.XPATH,
                                             "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[7]")
                    uc.click()
                    uc.send_keys(FD1EntityUC)
                    time.sleep(2)
                    uc.send_keys(Keys.ARROW_DOWN)
                    uc.send_keys(Keys.ENTER)

                    fsv = driver.find_element(By.XPATH,
                                              "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[8]")
                    fsv.click()
                    fsv.send_keys(FD1EntityFSV)
                    time.sleep(2)
                    fsv.send_keys(Keys.ENTER)

                    pk = driver.find_element(By.XPATH,
                                             "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[10]")
                    pk.click()
                    pk.send_keys(FD1EntityPK)
                    time.sleep(2)
                    pk.send_keys(Keys.ENTER)

                    time.sleep(2)

                    # PG21

                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Individual')])[1]").click()
                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Individual')])[1]").click()
                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Individual')])[1]").click()

                    individualQualifierTxt1 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[1]")
                    mailOrFaxTxt1 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[1]")
                    individualNameTxt1 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[1]")
                    telephoneNoTxt1 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[1]")

                    individualQualifierTxt1.click()
                    individualQualifierTxt1.send_keys(FD1individualQualifierData1)
                    time.sleep(2)
                    individualQualifierTxt1.send_keys(Keys.ENTER)
                    mailOrFaxTxt1.send_keys(FD1mailOrFaxData1)
                    individualNameTxt1.send_keys(FD1individualNameData1)
                    telephoneNoTxt1.send_keys(FD1telephoneNoData1)

                    individualQualifierTxt2 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[2]")
                    mailOrFaxTxt2 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[2]")
                    individualNameTxt2 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[2]")
                    telephoneNoTxt2 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[2]")

                    individualQualifierTxt2.click()
                    individualQualifierTxt2.send_keys(FD1individualQualifierData2)
                    time.sleep(2)
                    individualQualifierTxt2.send_keys(Keys.ENTER)
                    mailOrFaxTxt2.send_keys(FD1mailOrFaxData2)
                    individualNameTxt2.send_keys(FD1individualNameData2)
                    telephoneNoTxt2.send_keys(FD1telephoneNoData2)

                    individualQualifierTxt3 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[3]")
                    mailOrFaxTxt3 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[3]")
                    individualNameTxt3 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[3]")
                    telephoneNoTxt3 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[3]")

                    individualQualifierTxt3.click()
                    individualQualifierTxt3.send_keys(FD1individualQualifierData3)
                    time.sleep(2)
                    individualQualifierTxt3.send_keys(Keys.ENTER)
                    mailOrFaxTxt3.send_keys(FD1mailOrFaxData3)
                    individualNameTxt3.send_keys(FD1individualNameData3)
                    telephoneNoTxt3.send_keys(FD1telephoneNoData3)

                    individualQualifierTxt4 = driver.find_element(By.XPATH,
                                                                  "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[4]")
                    mailOrFaxTxt4 = driver.find_element(By.XPATH,
                                                        "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[4]")
                    individualNameTxt4 = driver.find_element(By.XPATH,
                                                             "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[4]")
                    telephoneNoTxt4 = driver.find_element(By.XPATH,
                                                          "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[4]")

                    individualQualifierTxt4.click()
                    individualQualifierTxt4.send_keys(FD1individualQualifierData4)
                    time.sleep(2)
                    individualQualifierTxt4.send_keys(Keys.ENTER)
                    mailOrFaxTxt4.send_keys(FD1mailOrFaxData4)
                    individualNameTxt4.send_keys(FD1individualNameData4)
                    telephoneNoTxt4.send_keys(FD1telephoneNoData4)

                    # PG02
                    itemType = driver.find_element(By.XPATH,
                                                   "//label[text()='Item Type:']//parent::div//following-sibling::div/select[@name='itemType']")
                    time.sleep(1)
                    itemType.click()
                    itemType.send_keys(FD1itemTypeData)
                    time.sleep(2)
                    itemType.send_keys(Keys.ENTER)

                    productcodequalifier = driver.find_element(By.XPATH,
                                                               "//label[text()='Product Code Qualifier:']//parent::div//following-sibling::div/select[@name='productCodeQualifier']")
                    productcodequalifier.click()
                    time.sleep(1)
                    productcodequalifier.send_keys(FD1productcodequalifierData)
                    time.sleep(2)
                    productcodequalifier.send_keys(Keys.ENTER)

                    productcodnumber = driver.find_element(By.XPATH,
                                                           "//label[text()='Product Code Number:']//parent::div//following-sibling::div/input[@name='productCodeNumber']")
                    time.sleep(1)
                    productcodnumber.send_keys(FD1productcodnumberData)
                    time.sleep(2)
                    productcodnumber.send_keys(Keys.ENTER)
                    #
                    # PG26
                    packagingQualifier = driver.find_element(By.XPATH,
                                                             "//span[text()='Packaging Qualifier:']//parent::div//following-sibling::div/select[@name='packagingQualifier']")
                    packagingQualifier.click()
                    packagingQualifier.send_keys(FD1packagingQualifierData)
                    packagingQualifier.send_keys(Keys.ENTER)

                    unitOfMeasure = driver.find_element(By.XPATH,
                                                        "//span[text()='Unit of Measure:']//parent::div//following-sibling::div/input[@role='combobox']")
                    unitOfMeasure.send_keys(FD1unitOfMeasureData)
                    time.sleep(3)
                    unitOfMeasure.send_keys(Keys.ENTER)

                    pgaqty = driver.find_element(By.XPATH,
                                                 "//span[text()='Quantity:']//parent::div//following-sibling::div/input[@name='quantity' and@id='quantity' and @maxlength='12']")
                    pgaqty.send_keys(FD1pg26qtyData)

                    # PG04,05,06
                    driver.find_element(By.XPATH, "(//button[contains(text(),'Add New Constituent')])[1]").click()

                    sourceTypeCodeTxt1 = driver.find_element(By.XPATH,
                                                             "(//label[text()='Source Type Code:']//parent::div//following-sibling::div/select[@name='sourceTypeCode'])[1]")
                    sourceTypeCodeTxt1.click()
                    sourceTypeCodeTxt1Option = driver.find_element(By.XPATH,
                                                                   "//option[normalize-space()='CSH - CSH - Country of Shipment']")
                    sourceTypeCodeTxt1Option.click()

                    specialUseDesignationTxt1 = driver.find_element(By.XPATH,
                                                                    "(//label[text()='Special Use Designation:']//parent::div//following-sibling::div/select[@name='specialUseDesignation'])[1]")
                    specialUseDesignationTxt1.click()
                    specialUseDesignationTxt1.send_keys(FD1SpecialUseDesignationData1)
                    specialUseDesignationTxt1.send_keys(Keys.ENTER)

                    countryCodeTxt1 = driver.find_element(By.XPATH,
                                                          "(//label[text()='Country Code:']//parent::div//following-sibling::div/input[@id='typeahead-basic'])[1]")
                    countryCodeTxt1.send_keys(FD1countryCodeData1)
                    time.sleep(2)
                    countryCodeTxt1.send_keys(Keys.ENTER)

                    specialUseDesignationTxt2 = driver.find_element(By.XPATH,
                                                                    "(//label[text()='Special Use Designation:']//parent::div//following-sibling::div/select[@name='specialUseDesignation'])[2]")
                    specialUseDesignationTxt2.click()
                    specialUseDesignationTxt2.send_keys(FD1SpecialUseDesignationData2)
                    specialUseDesignationTxt2.send_keys(Keys.ENTER)
                    sourceTypeCodeTxt2 = driver.find_element(By.XPATH,
                                                             "(//label[text()='Source Type Code:']//parent::div//following-sibling::div/select[@name='sourceTypeCode'])[2]")
                    sourceTypeCodeTxt2.click()
                    time.sleep(1)
                    sourceTypeCodeTxt2.send_keys(FD1sourceTypeCodeData2)
                    sourceTypeCodeTxt2.send_keys(Keys.ENTER)
                    countryCodeTxt2 = driver.find_element(By.XPATH,
                                                          "(//label[text()='Country Code:']//parent::div//following-sibling::div/input[@id='typeahead-basic'])[2]")
                    countryCodeTxt2.send_keys(FD1countryCodeData2)
                    time.sleep(2)
                    countryCodeTxt2.send_keys(Keys.ENTER)

                    # PG10
                    commodityCharacteristicDescription = driver.find_element(By.XPATH,
                                                                             "//span[text()='Commodity Characteristic Description:']//parent::div//following-sibling::div/input[@name='commodityCharacteristicDescription']")
                    commodityCharacteristicDescription.send_keys(FD1commodityCharDescripData)
                    time.sleep(2)

                    # PG23
                    AddNewInfo_Button = driver.find_element(By.XPATH,
                                                            "//app-affirmation-compliance-list[@class='p-2 ng-valid ng-touched ng-dirty']//button[contains(text(),'Add New Info')]")
                    AddNewInfo_Button.click()
                    AddNewInfo_Button.click()

                    afrmativecodeTxt1 = driver.find_element(By.XPATH, "(//select[@id='affirmationComplianceCode'])[1]")
                    afrmativecodeTxt1.click()
                    afrmativecodeTxt1.send_keys(FD1afrmativecodeData1)
                    afrmativecodeTxt1.send_keys(Keys.ENTER)
                    driver.find_element(By.XPATH, "(//input[@id='description'])[1]").send_keys(
                        FD1afrmativedescriptionData1)

                    afrmativecodeTxt2 = driver.find_element(By.XPATH, "(//select[@id='affirmationComplianceCode'])[2]")
                    afrmativecodeTxt2.click()
                    afrmativecodeTxt2.send_keys(FD1afrmativecodeData2)
                    afrmativecodeTxt2.send_keys(Keys.ENTER)
                    driver.find_element(By.XPATH, "(//input[@id='description'])[2]").send_keys(
                        FD1afrmativedescriptionData2)

                    afrmativecodeTxt3 = driver.find_element(By.XPATH, "(//select[@id='affirmationComplianceCode'])[3]")
                    afrmativecodeTxt3.click()
                    afrmativecodeTxt3.send_keys(FD1afrmativecodeData3)
                    afrmativecodeTxt3.send_keys(Keys.ENTER)
                    driver.find_element(By.XPATH, "(//input[@id='description'])[3]").send_keys(
                        FD1afrmativedescriptionData3)

                    # Opnen PG30
                    driver.find_element(By.XPATH,
                                        "//span[text()='Anticipated Arrival Information - PG30']//parent::div").click()
                    time.sleep(2)

                    inspectionLabTestingStatus = driver.find_element(By.XPATH,
                                                                     "//label[text()='Inspection/Lab Testing Status:']//parent::div//following-sibling::div/select[@name='inspectionTestingStatEntity']")
                    inspectionLabTestingStatus.click()
                    time.sleep(2)
                    inspectionLabTestingStatus.send_keys(FD1inspLabTestData)
                    inspectionLabTestingStatus.send_keys(Keys.ENTER)

                    scheduledTimeOfInspection = driver.find_element(By.XPATH,
                                                                    "//label[text()='Requested or Scheduled Time of Inspection; Time of previous Inspection; Arrival Time:']//parent::div//following-sibling::div/input[@name='scheduledTimeOfInspection']")
                    scheduledTimeOfInspection.send_keys(FD1schedTimeOfInspecData)

                    scheduledDateOfInspection = driver.find_element(By.XPATH,
                                                                    "//label[text()='Requested or Scheduled Date of Inspection; Date of previous Inspection; Arrival Date:']//parent::div//following-sibling::div//input[@name='scheduledDateInspection']")
                    scheduledDateOfInspection.send_keys(FD1scheduledDateOfInspectionData)

                    inspectionorArrivallocation = driver.find_element(By.XPATH,
                                                                      "//label[text()='Inspection or Arrival Location']//parent::div//following-sibling::div//input[@name='inspectionLocation']")
                    inspectionorArrivallocation.send_keys(FD1inspectionorArrivallocationData)

                    inspectionorArrivallocationCode = driver.find_element(By.XPATH,
                                                                          "//label[text()='Inspection or Arrival Location Code::']//parent::div//following-sibling::div/select[@name='arrivalLocationCode']")
                    inspectionorArrivallocationCode.click()
                    time.sleep(2)
                    inspectionorArrivallocationCode.send_keys(FD1inspectionorArrivallocationCodeData)

                    # PG27
                    driver.find_element(By.XPATH, "//input[@id='containerNumber']").send_keys(FD1containerNumberData)

                    # Check if values are fille in PGA or not
                    FD1Attributes = commercialDescription.get_attribute("value") and mf.get_attribute(
                        "value") and productcodequalifier.get_attribute("value")

                    saveAndClose = driver.find_element(By.XPATH, "//button[normalize-space()='Save & Close']")
                    saveAndClose.click()
                    time.sleep(2)

                    try:
                        alertDataIsValidMSG = driver.find_element(By.XPATH,
                                                                  "//div[normalize-space()='1. The Data is Valid...']")
                        if alertDataIsValidMSG:
                            alertDataIsValid = driver.find_element(By.XPATH,
                                                                   "//button[@type='button'][normalize-space()='Save & Close']")
                            alertDataIsValid.click()
                    except Exception as e:
                        print("Error while saving form")
                        logging.error("Error while saving form")

                    time.sleep(1)
                    try:
                        someValidationsError = driver.find_element(By.TAG_NAME, "body").text
                        if 'The Manufacturer record should have an entity number' in someValidationsError:
                            driver.find_element(By.XPATH,
                                                "//button[@type='button'][normalize-space()='Save & Close']").click()
                            time.sleep(1)
                            print("PGA has some validations issues but still PGA form saved")
                    except Exception as e:
                        print("PGA has issues and PGA form saved")
                        print(e)
                        time.sleep(1)
                    driver.find_element(By.XPATH, "//button[normalize-space()='OK']").click()
                    if FD1Attributes:
                        print("FD3 Filled")
                        logging.info("FD3 Filled")
                    maximizeQtySection = mywait.until(
                        EC.element_to_be_clickable((By.XPATH, "//button//span[normalize-space()=" + valhts + "]")))
                    maximizeQtySection.click()
                    time.sleep(1)

                # The below is neccessary if PGA available
                if EP5 or EP7 or FD1 or FD2 or FD3:
                    maximizeQtySection = mywait.until(
                        EC.element_to_be_clickable((By.XPATH, "//button//span[normalize-space()=" + valhts + "]")))
                    maximizeQtySection.click()

                # Add Cotton Quantity
                if invoicenoEx=="AB_1LCtnTC5_":
                    maximizeQtySection = mywait.until(EC.element_to_be_clickable((By.XPATH, "//button//span[normalize-space()=" + valhts + "]")))
                    maximizeQtySection.click()
                    CottonQty1=driver.find_element(By.XPATH, "(//input[@name='linevalue'])[2]")
                    CottonQty1.send_keys(htsqty1)
                    CottonQty2=driver.find_element(By.XPATH, "(//input[@name='linevalue'])[3]")
                    CottonQty2.send_keys(htsqty2)

                    DataFilledInCottonQuantity1 = CottonQty1.get_attribute("value")
                    DataFilledInCottonQuantity2 = CottonQty2.get_attribute("value")
                    if DataFilledInCottonQuantity1 and DataFilledInCottonQuantity2:
                        print("This is cotton HTS, Added Quantity: ",DataFilledInCottonQuantity1," and ",DataFilledInCottonQuantity2)

            except Exception as e:
                print(e)
                logging.error(e)

            DataFilledInLineAItem = tariffnotxt.get_attribute("value") and countryOfOriginText2.get_attribute("value") and countryOfExportText2.get_attribute("value")
            NumberOfLineItemsDone = driver.find_element(By.XPATH,"//button[@aria-expanded='true' and @class='btn btn-link']//div[2]").text

            # Add new Line Item
            addlineitembutton.click()

            if DataFilledInLineAItem:
                print("Line Item", NumberOfLineItemsDone, "Done")
            else:
                print("Line Item", NumberOfLineItemsDone, " Not Done")

        # Remove next line item if line items are greater than we want
        try:
            removeLineItem = mywait.until(EC.element_to_be_clickable((By.XPATH, "(//button[contains(text(),'Remove Line')])[" + str(lineitmscount + 1) + "]")))
            removeLineItem.click()
            print("Total Line Items are", lineitmscount)
            # logging.info("Total Line Items are", lineitmscount)
        except Exception as e:
            print(e)
            logging.error(e)

    except Exception as e:
        print(e)
        logging.error(e)
    # Save Form
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
    print("Test Case no : ", testCasesNumber, " End")
    # logging.info("Test Case no : ", testCasesNumber, " End")
    All = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "All")))
    All.click()
    time.sleep(1)
logoutButton = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
logoutButton.click()
time.sleep(1)
