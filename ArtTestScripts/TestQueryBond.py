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
#
# serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options, service=serv_obj)
# mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
#                                                                          ElementNotVisibleException,
#                                                                          ElementNotSelectableException,
#                                                                          ElementClickInterceptedException,
#                                                                          ElementNotInteractableException,
#                                                                          Exception])
#
# # URL
# driver.get("http://52.54.244.138:8080/ArtemusChb/")
# # driver.get("https://chb.artemusgroupusa.com/")
# # Maximize page
# driver.maximize_window()
#
# # Login
# driver.find_element(By.ID, "username").send_keys("Ashishh")
# driver.find_element(By.ID, "password").send_keys("ashishh1")
# # driver.find_element(By.ID, "username").send_keys("Varada")
# # driver.find_element(By.ID, "password").send_keys("varada1")
# driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
#
# # HomePage
# query = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Queries")))
# query.click()
# time.sleep(1)
# Bond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Bond")))
# Bond.click()
# time.sleep(1)
#
# file = "D:\Artmus Spec\Automation_Artemus\querylist.xlsx"
# for r in range(3, 5):
#     QueryNo = utills.readData(file, "Sheet2", r, 12)
#     ImporterData = utills.readData(file, "Sheet2", r, 1)
#
#     # Query the imorter ID and record the query data
#     print("This is Query No: ", QueryNo)
#     importerOfRrecord = driver.find_element(By.XPATH, "//input[@id='importerNo']")
#     importerOfRrecord.clear()
#     importerOfRrecord.send_keys(ImporterData)
#
#     submitButton = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
#     submitButton.click()
#
#     SHORT_TIMEOUT = 1  # give time for the loading element to appear
#     LONG_TIMEOUT = 30  # give time for loading to finish
#     LOADING_ELEMENT_XPATH = "//body//app-root//app-loader//h3[@class='loadingScreen__text']"
#
#     try:
#         WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
#     except TimeoutException:
#         pass
#
#     # Record the Data found after query the Bond
#     try:
#         ImporterNumber = driver.find_element(By.XPATH,"//span[text()='Importer Number:']//parent::div//following-sibling::div").text
#         utills.writeData(file, "Sheet2", r, 2, ImporterNumber)
#     except:
#         pass
#     try:
#         ImporterName = driver.find_element(By.XPATH,"//span[text()='Importer’s Name:']//parent::div//following-sibling::div").text
#         utills.writeData(file, "Sheet2", r, 4, ImporterName)
#     except:
#         pass
#     try:
#         BondEffectiveDate = driver.find_element(By.XPATH,"//span[text()='Bond Effective Date:']//parent::div//following-sibling::div").text
#         utills.writeData(file, "Sheet2", r, 6, BondEffectiveDate)
#     except:
#         pass
#
#     try:
#         QueryResultsCode = driver.find_element(By.XPATH,"//span[text()='Query Results Code:']//parent::div//following-sibling::div").text
#         utills.writeData(file, "Sheet2", r, 8, QueryResultsCode)
#     except:
#         pass
#
#     try:
#         BondType = driver.find_element(By.XPATH,"//span[text()='Bond Type/Activity Code:']//parent::div//following-sibling::div").text
#         utills.writeData(file, "Sheet2", r, 10, BondType)
#     except:
#         pass
#
#     try:
#         centerIdentifier = driver.find_element(By.XPATH,"//span[text()='Center Identifier:']//parent::div//following-sibling::div").text
#         utills.writeData(file, "Sheet2", r, 9, centerIdentifier)
#     except:
#         pass
#
#     # Click to Create/Update Importer link
#     driver.find_element(By.XPATH, "//a[normalize-space()='Create/Update Importer']").click()
#     time.sleep(1)
#
#     # Record the Data found in Importer Screen
#     try:
#         ImporterNumberInImpScreen = driver.find_element(By.XPATH,"//div/input[@id='importerIdentityNumber']")
#         ImporterNumberInImpScreenData=ImporterNumberInImpScreen.get_attribute("value")
#         utills.writeData(file, "Sheet2", r, 3, ImporterNumberInImpScreenData)
#     except:
#         pass
#     try:
#         ImporterNameInImpScreen = driver.find_element(By.XPATH,"//div/input[@id='importerName']")
#         ImporterNameInImpScreenData=ImporterNameInImpScreen.get_attribute("value")
#         utills.writeData(file, "Sheet2", r, 5, ImporterNameInImpScreenData)
#     except:
#         pass
#     try:
#         BondEffectiveDateInImpScreen = driver.find_element(By.XPATH,"//div/input[@id='bondEffectiveDate']")
#         BondEffectiveDateInImpScreenData=BondEffectiveDateInImpScreen.get_attribute("value")
#         utills.writeData(file, "Sheet2", r, 7, BondEffectiveDateInImpScreenData)
#     except:
#         pass
#
#
#
#     # Print the values of the elements in console
#     try:
#         print("In Query:                     And                     Importer Screen: ")
#         print("Importer Name: ", ImporterName, "            Importer Name: ",ImporterNameInImpScreenData)
#         print("Importer Number: ", ImporterNumber, "            Importer Number: ",ImporterNumberInImpScreenData)
#         print("Bond Effective Date: ", BondEffectiveDate,          "            Bond Effective Date: ",BondEffectiveDateInImpScreenData)
#     except:
#         pass
#
#
#     try:
#         if BondEffectiveDateInImpScreen.get_attribute("value"):
#             utills.writeData(file, "Sheet2", r, 11, "Yes")
#         else:
#             utills.writeData(file, "Sheet2", r, 11, "No Bond Effective Date")
#         # if  ImporterName == ImporterNameInImpScreenData and ImporterNumber == ImporterNumberInImpScreenData and BondEffectiveDate == BondEffectiveDateInImpScreenData:
#         #     utills.writeData(file, "Sheet2", r, 11, "Name Mismatch")
#         # else:
#         #     utills.writeData(file, "Sheet2", r, 11, "Failed")
#
#
#     except Exception as e:
#         print(e)
#
#     # Close the Importer Screen
#
#     driver.find_element(By.XPATH, "//span[@aria-hidden='true']").click()
#     time.sleep(1)
#
#
#
#
#
#
#
#
































