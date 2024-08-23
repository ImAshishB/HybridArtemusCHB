import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver
from utilites.utils import utills


class ReportsPage(BaseDriver):
    def __init__(self, driver, mywait):
        super().__init__(driver)
        self.driver = driver
        self.mywait = mywait

    # Locators
    reports_LINK_TEXT = "Reports"

    def reports(self):
        reportslink = self.mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.reports_LINK_TEXT)))
        reportslink.click()