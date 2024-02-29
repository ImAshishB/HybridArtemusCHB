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
file = "D:\Artmus Spec\Automation_Artemus\querylist.xlsx"
# HomePage
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

try:
    WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
except TimeoutException:
    pass
# Select Importer
selectImporterTxt = mywait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='typeahead-basic']")))
selectImporterTxt.click()
selectImporterTxt.send_keys("arttest")
time.sleep(2)
selectImporterTxt.send_keys(Keys.ENTER)
time.sleep(2)
nextarroro=driver.find_element(By.XPATH, "//i[@class='fa fa-arrow-circle-o-right fa-2x']")
rowsCount=len(driver.find_elements(By.XPATH, "//table/tbody/tr")) # count number of rows
colsCount=len(driver.find_elements(By.XPATH, "//table/thead/tr/th")) # count number of coloumns

print("Total number of rows are:",rowsCount)
print("Total number of coloumns are:",colsCount)

for r in range(1, rowsCount + 1):
    for c in range(1, colsCount + 1):
        values = driver.find_element(By.XPATH, "//table/tbody/tr[" + str(r) + "]/td[" + str(c) + "]").text
        print(values)
        utills.writeData(file, "Sheet3", r, c, values)
driver.close()
# a = 4
# for _ in range(a):
#
#     nextarroro.click()
#     try:
#         WebDriverWait(driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
#     except TimeoutException:
#         pass

