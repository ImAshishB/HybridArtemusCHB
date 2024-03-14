import time
import pytest
# import softest
import logging
import openpyxl
from openpyxl.styles import PatternFill
from pages.loginPage import Loginpage
from selenium.webdriver.common.by import By
from utilites import utils
from utilites.utils import utills
@pytest.mark.usefixtures("setup")
class TestLogin():
    file = "D:/Artmus Spec/Automation_Artemus/TestML.xlsx"
    log = utills.custom_logger()  # we can change logging level
    list_status = []  # Empty List Veriable

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)

    def test_loginBy1stOneCredentials(self):
        global hometext
        for r in range(3, 7):  # 2, self.rows+1
            self.usernameData = utills.readData(self.file, 'LoginTestDDT', r, 1)
            self.passwordData = utills.readData(self.file, 'LoginTestDDT', r, 2)
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            self.log.info("Clicked on Login Button")
            self.lp.loadingScreenHandling()

            try:
                home = self.driver.find_element(By.XPATH, "//a[@routerlink='/userHome']")
                hometext = home.text
                self.log.info("Name shown in Homepage")
            except Exception as e:
                self.log.info("Name not shown in Homepage")

            if hometext == "Welcome, tnash  ":
                # assert True
                self.lp.logout()
                self.log.info("Test Case Pass")
                utills.writeData(self.file, "LoginTestDDT", r, 4, "Login Successfully")

            if hometext != "Welcome, tnash  ":
                # assert True
                self.lp.logout()
                self.log.info("Test Case Pass")
                utills.writeData(self.file, "LoginTestDDT", r, 4, "Wrong User Login")

        self.driver.close()


# pytest -v -s testcases/test_Login.py
# pytest -v -s testcases/test_Login.py --browser chrome
# pytest -v -s testcases/test_Login.py --browser firefox

# pytest -v -s testcases/test_LoginDDT.py
# pytest -v -s testcases/test_LoginDDT.py --browser firefox

# pytest -v -s --html=reports\LoginTestDDTReport.html testcases/test_LoginDDT.py
# pytest -v --html=reports\LoginTestDDTReport.html testcases/test_LoginDDT.py
# pytest -v -s --html=reports\report.html testcases/test_LoginDDT.py    #if in html report if logs are not getting genrated then remove -s and try