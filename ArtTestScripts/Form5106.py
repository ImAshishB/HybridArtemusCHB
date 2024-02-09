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
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
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

def random_importerNameGenerator(size=4, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))
def random_importerNumberGenerator(size=9, chars=string.digits):
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
time.sleep(4)
driver.find_element(By.LINK_TEXT, "5106").click()
time.sleep(2)


# Select Importer
# for r in range(3, 4):
#     selectImporterData = utills.readData(file, "Sheet1", r, 140)
#     selectImporterTxt = mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='typeahead-basic']")))
#     selectImporterTxt.click()
#     selectImporterTxt.send_keys(selectImporterData)
#     time.sleep(2)
#     selectImporterTxt.send_keys(Keys.ENTER)

for r in range(11, 12):
    # i = 0
    # i = i - 1
    # #Login
    usern = utills.readData(file, "Sheet5106", r, 4)
    pasw = utills.readData(file, "Sheet5106", r, 5)

    # 5106 Data
    UtilizedforChckBoxData = utills.readData(file, "Sheet5106", r, 3)
    ImporterNameEx = utills.readData(file, "Sheet5106", r, 6)
    ImporterNameData = ImporterNameEx + random_importerNameGenerator()
    ImporterNumberEx = utills.readData(file, "Sheet5106", r, 7)
    ImporterNumberData = ImporterNumberEx + random_importerNumberGenerator()
    NameQualifierData = utills.readData(file, "Sheet5106", r, 8)
    AlternateImporterNameData = utills.readData(file, "Sheet5106", r, 9)
    OtherDescriptionData = utills.readData(file, "Sheet5106", r, 10)
    ImporterTypeData = utills.readData(file, "Sheet5106", r, 11)
    MailingAddressData = utills.readData(file, "Sheet5106", r, 12)
    Line1Data = utills.readData(file, "Sheet5106", r, 13)
    Line2Data = utills.readData(file, "Sheet5106", r, 14)
    ZipcodeData = utills.readData(file, "Sheet5106", r, 15)
    AddressTypeData = utills.readData(file, "Sheet5106", r, 16)
    cityData = utills.readData(file, "Sheet5106", r, 17)
    CountryCodeData = utills.readData(file, "Sheet5106", r, 18)
    StateData = utills.readData(file, "Sheet5106", r, 19)
    AddressExplanationData = utills.readData(file, "Sheet5106", r, 20)
    PhoneData = utills.readData(file, "Sheet5106", r, 21)
    EmailData = utills.readData(file, "Sheet5106", r, 22)

    # Open 5106 Form
    driver.find_element(By.XPATH, "//div[normalize-space()='Form 5106']").click()
    time.sleep(2)
    print("Form 5106 Opened")

    driver.find_element(By.ID, "importerName").send_keys(ImporterNameData)
    driver.find_element(By.ID, "importerNumber").send_keys(ImporterNumberData)

    QualifierDropdown = driver.find_element(By.ID, "nameQualifier")
    QualifierDropdown.click()
    QualifierDropdown.send_keys(NameQualifierData)
    QualifierDropdown.send_keys(Keys.ENTER)

    driver.find_element(By.ID, "alternateImporterName").send_keys(AlternateImporterNameData)

    ImporterType = driver.find_element(By.XPATH, "//select[@id='importerType']")
    ImporterType.click()
    ImporterType.send_keys(ImporterTypeData)
    ImporterType.send_keys(Keys.ENTER)

    # Utilized For
    IORCheck=driver.find_element(By.XPATH, "//input[@id='importerOfRecordUtilized']")
    IORCheck.click()
    ConsigneeCheck = driver.find_element(By.XPATH, "//input[@id='consigneeUtilized']")
    ConsigneeCheck.click()
    DrawbackCheck = driver.find_element(By.XPATH, "//input[@id='drawbackClaimant']")
    DrawbackCheck.click()
    RefundsCheck = driver.find_element(By.XPATH, "//input[@id='refundUtilized']")
    RefundsCheck.click()
    OthersCheck = driver.find_element(By.XPATH, "//input[@id='others']")
    OthersCheck.click()
    OthersDescriptionText = driver.find_element(By.XPATH, "//input[@id='otherUtilizationDescription']")
    OthersDescriptionText.send_keys(OtherDescriptionData)



    driver.find_element(By.ID, "lineOne").send_keys(Line1Data)
    driver.find_element(By.ID, "lineTwo").send_keys(Line2Data)
    driver.find_element(By.ID, "postalCode").send_keys(ZipcodeData)

    addressType = driver.find_element(By.ID, "addressType")
    addressType.click()
    addressType.send_keys(AddressTypeData)
    addressType.send_keys(Keys.ENTER)

    driver.find_element(By.ID, "state").send_keys(StateData)
    driver.find_element(By.ID, "city").send_keys(cityData)

    Country = driver.find_element(By.XPATH,
                                  "(//span[text()='Country Code:']//parent::div//following-sibling::div/input[@id='typeahead-basic'])[1]")
    Country.click()
    Country.send_keys(CountryCodeData)
    time.sleep(2)
    Country.send_keys(Keys.ENTER)

    driver.find_element(By.LINK_TEXT, "Copy Mailing Address to Physical Address").click()

    driver.find_element(By.ID, "phoneNumber").send_keys(PhoneData)

    driver.find_element(By.ID, "emailAddress").send_keys(EmailData)



    # Save Form
    saveButton = mywait.until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-outline-info'][normalize-space()='Save'])[1]")))
    saveButton.click()
    time.sleep(2)

    msg = driver.find_element(By.TAG_NAME, "body").text
    if 'Form Saved Successfully!' in msg:
        formSavedConfirmationMsgButton = driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
        formSavedConfirmationMsgButton.click()
        time.sleep(1)
        print("Form Saved Successfully")
    else:
        print("Form not Saved")

    All = mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "All")))
    All.click()
    time.sleep(1)
#l ogoutButton = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
# logoutButton.click()
# time.sleep(1)