#
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
#
# serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# driver = webdriver.Chrome(options=options, service=serv_obj)
# mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
#                                                                          ElementNotVisibleException,
#                                                                          ElementNotSelectableException,
#                                                                          ElementClickInterceptedException,
#                                                                          ElementNotInteractableException,
#                                                                          Exception])
#
# # URL
# driver.get("http://52.54.244.138:8080/ArtemusChb/")
# # driver.get("https://chb.artemusgroupusa.com/")
# # Maximize page
# driver.maximize_window()
#
# # Login
# driver.find_element(By.ID, "username").send_keys("Ashishh")
# driver.find_element(By.ID, "password").send_keys("ashishh1")
# # driver.find_element(By.ID, "username").send_keys("Varada")
# # driver.find_element(By.ID, "password").send_keys("varada1")
# driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
#
#
#
# file = "D:\Artmus Spec\Automation_Artemus\querylist.xlsx"
# for r in range(3, 41):
#     QueryNo = utills.readData(file, "Sheet2", r, 12)
#     ImporterData = utills.readData(file, "Sheet2", r, 1)
#
#     # HomePage
#     query = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Queries")))
#     query.click()
#     time.sleep(1)
#     Bond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Bond")))
#     Bond.click()
#     time.sleep(1)
#
#     # Query the imorter ID and record the query data
#     print("This is Query No: ", QueryNo)
#     importerOfRrecord = driver.find_element(By.XPATH, "//input[@id='importerNo']")
#     importerOfRrecord.clear()
#     importerOfRrecord.send_keys(ImporterData)
#
#     submitButton = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
#     submitButton.click()
#
#     SHORT_TIMEOUT = 1  # give time for the loading element to appear
#     LONG_TIMEOUT = 30  # give time for loading to finish
#     LOADING_ELEMENT_XPATH = "//body//app-root//app-loader//h3[@class='loadingScreen__text']"
#
#     try:
#         WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
#     except TimeoutException:
#         pass
#     time.sleep(1)
#
#     # Record the Data found after query the Bond
#     try:
#         ImporterNumber = driver.find_element(By.XPATH,"//span[text()='Importer Number:']//parent::div//following-sibling::div").text
#         utills.writeData(file, "Sheet2", r, 2, ImporterNumber)
#     except:
#         pass
#
#     try:
#         ImporterName = driver.find_element(By.XPATH,"//span[text()='Importer’s Name:']//parent::div//following-sibling::div").text
#         utills.writeData(file, "Sheet2", r, 4, ImporterName)
#     except:
#         pass
#
#     try:
#         try:
#             BondEffectiveDate = driver.find_element(By.XPATH,
#                                                     "(//span[text()='Bond Effective Date:'])[2]//parent::div//following-sibling::div").text
#             utills.writeData(file, "Sheet2", r, 6, BondEffectiveDate)
#         except:
#             BondEffectiveDate = driver.find_element(By.XPATH,
#                                                     "//span[text()='Bond Effective Date:']//parent::div//following-sibling::div").text
#             utills.writeData(file, "Sheet2", r, 6, BondEffectiveDate)
#             pass
#     except:
#         pass
#
#
#     # try:
#     #     QueryResultsCode = driver.find_element(By.XPATH,"//span[text()='Query Results Code:']//parent::div//following-sibling::div").text
#     #     utills.writeData(file, "Sheet2", r, 8, QueryResultsCode)
#     # except:
#     #     pass
#
#     try:
#         centerIdentifier = driver.find_element(By.XPATH,"//span[text()='Center Identifier:']//parent::div//following-sibling::div").text
#         utills.writeData(file, "Sheet2", r, 9, centerIdentifier)
#     except:
#         pass
#
#     try:
#         print("Importer Name In Query:			        ", ImporterName,"              Bond Effective Date In Query: ", BondEffectiveDate)
#     except:
#         pass
#     time.sleep(1)
#
#     # Click to Create/Update Importer link
#     try:
#         driver.find_element(By.XPATH, "//a[normalize-space()='Create/Update Importer']").click()
#         time.sleep(1)
#     except:
#         print("Create/Update Importer Link Not Found")
#         pass
#
#     time.sleep(1)
#     # driver.find_element(By.XPATH, "//a[normalize-space()='Create/Update Importer']").click()
#     # time.sleep(1)
#
#     # Record the Data found in Importer Screen
#     try:
#         ImporterNumberInImpScreen = driver.find_element(By.XPATH,"//div/input[@id='importerIdentityNumber']")
#         ImporterNumberInImpScreenData=ImporterNumberInImpScreen.get_attribute("value")
#         utills.writeData(file, "Sheet2", r, 3, ImporterNumberInImpScreenData)
#     except:
#         pass
#
#
#     try:
#         ImporterNameInImpScreen = driver.find_element(By.XPATH,"//div/input[@id='importerName']")
#         ImporterNameInImpScreenData=ImporterNameInImpScreen.get_attribute("value")
#         utills.writeData(file, "Sheet2", r, 5, ImporterNameInImpScreenData)
#     except:
#         pass
#     try:
#         BondEffectiveDateInImpScreen = driver.find_element(By.XPATH,"//div/input[@id='bondEffectiveDate']")
#         BondEffectiveDateInImpScreenData=BondEffectiveDateInImpScreen.get_attribute("value")
#         utills.writeData(file, "Sheet2", r, 7, BondEffectiveDateInImpScreenData)
#     except:
#         print("Bond Effective Date in Importer Screen Not Found")
#         utills.writeData(file, "Sheet2", r, 7, "Not Found")
#         pass
#     try:
#         print("Importer Name in Importer Screen:	    ",ImporterNameInImpScreenData,"              Bond Effective Date in Importer Screen: ",BondEffectiveDateInImpScreenData)
#     except:
#         pass
#
#
#     try:
#         if BondEffectiveDateInImpScreen.get_attribute("value"):
#             utills.writeData(file, "Sheet2", r, 11, "Yes")
#         else:
#             utills.writeData(file, "Sheet2", r, 11, "No Bond Effective Date")
#     except:
#         pass
#     time.sleep(1)
#
#     # Close the Importer Screen
#
#     try:
#         driver.find_element(By.XPATH, "//span[@aria-hidden='true']").click()
#         time.sleep(1)
#     except:
#         print("Importer Screen is not closed")
#         pass
#
#     time.sleep(1)
#
#
#     # Go to Importer Screen
#
#     try:
#         Importer = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Importer")))
#         Importer.click()
#         time.sleep(1)
#     except:
#         print("Importer Screen is not opened")
#         pass
#
#     time.sleep(1)
#
#
#     try:
#         WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
#     except:
#         pass
#
#     try:
#         searchImporter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='searchImporter']")))
#         searchImporter.click()
#         searchImporter.send_keys(ImporterData)
#         searchImporter.send_keys(Keys.ENTER)
#         time.sleep(1)
#     except:
#         print("Search Importer is not working")
#         pass
#
#     time.sleep(1)
#
#
#     try:
#         textInBody = driver.find_element(By.TAG_NAME, "body").text
#         if 'No Entry Found for' in textInBody:
#             ImporterNotFound = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
#             ImporterNotFound.click()
#             time.sleep(1)
#         else:
#             try:
#                 WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
#             except:
#                 pass
#
#             time.sleep(1)
#             editImporter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-edit']")))
#             editImporter.click()
#
#             time.sleep(1)
#             ImporterNameInEditImporterScreen = driver.find_element(By.XPATH, "//div/input[@id='importerName']")
#             ImporterNameInEditImporterScreenData = ImporterNameInEditImporterScreen.get_attribute("value")
#             utills.writeData(file, "Sheet2", r, 10, ImporterNameInEditImporterScreenData)
#             try:
#                 BondEffectiveDateInEditImporterScreen = driver.find_element(By.XPATH,"//div/input[@id='bondEffectiveDate']")
#                 BondEffectiveDateInEditImporterScreenData = BondEffectiveDateInEditImporterScreen.get_attribute("value")
#                 utills.writeData(file, "Sheet2", r, 13, BondEffectiveDateInEditImporterScreenData)
#             except:
#                 print("No Bond Effective Date in Edit Importer Screen")
#                 utills.writeData(file, "Sheet2", r, 13, "Not found")
#                 pass
#
#
#             print("Importer Name in Edit Importer Screen:	", ImporterNameInEditImporterScreenData,"             Bond Effective Date in Edit Importer Screen: ",BondEffectiveDateInEditImporterScreenData)
#
#             if BondEffectiveDateInEditImporterScreenData == BondEffectiveDateInImpScreenData:
#                 utills.writeData(file, "Sheet2", r, 14, "Passed")
#             else:
#                 utills.writeData(file, "Sheet2", r, 14, "Failed")
#     except Exception as e:
#         print(e)
#         time.sleep(1)
#     print("-----------------------------------------------------------------------------------------------")























































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

serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options, service=serv_obj)
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         ElementClickInterceptedException,
                                                                         ElementNotInteractableException,
                                                                         Exception])

# URL
# driver.get("http://52.54.244.138:8080/ArtemusChb/")
driver.get("https://chb.artemusgroupusa.com/")
# Maximize page
driver.maximize_window()

# Login
# driver.find_element(By.ID, "username").send_keys("Ashishh")
# driver.find_element(By.ID, "password").send_keys("ashishh1")
driver.find_element(By.ID, "username").send_keys("Varada")
driver.find_element(By.ID, "password").send_keys("varada1")
driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()



file = "D:\Artmus Spec\Automation_Artemus\querylist.xlsx"
for r in range(467, 491):
    QueryNo = utills.readData(file, "Sheet2", r, 10)
    ImporterData = utills.readData(file, "Sheet2", r, 1)

    # HomePage
    query = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Queries")))
    query.click()
    time.sleep(1)
    Bond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Bond")))
    Bond.click()
    time.sleep(1)

    # Query the imorter ID and record the query data
    print("This is Query No: ", QueryNo, "          ", ImporterData)

    importerOfRrecord = driver.find_element(By.XPATH, "//input[@id='importerNo']")
    importerOfRrecord.clear()
    importerOfRrecord.send_keys(ImporterData)

    submitButton = driver.find_element(By.XPATH, "//button[normalize-space()='Submit']")
    submitButton.click()

    SHORT_TIMEOUT = 1  # give time for the loading element to appear
    LONG_TIMEOUT = 30  # give time for loading to finish
    LOADING_ELEMENT_XPATH = "//body//app-root//app-loader//h3[@class='loadingScreen__text']"

    try:
        WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
    except TimeoutException:
        pass

    # Record the Data found after query the Bond

    try:
        ImporterNumber = driver.find_element(By.XPATH,"//span[text()='Importer Number:']//parent::div//following-sibling::div").text
        utills.writeData(file, "Sheet2", r, 2, ImporterNumber)
    except:
        pass

    try:
        ImporterName = driver.find_element(By.XPATH,"//span[text()='Importer’s Name:']//parent::div//following-sibling::div").text
        utills.writeData(file, "Sheet2", r, 4, ImporterName)
    except:
        pass

    try:
        BondEffectiveDate = driver.find_element(By.XPATH,"(//span[text()='Bond Effective Date:'])[4]//parent::div//following-sibling::div").text
        utills.writeData(file, "Sheet2", r, 7, BondEffectiveDate)
    except:
        pass
    try:
        BondEffectiveDate = driver.find_element(By.XPATH,"(//span[text()='Bond Effective Date:'])[3]//parent::div//following-sibling::div").text
        utills.writeData(file, "Sheet2", r, 7, BondEffectiveDate)
    except:
        pass

    try:
        BondEffectiveDate = driver.find_element(By.XPATH,"(//span[text()='Bond Effective Date:'])[2]//parent::div//following-sibling::div").text
        utills.writeData(file, "Sheet2", r, 7, BondEffectiveDate)
    except:
        pass
    try:
        BondEffectiveDate = driver.find_element(By.XPATH,"(//span[text()='Bond Effective Date:'])[1]//parent::div//following-sibling::div").text
        utills.writeData(file, "Sheet2", r, 7, BondEffectiveDate)
    except:
        print("Bond Effective Date In Query is not Found for this Bond")
        pass

    try:
        BondType = driver.find_element(By.XPATH,"//span[text()='Bond Type/Activity Code:']//parent::div//following-sibling::div").text
        utills.writeData(file, "Sheet2", r, 12, BondType)
        print("Bond Type/Activity Code In Query:				", BondType)
    except:
        pass

    try:
        BondSufficiencyIndicator = driver.find_element(By.XPATH,"//span[text()='Bond Sufficiency Indicator:']//parent::div//following-sibling::div").text
        utills.writeData(file, "Sheet2", r, 15, BondSufficiencyIndicator)
        print("Bond Sufficiency Indicator In Query:				", BondSufficiencyIndicator)
        if BondSufficiencyIndicator=="N":
            print("Bond Sufficiency Indicator In Query is N")
            utills.writeData(file, "Sheet2", r, 16, "Ala Ala N ala")
    except:
        pass



    try:
        print("Importer Name In Query:			        ", ImporterName,"              Bond Effective Date In Query:                 ", BondEffectiveDate)
    except:
        pass

    # Click to Create/Update Importer link
    try:
        driver.find_element(By.XPATH, "//a[normalize-space()='Create/Update Importer']").click()
        time.sleep(1)
    except:
        print("Create/Update Importer Link Not Found")
        pass

    # Record the Data found in Importer Screen
    try:
        ImporterNumberInImpScreen = driver.find_element(By.XPATH,"//div/input[@id='importerIdentityNumber']")
        ImporterNumberInImpScreenData=ImporterNumberInImpScreen.get_attribute("value")
        utills.writeData(file, "Sheet2", r, 3, ImporterNumberInImpScreenData)
    except:
        pass


    try:
        ImporterNameInImpScreen = driver.find_element(By.XPATH,"//div/input[@id='importerName']")
        ImporterNameInImpScreenData=ImporterNameInImpScreen.get_attribute("value")
        utills.writeData(file, "Sheet2", r, 5, ImporterNameInImpScreenData)
    except:
        pass
    try:
        BondEffectiveDateInImpScreen = driver.find_element(By.XPATH,"//div/input[@id='bondEffectiveDate']")
        BondEffectiveDateInImpScreenData=BondEffectiveDateInImpScreen.get_attribute("value")
        utills.writeData(file, "Sheet2", r, 8, BondEffectiveDateInImpScreenData)
    except:
        print("Bond Effective Date in Importer Screen Not Found")
        utills.writeData(file, "Sheet2", r, 8, "Bond Effective Date Not Found")
        pass

    try:
        BondTypeInImpScreenDRP = driver.find_element(By.XPATH,"//select[@id='bondType']")
        BondTypeInImpScreen = driver.find_element(By.CSS_SELECTOR,"option:selected")
        BondTypeInImpScreenData = BondTypeInImpScreen.get_attribute("value")
        utills.writeData(file, "Sheet2", r, 13, BondTypeInImpScreenData)
    except:
        pass
    try:
        print("Importer Name in Importer Screen:	    ",ImporterNameInImpScreenData,"              Bond Effective Date in Importer Screen:       ",BondEffectiveDateInImpScreenData)
    except:
        pass


    # Close the Importer Screen

    try:
        driver.find_element(By.XPATH, "//span[@aria-hidden='true']").click()
        time.sleep(1)
    except:
        print("Importer Screen is not closed")
        pass


    # Go to Importer Screen

    try:
        Importer = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Importer")))
        Importer.click()
        time.sleep(1)
    except:
        print("Importer Screen is not opened")
        pass


    try:
        WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
    except:
        pass

    try:
        searchImporter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='searchImporter']")))
        searchImporter.click()
        searchImporter.send_keys(ImporterData)
        searchImporter.send_keys(Keys.ENTER)
        time.sleep(1)
    except:
        print("Search Importer is not working")
        pass

    time.sleep(1)


    try:
        textInBody = driver.find_element(By.TAG_NAME, "body").text
        if 'No Entry Found for' in textInBody:
            ImporterNotFound = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
            ImporterNotFound.click()
            time.sleep(1)
        else:
            try:
                WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
            except:
                pass
            editImporter = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[@class='fa fa-edit']")))
            editImporter.click()
            time.sleep(1)

            ImporterNameInEditImporterScreen = driver.find_element(By.XPATH, "//div/input[@id='importerName']")
            ImporterNameInEditImporterScreenData = ImporterNameInEditImporterScreen.get_attribute("value")
            utills.writeData(file, "Sheet2", r, 6, ImporterNameInEditImporterScreenData)

            try:
                BondTypeInEditImpScreen = driver.find_element(By.XPATH, "//select[@id='bondType']")
                BondTypeInEditImpScreenData = BondTypeInEditImpScreen.get_attribute("value")
                utills.writeData(file, "Sheet2", r, 14, BondTypeInEditImpScreenData)
            except:
                pass

            try:
                BondEffectiveDateInEditImporterScreen = driver.find_element(By.XPATH,"//div/input[@id='bondEffectiveDate']")
                BondEffectiveDateInEditImporterScreenData = BondEffectiveDateInEditImporterScreen.get_attribute("value")
                utills.writeData(file, "Sheet2", r, 9, BondEffectiveDateInEditImporterScreenData)
            except:
                print("No Bond Effective Date in Edit Importer Screen")
                utills.writeData(file, "Sheet2", r, 9, "Not found")
                pass


            print("Importer Name in Edit Importer Screen:	", ImporterNameInEditImporterScreenData,"              Bond Effective Date in Edit Importer Screen:  ",BondEffectiveDateInEditImporterScreenData)
    except Exception as e:
        print(e)
        time.sleep(1)
    print("-----------------------------------------------------------------------------------------------")





































































