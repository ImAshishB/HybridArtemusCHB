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



# file = "D:\Artmus Spec\Automation_Artemus\querylist.xlsx"
# for r in range(1, 6):
#     ImporterData = utills.readData(file, "Sheet3", r, 1)
#     print(ImporterData)

    # try:
    #     ImporterNumber = driver.find_element(By.XPATH,"//span[text()='Importer Number:']//parent::div//following-sibling::div").text
    #     print(ImporterNumber)
    #     utills.writeData(file, "Sheet3", r, 2, ImporterNumber)
    # except:
    #     pass

a = 4
for _ in range(a):
    print("Ashish")