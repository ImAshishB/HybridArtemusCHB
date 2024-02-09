from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
    ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
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
driver.get("https://www.calculator.net/")
input1Data=2
input2Data=3

try:
    # value of A
    input1=driver.find_element(By.XPATH, "//span[normalize-space()='"+str(input1Data)+"']")
    input1.click()
    # multiply
    driver.find_element(By.XPATH, "//span[normalize-space()='×']").click()
    # value of B
    input2 = driver.find_element(By.XPATH, "//span[normalize-space()='" + str(input2Data) + "']")
    input2.click()
    # equal to C
    driver.find_element(By.XPATH, "//span[normalize-space()='=']").click()
    time.sleep(1)
    # calculation
    calculation_element = driver.find_element(By.XPATH, "//div[@id='sciOutPut']")

    input1Text = input1.text
    Intinput1Text = int(input1Text)

    input2Text = input2.text
    Intinput2BText = int(input2Text)

    calculation_text = calculation_element.text
    Intcalculation_text = int(calculation_text)


    expected_result = Intinput1Text* Intinput2BText
    print("Expected result:", expected_result)
    print("Actual result:", Intcalculation_text)
    if expected_result == Intcalculation_text:
        print("Calculation is correct!")
    else:
        print("Calculation is not correct!")

except Exception as e:
    print("Error:", e)





# from selenium import webdriver
# from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
#     ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
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
# driver.get("https://www.calculator.net/")
# input1Data=[1,2,3,4,5,6,7,8,9,10]
# input2Data=[2,3,4,5,6,7,8,9,10,11]
#
# try:
#     for input1Value, input2Value in zip(input1Data, input2Data):
#         # value of A
#         input1 = driver.find_element(By.XPATH, "//span[normalize-space()='" + str(input1Value) + "']")
#         input1.click()
#         # multiply
#         driver.find_element(By.XPATH, "//span[normalize-space()='×']").click()
#         # value of B
#         input2 = driver.find_element(By.XPATH, "//span[normalize-space()='" + str(input2Value) + "']")
#         input2.click()
#         # equal to C
#         driver.find_element(By.XPATH, "//span[normalize-space()='=']").click()
#         time.sleep(1)
#         # calculation
#         calculation_element = driver.find_element(By.XPATH, "//div[@id='sciOutPut']")
#
#         input1Text = input1.text
#         Intinput1Text = int(input1Text)
#
#         input2Text = input2.text
#         Intinput2BText = int(input2Text)
#
#         calculation_text = calculation_element.text
#         Intcalculation_text = int(calculation_text)
#
#         expected_result = Intinput1Text * Intinput2BText
#         print("Expected result:", expected_result)
#         print("Actual result:", Intcalculation_text)
#         if expected_result == Intcalculation_text:
#             print("Calculation is correct!")
#         else:
#             print("Calculation is not correct!")
#
# except Exception as e:
#     print("Error:", e)
