# # In this Script, script will be record errors and will be continuing for next script.
# import logging
# import datetime
# from selenium import webdriver
# from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
#     ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException, TimeoutException
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
# #logging.basicConfig(filename="Art_7501_1Entry", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')
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
#
# # Maximize page
# driver.maximize_window()
# file = "D:\Artmus Spec\Automation_Artemus\TestML.xlsx"
# rows = utills.getRowCount(file, "Sheet1")
# coloumns = utills.getColumnCount(file, "Sheet1")
#
# def random_SRNGenerator(size=4, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))
# def random_BillGenerator(size=6, chars=string.ascii_uppercase + string.digits):
#     return ''.join(random.choice(chars) for x in range(size))
#
#
#
# usern = "Ashishh"
# pasw = "ashishh1"
# invoicenoData = "AB_SRN_" + random_SRNGenerator()
#
#     # Login
# login_username = mywait.until(EC.element_to_be_clickable((By.ID, "username")))
# login_username.click()
# login_username.send_keys(usern)
# login_password = mywait.until(EC.element_to_be_clickable((By.ID, "password")))
# login_password.click()
# login_password.send_keys(pasw)
# driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
# print("Login Done")
#
# # Wait till page loading stops
# SHORT_TIMEOUT = 1  # give time for the loading element to appear
# LONG_TIMEOUT = 30  # give time for loading to finish
# LOADING_ELEMENT_XPATH = "//body//app-root//app-loader//h3[@class='loadingScreen__text']"
# try:
#     WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
# except TimeoutException:
#     pass
#
# # HomePage
# AESLink = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "AES")))
# AESLink.click()
# time.sleep(2)
#
# AESDirectLink = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "AES Direct")))
# AESDirectLink.click()
# time.sleep(1)
# print("AES Direct Form opened")
#
# # Data
# emailData = "ashishbisen4@gmail.com"
# SRNData = random_SRNGenerator
# # Fill the form
# emailTxt = driver.find_element(By.ID, "emailResponseAddress")
# emailTxt.send_keys()







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

# Configure logger

logging.basicConfig(filename="Art_AES_MEntry", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', filemode='w')
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
rows = utills.getRowCount(file, "AESDataSheet")
coloumns = utills.getColumnCount(file, "AESDataSheet")


def random_SRNGenerator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))
def random_emailGenerator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_TRNGenerator(size=4, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


    # Login
login_username = mywait.until(EC.element_to_be_clickable((By.ID, "username")))
login_username.click()
login_username.send_keys("Ashishh")
login_password = mywait.until(EC.element_to_be_clickable((By.ID, "password")))
login_password.click()
login_password.send_keys("ashishh1")
driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
print("Login Done")

# Wait till page loading stops
SHORT_TIMEOUT = 1  # give time for the loading element to appear
LONG_TIMEOUT = 30  # give time for loading to finish
LOADING_ELEMENT_XPATH = "//body//app-root//app-loader//h3[@class='loadingScreen__text']"
try:
    WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
except TimeoutException:
    pass


AESLink = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "AES")))
AESLink.click()
time.sleep(1)

