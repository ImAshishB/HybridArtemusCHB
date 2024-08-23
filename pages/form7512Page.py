import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver
from utilites.utils import utills


class Form7512Page(BaseDriver):
    def __init__(self, driver, mywait):
        super().__init__(driver)
        self.driver = driver
        self.mywait = mywait

    # Locators
    form7512_LINK_TEXT = "Form 7512"

    def form7512(self):
        form7512link = self.mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.form7512_LINK_TEXT)))
        form7512link.click()