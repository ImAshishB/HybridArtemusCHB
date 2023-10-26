# import time
# import pytest
# # import softest
# import logging
# import openpyxl
# from openpyxl.styles import PatternFill
# from pages.loginPage import Loginpage
# from selenium.webdriver.common.by import By
# from utilites import utils
# from utilites.utils import utills
# @pytest.mark.usefixtures("setup")
# class TestLogin():
#     file = "D:\\LoginTestData22.xlsx"
#     log = utills.custom_logger()  # we can change logging level
#     # rows = utills.getRowCount(self.file, "Sheet1")
#     # coloumns = utills.getColumnCount(self.file, "Sheet1")
#
#
#     @pytest.fixture(autouse=True)
#     def class_setup(self):
#         self.lp = Loginpage(self.driver, self.mywait)
#         self.rows = utills.getRowCount(self.file, "Sheet1")
#         self.coloumns = utills.getColumnCount(self.file, "Sheet1")
#         list_status = []  # Empty List Veriable
#
#
#     def test_loginBy1stOneCredentials(self):
#
#         # list_status = []  # Empty List Veriable
#         for r in range(2, self.rows + 1):  # 2, self.rows+1
#             self.usernameData = utills.readData(self.file, 'Sheet1', r, 1)
#             self.passwordData = utills.readData(self.file, 'Sheet1', r, 2)
#             self.lp.userName(self.usernameData)
#             self.lp.password(self.passwordData)
#             self.lp.login()
#             time.sleep(5)
#
#             home = self.driver.find_element(By.XPATH, "//a[@routerlink='/userHome']")
#             hometext = home.text
#             self.log.info("Name shown in Homepage")
#
#             if hometext == "Welcome, tnash  ":
#                 # assert True
#                 self.lp.logout()
#                 self.log.info("Test Case Pass")
#                 # print("Test Case Pass")
#             else:
#                 self.lp.logout()
#                 self.log.warning("Test Case failed")
#                 # print("Test Case failed")
#                 #assert False



# pytest -v -s testcases/test_Login.py
# pytest -v -s testcases/test_Login.py --browser chrome
# pytest -v -s testcases/test_Login.py --browser firefox

# pytest -v -s testcases/test_LoginDDT.py
# pytest -v -s testcases/test_LoginDDT.py --browser firefox


# pytest -v -s --html=reports\report.html testcases/test_LoginDDT.py    #if in html report if logs are not getting genrated then remove -s and try



















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
    file = "D:\\LoginTestData22.xlsx"
    log = utills.custom_logger()  # we can change logging level
    rows = utills.getRowCount(file, "Sheet1")
    coloumns = utills.getColumnCount(file, "Sheet1")
    list_status = []  # Empty List Veriable




    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)


    def test_loginBy1stOneCredentials(self):
        for r in range(2, 3):  # 2, self.rows+1
            self.usernameData = utills.readData(self.file, 'Sheet1', r, 1)
            self.passwordData = utills.readData(self.file, 'Sheet1', r, 2)
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            time.sleep(5)

            home = self.driver.find_element(By.XPATH, "//a[@routerlink='/userHome']")
            hometext = home.text
            self.log.info("Name shown in Homepage")

            if hometext == "Welcome, tnash  ":
                # assert True
                self.lp.logout()
                self.log.info("Test Case Pass")
                # print("Test Case Pass")
            else:
                self.lp.logout()
                self.log.warning("Test Case failed")

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

# pytest -v -s testcases/test_LoginDDT.py
# pytest -v -s testcases/test_LoginDDT.py --browser firefox


# pytest -v -s --html=reports\report.html testcases/test_LoginDDT.py    #if in html report if logs are not getting genrated then remove -s and try