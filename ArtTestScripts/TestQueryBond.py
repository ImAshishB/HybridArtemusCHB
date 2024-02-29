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
driver.get("http://52.54.244.138:8080/ArtemusChb/")
# driver.get("https://chb.artemusgroupusa.com/")
# Maximize page
driver.maximize_window()

# Login
driver.find_element(By.ID, "username").send_keys("Ashishh")
driver.find_element(By.ID, "password").send_keys("ashishh1")
# driver.find_element(By.ID, "username").send_keys("Varada")
# driver.find_element(By.ID, "password").send_keys("varada1")
driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()

# HomePage
query = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Queries")))
query.click()
time.sleep(1)
Bond = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Bond")))
Bond.click()
time.sleep(1)

file = "D:\Artmus Spec\Automation_Artemus\querylist.xlsx"
for r in range(3, 4):
    ImporterData = utills.readData(file, "Sheet2", r, 1)

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
    try:
        ImporterNumber = driver.find_element(By.XPATH,"//span[text()='Importer Number:']//parent::div//following-sibling::div").text
        # utills.writeData(file, "Sheet2", r, 2, ImporterNumber)
    except:
        pass
    try:
        ImporterName = driver.find_element(By.XPATH,"//span[text()='Importer’s Name:']//parent::div//following-sibling::div").text
        # utills.writeData(file, "Sheet2", r, 3, ImporterName)
    except:
        pass
    try:
        BondEffectiveDate = driver.find_element(By.XPATH,"//span[text()='Bond Effective Date:']//parent::div//following-sibling::div").text
        # utills.writeData(file, "Sheet2", r, 4, BondEffectiveDate)
    except:
        pass
    try:
        ImporterScreenBondEffectiveDate = driver.find_element(By.XPATH,"").text
        # utills.writeData(file, "Sheet2", r, 5, ImporterScreenBondEffectiveDate)
    except:
        pass
    # try:
    #     QueryResultsCode = driver.find_element(By.XPATH,"//span[text()='Query Results Code:']//parent::div//following-sibling::div").text
    #     utills.writeData(file, "Sheet2", r, 6, QueryResultsCode)
    # except:
    #     pass
    #
    # try:
    #     BondType = driver.find_element(By.XPATH,"//span[text()='Bond Type/Activity Code:']//parent::div//following-sibling::div").text
    #     utills.writeData(file, "Sheet2", r, 7, BondType)
    # except:
    #     pass
    #
    # try:
    #     BondNumber = driver.find_element(By.XPATH,"//span[text()='Bond Number:']//parent::div//following-sibling::div").text
    #     utills.writeData(file, "Sheet2", r, 8, BondNumber)
    # except:
    #     pass
    # try:
    #     centerIdentifier = driver.find_element(By.XPATH,"//span[text()='Center Identifier:']//parent::div//following-sibling::div").text
    #     utills.writeData(file, "Sheet2", r, 9, centerIdentifier)
    # except:
    #     pass

    driver.find_element(By.XPATH,"//a[normalize-space()='Create/Update Importer']").click()
    time.sleep(1)


    try:
        FilerCode= driver.find_element(By.XPATH,"//span[text()='Filer Code :']//parent::div//following-sibling::div/input[@id='entryFilerCode']")
        ss=FilerCode.get_attribute("value")
        print(ss)
        # sss=FilerCode.get_attribute("name")
        # utills.writeData(file, "Sheet2", r, 8, FilerCode)
        # print(sss)
    except:
        pass

    driver.find_element(By.XPATH, "//span[@aria-hidden='true']").click()
    time.sleep(1)

