import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import ActionChains, Keys
from base.base_driver import BaseDriver
from utilites.utils import utills


class Querypage(BaseDriver):
    # log = utills.custom_logger(logLevel=logging.WARNING) # we can change logging level
    def __init__(self, driver, mywait):
        super().__init__(driver)
        self.driver = driver
        self.mywait = mywait

    query_LINK_TEXT = "Queries"
    misc_LINK_TEXT = "Miscellaneous"
    tariffquery_XPATH = "//span[normalize-space()='Tariff Query']"
    htsnumberTxt_ID = "HTSUSNo"
    htsOutclick_XPATH = "//span[normalize-space()='HTSUS:']"
    typehade_XPATH = "//ngb-typeahead-window[@id='ngb-typeahead-0']"
    dateofquery_XPATH = "//input[@name='fromDate']"
    submit_XPATH = '//*[@id="formDiv"]/form/div[3]/div[2]/button'


    def query(self):
        querylink = self.mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.query_LINK_TEXT)))
        querylink.click()

    def misc(self):
        misclink = self.mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.misc_LINK_TEXT)))
        misclink.click()

    def tariffquery(self):
        tariffquerylink = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.tariffquery_XPATH)))
        tariffquerylink.click()

    def hts(self,htsNumber):
        htsInput = self.driver.find_element(By.ID, self.htsnumberTxt_ID)
        htsInput.clear()
        self.driver.find_element(By.XPATH, self.htsOutclick_XPATH).click()
        htsInput.send_keys(htsNumber)

        try:
            time.sleep(2)
            typhade = self.driver.find_element(By.XPATH, self.typehade_XPATH)
            if typhade:
                htsInput.send_keys(Keys.ENTER)
        except:
            print("New HTS found",htsNumber)

    def dateofquery(self,date):
        self.driver.find_element(By.XPATH, self.dateofquery_XPATH).clear()
        self.driver.find_element(By.XPATH, self.dateofquery_XPATH).send_keys(date)

    def submitButton(self):
        submit = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.submit_XPATH)))
        submit.click()


