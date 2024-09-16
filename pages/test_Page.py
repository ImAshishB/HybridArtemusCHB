import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains, Keys
from base.base_driver import BaseDriver
from utilites.utils import utills

class TestPage(BaseDriver):
    # log = utills.custom_logger(logLevel=logging.WARNING) # we can change logging level
    def __init__(self, driver, mywait):
        super().__init__(driver)
        self.driver = driver
        self.mywait = mywait

    login_username_element = (By.ID, "username")
    login_password_element = (By.ID, "password")
    loginButton_element = (By.XPATH, '//*[@id="background"]/div/div/div/div/div/form/button')
    logOutButton_element = (By.XPATH, "//a[normalize-space()='Logout']")

    def userName(self,username):
        login_usernameTxt = self.mywait.until(EC.element_to_be_clickable(self.login_username_element))
        login_usernameTxt.click()
        login_usernameTxt.send_keys(username)
        #self.log.warning("username done")

    def password(self, password):
        login_passwordTxt = self.mywait.until(EC.element_to_be_clickable(self.login_password_element))
        login_passwordTxt.click()
        login_passwordTxt.send_keys(password)
        #self.log.warning("password done")

    def login(self):
        loginButton = self.driver.find_element(*self.loginButton_element)
        loginButton.click()
        #self.log.warning("login done")

    def logout(self):
        logoutButton = self.driver.find_element(*self.logOutButton_element)
        logoutButton.click()
        #self.log.warning("logout done")

    def close(self):
        self.driver.close()

