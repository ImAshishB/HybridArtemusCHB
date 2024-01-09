import time
import pytest
from pages.loginPage import Loginpage
from pages.entryformPage import EntryFormPage
from selenium.webdriver.common.by import By
from utilites.utils import utills
from selenium.common import NoAlertPresentException
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver
from utilites.utils import utills

@pytest.mark.usefixtures("setup")
class TestEntryForm():
    random = "ABTestInvc"+ utills.random_invoceGenerator() # random_invoceGenerator() came from utils
    # random = " "
    file = "D:/Artmus Spec/Automation_Artemus/TestML.xlsx"
    log = utills.custom_logger()  # we can change logging level
    rows = utills.getRowCount(file, "Sheet1")
    coloumns = utills.getColumnCount(file, "Sheet1")
    list_status = []  # Empty List Veriable

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)
        self.esf = EntryFormPage(self.driver, self.mywait)


    def test_saveformwithinvoiceNumber(self):
        self.log.info("----------------Test Case test_saveformwithinvoiceNumber Starterd----------------")

        for r in range(3, 4):
            self.usernameData = utills.readData(self.file, 'Sheet1', r, 5)
            self.passwordData = utills.readData(self.file, 'Sheet1', r, 6)
            self.selectIMPORTERData = utills.readData(self.file, 'Sheet1', r, 140)


            # Login
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            time.sleep(4)

            # Go to 7501 Page
            self.esf = EntryFormPage(self.driver, self.mywait)
            self.esf.shipment()
            self.esf.selectImporter(self.selectIMPORTERData)
            self.esf.form7501()
            self.log.info("----Entered in Form 7501----")

            # Add Invoice Number
            self.esf.invoicenumber(self.random)

            # Save the form
            self.esf.saveform()

            # Verify that form should be saved
            self.msg = self.driver.find_element(By.TAG_NAME, "body").text

            if 'Form saved succesfully!' in self.msg:
                assert True
                self.esf.formSavedConfirmationMsg()
                self.log.info("Test Case 'save form with invoice Number' Passed")
                self.lp.logout()
                self.esf.close()
            else:
                self.driver.save_screenshot(".\\screenshots\\" + "test_saveformwithinvoiceNumber_scr.png")  # Screenshot
                self.esf.formSavedConfirmationMsg()
                self.log.info("Test Case 'save form with invoice Number' Failed")
                # self.lp.logout()
                assert False
        self.log.info("----------------Test Case test_saveformwithinvoiceNumber End----------------")

    def test_saveformwithoutinvoiceNumber(self):
        self.log.info("----------------Test Case test_saveformwithoutinvoiceNumber Starterd----------------")

        for r in range(3, 4):
            self.usernameData = utills.readData(self.file, 'Sheet1', r, 5)
            self.passwordData = utills.readData(self.file, 'Sheet1', r, 6)
            self.selectIMPORTERData = utills.readData(self.file, 'Sheet1', r, 140)

            # Login
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            time.sleep(4)

            # Go to 7501 Page
            self.esf = EntryFormPage(self.driver, self.mywait)
            self.esf.shipment()
            self.esf.selectImporter(self.selectIMPORTERData)
            self.esf.form7501()
            self.log.info("----Entered in Form 7501----")

            # Do not Add Invoice Number
            # self.esf.invoicenumber(self.random)

            # Save the form
            self.esf.saveform()

            # Verify that form should be saved
            self.msg = self.driver.find_element(By.TAG_NAME, "body").text

            if 'Enter Invoice Number!' in self.msg:
                assert True
                self.esf.formSavedConfirmationMsg()
                self.log.info("Test Case 'save form without invoice Number' Passed")
                self.lp.logout()
                self.esf.close()
            else:
                self.driver.save_screenshot(".\\screenshots\\" + "test_saveformwithoutinvoiceNumber_scr.png")  # Screenshot
                self.esf.formSavedConfirmationMsg()
                self.log.info("Test Case 'save form without invoice Number' Failed")
                # self.lp.logout()
                assert False
        self.log.info("----------------Test Case test_saveformwithoutinvoiceNumber End----------------")

    def test_saveformwithExistinginvoiceNumber(self):
        self.log.info("----------------Test Case test_saveformwithExistinginvoiceNumber Starterd----------------")

        for r in range(3, 4):
            self.usernameData = utills.readData(self.file, 'Sheet1', r, 5)
            self.passwordData = utills.readData(self.file, 'Sheet1', r, 6)
            self.selectIMPORTERData = utills.readData(self.file, 'Sheet1', r, 140)

            # Login
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            time.sleep(4)

            # Go to 7501 Page
            self.esf = EntryFormPage(self.driver, self.mywait)
            self.esf.shipment()
            self.esf.selectImporter(self.selectIMPORTERData)
            self.esf.form7501()
            self.log.info("----Entered in Form 7501----")

            # Add Invoice Number
            self.esf.invoicenumber(self.random)

            self.esf.webalert()
            self.log.info("Test Case 'save form with Existing invoice Number' Passed")

            # LogOut
            self.lp.logout()
            self.esf.close()
            self.log.info("----------------Test Case test_saveformwithExistinginvoiceNumber End----------------")

    def test_saveformwithParts(self):
        self.log.info("----------------Test Case test_saveformwithParts Starterd----------------")

        for r in range(3, 4):
            self.usernameData = utills.readData(self.file, 'Sheet1', r, 5)
            self.passwordData = utills.readData(self.file, 'Sheet1', r, 6)
            self.selectIMPORTERData = utills.readData(self.file, 'Sheet1', r, 140)

            # Login
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            time.sleep(4)

            # Go to 7501 Page
            self.esf = EntryFormPage(self.driver, self.mywait)
            self.esf.shipment()
            self.esf.selectImporter(self.selectIMPORTERData)
            self.esf.form7501()
            self.log.info("----Entered in Form 7501----")

            # Add Invoice Number
            self.esf.invoicenumber(self.random)

            # Add Line Items
            self.esf.part("ABSmkPart")
            self.esf.entererror()

            # Save the form
            self.esf.saveform()

            # Verify that form should be saved
            self.msg = self.driver.find_element(By.TAG_NAME, "body").text

            if 'Form saved succesfully!' in self.msg:
                assert True
                self.esf.formSavedConfirmationMsg()
                self.log.info("Test Case 'save form with Parts' Passed")
                self.lp.logout()
                self.esf.close()
            else:
                self.driver.save_screenshot(".\\screenshots\\" + "test_saveformwithParts_scr.png")  # Screenshot
                self.esf.formSavedConfirmationMsg()
                self.log.info("Test Case 'save form with Parts' Failed")
                # self.lp.logout()
                assert False
        self.log.info("----------------Test Case test_saveformwithParts End----------------")




# pytest -v -s testcases/test_smokTestCases.py
# pytest -v -s testcases/test_smokTestCases.py --browser chrome
# pytest -v -s testcases/test_smokTestCases.py --browser firefox
# pytest -v -s --html=reports\smokTestReport.html testcases/test_smokTestCases.py
# pytest -v --html=reports\smokTestReport.html testcases/test_smokTestCases.py --browser chrome   #if in html report if logs are not getting genrated then remove -s and try
# pytest -v -s -n=3 --html=reports\smokTestReport.html testcases/test_smokTestCases.py --browser chrome