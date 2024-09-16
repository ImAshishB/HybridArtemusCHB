import time
import pytest
# import softest
import logging

from pages.test_Page import TestPage
from selenium.webdriver.common.by import By
from utilites.utils import utills
@pytest.mark.usefixtures("setup")
class TestLogin():
    log = utills.custom_logger()  # we can change logging level
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = TestPage(self.driver, self.mywait)
    def test_loginBy1stOneCredentials(self):
        #lp = Loginpage(self.driver, self.mywait)
        self.lp.userName("tnash")
        self.lp.password("tnash1")
        self.lp.login()
        self.lp.loadingScreenHandling()

        home = self.driver.find_element(By.XPATH, "//a[@routerlink='/userHome']")
        hometext=home.text
        self.log.info("Login Done")

        if hometext== "Welcome, tnash  ":
            assert True
            self.lp.logout()
            self.log.info("Test Case Pass")
            self.lp.close()
        else:
            self.lp.logout()
            self.log.error("Test Case failed")
            assert False


    def test_loginBy2ndOneCredentials(self):
        #lp = Loginpage(self.driver, self.mywait)
        self.lp.userName("artemus")
        self.lp.password("artemus@257")
        self.lp.login()
        self.lp.loadingScreenHandling()

        home = self.driver.find_element(By.XPATH, "//a[@routerlink='/userHome']")
        hometext=home.text
        print(hometext)
        self.log.info("Login Done")

        if hometext!= "Welcome, tnash  ":
            assert True
            self.lp.logout()
            self.lp.close()
            print("Test Case Pass")
            self.log.info("Test Case 2 Pass")

        else:
            self.lp.logout()
            print("Test Case failed")
            self.log.error("Test Case 2 failed")
            assert False



# pytest -v -s testcases/test_Test1.py
# pytest -v -s testcases/test_Test1.py --browser chrome
# pytest -v -s testcases/test_Test1.py --browser firefox
# pytest -v -s --html=reports\report.html testcases/test_Test1.py    #if in html report if logs are not getting genrated then remove -s and try
# pytest -v  --html=reports\loginTestReport.html testcases/test_Test1.py