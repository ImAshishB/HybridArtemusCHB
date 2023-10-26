import time
import pytest
# import softest
import logging

from pages.loginPage import Loginpage
from selenium.webdriver.common.by import By
from utilites.utils import utills
@pytest.mark.usefixtures("setup")
class TestLogin():
    log = utills.custom_logger()  # we can change logging level

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)

    def test_loginBy1stOneCredentials(self):

        #lp = Loginpage(self.driver, self.mywait)
        self.lp.userName("tnash")
        self.lp.password("tnash1")
        self.lp.login()
        time.sleep(3)

        home = self.driver.find_element(By.XPATH, "//a[@routerlink='/userHome']")
        hometext=home.text
        self.log.info("Name shown in Homepage")

        if hometext== "Welcome, tnash  ":
            assert True
            self.lp.logout()
            self.log.info("Test Case Pass")
        else:
            self.lp.logout()
            self.log.info("Test Case failed")
            assert False


    def test_loginBy2ndOneCredentials(self):

        #lp = Loginpage(self.driver, self.mywait)
        self.lp.userName("artemus")
        self.lp.password("artemus@257")
        self.lp.login()
        time.sleep(5)

        home = self.driver.find_element(By.XPATH, "//a[@routerlink='/userHome']")
        hometext=home.text
        print(hometext)
        self.log.info("Name shown in Homepage2")

        if hometext!= "Welcome, tnash  ":
            assert True
            self.lp.logout()
            print("Test Case Pass")
            self.log.info("Test Case 2 Pass")
        else:
            self.lp.logout()
            print("Test Case failed")
            self.log.info("Test Case 2 failed")
            assert False



# pytest -v -s testcases/test_Login.py
# pytest -v -s testcases/test_Login.py --browser chrome
# pytest -v -s testcases/test_Login.py --browser firefox
# pytest -v -s --html=reports\report.html testcases/test_Login.py    #if in html report if logs are not getting genrated then remove -s and try