for r in range(3, 4):
    i = 0
    i = i - 1

    # ----------------------------------
    # HomePage
    AESDirectLink = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "AES Direct")))
    AESDirectLink.click()
    time.sleep(1)

    #---------------------------------------------------------------------------------------------------------

    # Shipment Page

    try:
        print("AES Direct Form opened")
        print("Shipment Section opened")

        TCNoData = utills.readData(file, "AESDataSheet", r, 2)
        TCNameData = utills.readData(file, "AESDataSheet", r, 3)
        LineItemsData = utills.readData(file, "AESDataSheet", r, 4)
        emailExl = utills.readData(file, "AESDataSheet", r, 8)
        emailData = emailExl + random_emailGenerator() + "@gmail.com"
        SRNExl = utills.readData(file, "AESDataSheet", r, 9)
        SRNData = SRNExl + random_SRNGenerator()
        filingOptionDrpData = utills.readData(file, "AESDataSheet", r, 10)
        MOTDrpData = utills.readData(file, "AESDataSheet", r, 11)
        portOfxportTPData = utills.readData(file, "AESDataSheet", r, 12)
        portofUnladingData = utills.readData(file, "AESDataSheet", r, 13)
        originStateData = utills.readData(file, "AESDataSheet", r, 15)
        countryOfDestinationData = utills.readData(file, "AESDataSheet", r, 16)
        inBondTypeData = utills.readData(file, "AESDataSheet", r, 17)
        FTZData = utills.readData(file, "AESDataSheet", r, 18)
        importEntryData = utills.readData(file, "AESDataSheet", r, 19)
        originalITNData = utills.readData(file, "AESDataSheet", r, 20)
        routedYNData = utills.readData(file, "AESDataSheet", r, 21)
        partyYNData = utills.readData(file, "AESDataSheet", r, 22)
        hzmatYNData = utills.readData(file, "AESDataSheet", r, 23)



        emailTxt = driver.find_element(By.ID, "emailResponseAddress")
        emailTxt.send_keys(emailData)

        srnTxt = driver.find_element(By.ID, "shipmentReferenceNumber")
        srnTxt.send_keys(SRNData)
        srnOutCLick = driver.find_element(By.XPATH, "//label[@for='shipmentReferenceNumber']")
        srnOutCLick.click()
        time.sleep(1)

        filingOptionDrp = driver.find_element(By.XPATH,"//select[@id='filingOption']")
        filingOptionDrp.send_keys(filingOptionDrpData)

        MOTDrp = driver.find_element(By.XPATH, "//select[@id='modeOfTransport']")
        MOTDrp.send_keys(MOTDrpData)

        portOfxportTPTxt = driver.find_element(By.ID, "portofExport")
        portOfxportTPTxt.click()
        portOfxportTPTxt.send_keys(portOfxportTPData)
        time.sleep(2)
        portOfxportTPTxt.send_keys(Keys.ENTER)
        time.sleep(1)

        portofUnladingTPTxt = driver.find_element(By.ID, "portofUnlading")
        portofUnladingTPTxt.click()
        portofUnladingTPTxt.send_keys(portofUnladingData)
        time.sleep(2)
        portofUnladingTPTxt.send_keys(Keys.ENTER)
        time.sleep(1)

        originStateDrp = driver.find_element(By.XPATH, "//select[@id='originState']")
        originStateDrp.send_keys(originStateData)

        countryOfDestinationTPTxt = driver.find_element(By.XPATH, "//label[@for='countryofDestination']//following-sibling::input[@id='typeahead-basic']")
        countryOfDestinationTPTxt.click()
        countryOfDestinationTPTxt.send_keys(countryOfDestinationData)
        time.sleep(2)
        countryOfDestinationTPTxt.send_keys(Keys.ENTER)
        time.sleep(1)

        inBondTypesDrp = driver.find_element(By.XPATH, "//select[@id='inbondType']")
        inBondTypesDrp.send_keys(inBondTypeData)

        if routedYNData == "Y":
            routedYes = driver.find_element(By.XPATH, "//input[@id='isRoutedTransactionYes']")
            routedYes.click()
        if routedYNData == "N":
            routedNo = driver.find_element(By.XPATH, "//input[@id='isRoutedTransactionNo']")
            routedNo.click()

        if partyYNData == "Y":
            partyYes = driver.find_element(By.XPATH, "(//input[@id='relatedCompanyIndicator'])[1]")
            partyYes.click()
        if partyYNData == "N":
            partyNo = driver.find_element(By.XPATH, "(//input[@id='relatedCompanyIndicator'])[2]")
            partyNo.click()

        if hzmatYNData == "Y":
            hazmatYes = driver.find_element(By.XPATH, "//input[@id='hazardousMaterialIndicatorYes']")
            hazmatYes.click()
        if hzmatYNData == "N":
            hazmatNo = driver.find_element(By.XPATH, "//input[@id='hazardousMaterialIndicatorNo']")
            hazmatNo.click()


        print("Shipment Section Done")

    except Exception as e:
        print(e)
        print("!! Shipment Section Not Done !!")

    # Go to Party Page
    try:
        goToPartySection = driver.find_element(By.XPATH, "//button[normalize-space()='Step 2: Parties']")
        goToPartySection.click()
    except:
        pass


    # Party Page
    try:
        print("Party Section opened")

        USPPIPartyData = utills.readData(file, "AESDataSheet", r, 24)
        UCPartyData = utills.readData(file, "AESDataSheet", r, 37)
        UCsoldEnRoutRadioData = utills.readData(file, "AESDataSheet", r, 38)
        UCconsigneeTypeData = utills.readData(file, "AESDataSheet", r, 39)
        ICPartyData = utills.readData(file, "AESDataSheet", r, 52)
        FFPartyData = utills.readData(file, "AESDataSheet", r, 65)

        #USPPI
        loadProfileLinkUSPPI = driver.find_element(By.XPATH, "(//a[contains(text(),'Load from Profile')])[1]")
        loadProfileLinkUSPPI.click()

        profileNameTxt = driver.find_element(By.XPATH,"//input[@id='profile']")
        profileNameTxt.click()
        profileNameTxt.send_keys(USPPIPartyData)
        time.sleep(2)
        profileNameTxt.send_keys(Keys.ENTER)
        time.sleep(1)

        loadProfileButtonUSPPI = driver.find_element(By.XPATH, "//button[normalize-space()='Load Profile']")
        loadProfileButtonUSPPI.click()


        #UC
        loadProfileLinkUSPPI = driver.find_element(By.XPATH, "(//a[contains(text(),'Load from Profile')])[2]")
        loadProfileLinkUSPPI.click()

        profileNameTxt = driver.find_element(By.XPATH,"//input[@id='profile']")
        profileNameTxt.click()
        profileNameTxt.send_keys(UCPartyData)
        time.sleep(2)
        profileNameTxt.send_keys(Keys.ENTER)
        time.sleep(1)

        loadProfileButtonUSPPI = driver.find_element(By.XPATH, "//button[normalize-space()='Load Profile']")
        loadProfileButtonUSPPI.click()

        if UCsoldEnRoutRadioData == "Y":
            SoldEnRoutYes = driver.find_element(By.XPATH, "//input[@id='soldEnRouteYes']")
            SoldEnRoutYes.click()
        if UCsoldEnRoutRadioData == "N":
            SoldEnRoutNo = driver.find_element(By.XPATH, "//input[@id='soldEnRouteNo']")
            SoldEnRoutNo.click()

        consigneeTypeOptionDrp = driver.find_element(By.XPATH, "//select[@id='consigneeType']")
        consigneeTypeOptionDrp.send_keys(UCconsigneeTypeData)



        



        # #IC
        # loadProfileLinkUSPPI = driver.find_element(By.XPATH, "(//a[contains(text(),'Load from Profile')])[3]")
        # loadProfileLinkUSPPI.click()
        #
        # profileNameTxt = driver.find_element(By.XPATH,"//input[@id='profile']")
        # profileNameTxt.click()
        # profileNameTxt.send_keys(ICPartyData)
        # time.sleep(2)
        # profileNameTxt.send_keys(Keys.ENTER)
        # time.sleep(1)
        #
        # loadProfileButtonUSPPI = driver.find_element(By.XPATH, "//button[normalize-space()='Load Profile']")
        # loadProfileButtonUSPPI.click()
        #
        #
        #FF
        loadProfileLinkUSPPI = driver.find_element(By.XPATH, "(//a[contains(text(),'Load from Profile')])[4]")
        loadProfileLinkUSPPI.click()

        profileNameTxt = driver.find_element(By.XPATH,"//input[@id='profile']")
        profileNameTxt.click()
        profileNameTxt.send_keys(FFPartyData)
        time.sleep(2)
        profileNameTxt.send_keys(Keys.ENTER)
        time.sleep(1)

        loadProfileButtonUSPPI = driver.find_element(By.XPATH, "//button[normalize-space()='Load Profile']")
        loadProfileButtonUSPPI.click()

        print("Party Section Done")

    except Exception as e:
        print(e)
        print("!! Party Section not Done !!")


    # Go to Commodity page
    try:
        goToCommoditySection = driver.find_element(By.XPATH,"//button[normalize-space()='Step 3: Commodities']")
        goToCommoditySection.click()
    except:
        pass

    # Commodity Page
    try:
        print("Commodity Section opened")

        lineItemData = utills.readData(file, "AESDataSheet", r, 4).split(",")
        ExportInformationCodeDrpData = utills.readData(file, "AESDataSheet", r, 82).split(",")
        HTSNUmberData = utills.readData(file, "AESDataSheet", r, 83).split(",")
        HTSQty1Data = utills.readData(file, "AESDataSheet", r, 84).split(",")
        HTSQty2Data = utills.readData(file, "AESDataSheet", r, 85).split(",")
        originOfGoodsData = utills.readData(file, "AESDataSheet", r, 86).split(",")
        valueOfGoodsData = utills.readData(file, "AESDataSheet", r, 87).split(",")
        shippingWeightData = utills.readData(file, "AESDataSheet", r, 88).split(",")
        ECCNData = utills.readData(file, "AESDataSheet", r, 89)
        licenseTypeData = utills.readData(file, "AESDataSheet", r, 90).split(",")


        ExportInformationCodeDrp = driver.find_element(By.XPATH, "//select[@id='exportInfoCode-0']")
        HTSNUmberTxt = driver.find_element(By.XPATH,"//input[@id='typeahead-basic' and @placeholder='Type Schedule B or HTS Number']")
        HTSQty1Txt = driver.find_element(By.XPATH, "//input[@id='firstQty-0']")
        HTSQty2Txt = driver.find_element(By.XPATH, "//input[@id='secondQty-0']")
        originOfGoodsTxt = driver.find_element(By.XPATH, "//select[@id='originOfGoods-0']")
        valueOfGoodsTxt = driver.find_element(By.XPATH, "//input[@id='valueOfGoods-0']")
        shippingWeightTxt = driver.find_element(By.XPATH, "//input[@id='shippingWeight']")
        licenseTypeTxt = driver.find_element(By.XPATH, "//select[@id='licenseExemptionTypeCode-0']")
        AddLineBtn = driver.find_element(By.XPATH, "//button[normalize-space()='Add New Line']")
        RemoveLineBtn = driver.find_element(By.XPATH, "//button[normalize-space()='Delete Line']")
        for valExportInformationCodeDrpData, valHTSNUmberData, valHTSQty1Data, valHTSQty2Data, valoriginOfGoodsData, valvalueOfGoodsData, valshippingWeightData, vallicenseTypeData in zip(ExportInformationCodeDrpData, HTSNUmberData,
                                                                              HTSQty1Data, HTSQty2Data, originOfGoodsData, valueOfGoodsData, shippingWeightData, licenseTypeData):


            ExportInformationCodeDrp.send_keys(valExportInformationCodeDrpData)

            HTSNUmberTxt.click()
            HTSNUmberTxt.send_keys(valHTSNUmberData)
            time.sleep(2)
            HTSNUmberTxt.send_keys(Keys.ENTER)
            time.sleep(1)

            HTSQty1Txt.send_keys(valHTSQty1Data)

            # HTSQty2Txt.send_keys(valHTSQty2Data)

            originOfGoodsTxt.send_keys(valoriginOfGoodsData)

            valueOfGoodsTxt.send_keys(valvalueOfGoodsData)


            shippingWeightTxt.send_keys(valshippingWeightData)

            licenseTypeTxt.send_keys(vallicenseTypeData)

            AddLineBtn.click()

        RemoveLineBtn.click()

        print("Commodity Section done")

    except Exception as e:
        print(e)
        logging.error(e)
        print("!! Commodity Section not done !!")

    # Go to Transportation

    try:
        goToTransportationSection = driver.find_element(By.XPATH,"//button[normalize-space()='Step 4: Transportation']")
        goToTransportationSection.click()
    except:
        pass

    # Transportation Page
    try:
        print("Transport Section opened")

        ScacCodeData = utills.readData(file, "AESDataSheet", r, 102)
        ConvencyNameData = utills.readData(file, "AESDataSheet", r, 103)
        TRNExl = utills.readData(file, "AESDataSheet", r, 104)
        TrasnportationNoData = TRNExl + random_SRNGenerator()

        ScacCodeTxt = driver.find_element(By.XPATH, "//label[@for='carrierId']//following-sibling::input[@id='typeahead-basic']")
        ScacCodeTxt.click()
        ScacCodeTxt.send_keys(ScacCodeData)
        time.sleep(2)
        ScacCodeTxt.send_keys(Keys.ENTER)
        time.sleep(1)

        ConvencyNameTxt = driver.find_element(By.XPATH,"//input[@id='conveyanceName']")
        ConvencyNameTxt.send_keys(ConvencyNameData)

        TrasnportationNoTxt = driver.find_element(By.XPATH, "//input[@id='transportationrefNumber']")
        TrasnportationNoTxt.send_keys(TrasnportationNoData)

        print("Transport Section done")

    except Exception as e:
        print(e)
        logging.error(e)
        print("!! Transport Section not done !!")




    # # Save Form
    # try:
    #     saveButton = mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Save']")))
    #     saveButton.click()
    #     time.sleep(2)
    #
    #     msg = driver.find_element(By.TAG_NAME, "body").text
    #
    #     if 'Form saved successfully' in msg:
    #         formSavedConfirmationMsgButton = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
    #         formSavedConfirmationMsgButton.click()
    #         time.sleep(2)
    #         print("Form Saved Successfully")
    #         # logoutButton = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
    #         # logoutButton.click()
    #     else:
    #         driver.save_screenshot(".\\screenshots\\" + "testing_scr.png")  # Screenshot
    #         print("!! Failed to save the form !!")
    #         # logoutButton = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
    #         # logoutButton.click()
    #
    # except:
    #     pass
    #
    #
    #
    # All = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "All")))
    # All.click()
    # time.sleep(1)
# logoutButton = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
# logoutButton.click()
# time.sleep(1)
