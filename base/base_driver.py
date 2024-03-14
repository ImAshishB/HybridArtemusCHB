import pytest
from selenium.common import NoAlertPresentException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.support.wait import WebDriverWait


class BaseDriver:
    def __init__(self, driver):
        self.driver = driver

    def entererror(self):
        try:
            entererrorBox = self.driver.find_elements(By.XPATH, "//button[normalize-space()='Ok']")
            if entererrorBox:
                time.sleep(1)
                self.driver.find_element(By.XPATH, "//button[normalize-space()='Ok']").click()
        except Exception as e:
            print(e)

    def billalert(self):
        billalert = self.driver.find_elements(By.XPATH,"//div[@class='swal2-popup swal2-modal swal2-icon-warning animate__animated animate__fadeInDown']//button[text()='OK']")
        if billalert:
            time.sleep(1)
            self.driver.find_element(By.XPATH,"//div[@class='swal2-popup swal2-modal swal2-icon-warning animate__animated animate__fadeInDown']//button[text()='OK']").click()
            print("This Bill Number is already Used in another Entry")

    def webalert(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
        except NoAlertPresentException:
            pass

    def loadingScreenHandling(self):
        SHORT_TIMEOUT = 1  # give time for the loading element to appear
        LONG_TIMEOUT = 30  # give time for loading to finish
        LOADING_ELEMENT_XPATH = "//body//app-root//app-loader//h3[@class='loadingScreen__text']"
        try:
            WebDriverWait(self.driver, LONG_TIMEOUT).until(EC.invisibility_of_element_located((By.XPATH, LOADING_ELEMENT_XPATH)))
        except TimeoutException:
            pass







