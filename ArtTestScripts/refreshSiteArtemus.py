


# from selenium import webdriver
# from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
#     ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException
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
# mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions= [NoSuchElementException,
#                                                                          ElementNotVisibleException,
#                                                                          ElementNotSelectableException,
#                                                                          ElementClickInterceptedException,
#                                                                          ElementNotInteractableException,
#                                                                          Exception])
#
# # URL
# driver.get("http://52.54.244.138:8080/ArtemusChb/")
# # Maximize page
# driver.maximize_window()
#
# #Login
# driver.find_element(By.ID, "username").send_keys("tnash")
# driver.find_element(By.ID, "password").send_keys("tnash1")
# driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()
#
# #HomePage
# query = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.LINK_TEXT, "Queries")))
# query.click()
# misc = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT,"Miscellaneous")))
# misc.click()
# tariffquery = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//span[normalize-space()='Tariff Query']")))
# tariffquery.click()
# file="D:\Artmus Spec\Automation_Artemus\querylist.xlsx"
# rows=utills.getRowCount(file,"Sheet1")
#
#
# for r in range(2,3):
#     htsno=utills.readData(file,"Sheet1",r,1).split(",")
#
#     for val1 in zip(htsno):
#
#         # clear input
#         htsInput=driver.find_element(By.ID, "HTSUSNo")
#         htsInput.clear()
#
#         # Click on outline of input
#         htsOutClick = driver.find_element(By.XPATH,"//span[normalize-space()='HTSUS:']")
#         htsOutClick.click()
#
#         # Send value
#         htsInput.send_keys(val1)
#
#         # try if typehade is available
#         try:
#             time.sleep(2)
#             typhade = driver.find_element(By.XPATH, "//ngb-typeahead-window[@id='ngb-typeahead-0']")
#             if typhade:
#                 htsInput.send_keys(Keys.ENTER)
#         except:
#             print("New HTS found",val1)
#
#         # Add Date
#         driver.find_element(By.XPATH, "//input[@name='fromDate']").clear()
#         driver.find_element(By.XPATH, "//input[@name='fromDate']").send_keys("2023/10/17")
#
#         # Submit
#         submit = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="formDiv"]/form/div[3]/div[2]/button')))
#         submit.click()
#         time.sleep(5)


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
mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions= [NoSuchElementException,
                                                                         ElementNotVisibleException,
                                                                         ElementNotSelectableException,
                                                                         ElementClickInterceptedException,
                                                                         ElementNotInteractableException,
                                                                         Exception])

# URL
# driver.get("http://52.54.244.138:8080/ArtemusChb/")
# # Maximize page
# driver.maximize_window()
#
# #Login
# driver.find_element(By.ID, "username").send_keys("Ashishh")
# driver.find_element(By.ID, "password").send_keys("ashishh1")
# driver.find_element(By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button').click()


website_url = "http://52.54.244.138:8080/ArtemusChb/"
driver.get(website_url)
a=1
try:
    while True:
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        driver.get(website_url)
        print(a)
        a+=1
        # time.sleep(5)
        # if mywait.until(EC.visibility_of_element_located((By.ID, "username"))):
        #     print("Page loaded successfully")
        # else:
        #     driver.refresh()
        #     print("Page not loaded yet")

        # Wait for 2 minutes before refreshing


except KeyboardInterrupt:
    # Handle keyboard interrupt (Ctrl+C)
    print("Refreshing stopped by user")
    driver.quit()









