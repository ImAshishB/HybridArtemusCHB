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
class TestSmokTC():
    random = "AB1_SmokTest_"+ utills.random_invoceGenerator() # random_invoceGenerator() came from utils
    randomPlus = "AB2_SmokTest_"+ utills.random_invoceGenerator() # random_invoceGenerator() came from utils
    # random = " "
    file = "D:/Artmus Spec/Automation_Artemus/TestML.xlsx"
    log = utills.custom_logger()  # we can change logging level
    list_status = []  # Empty List Veriable

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)
        self.esf = EntryFormPage(self.driver, self.mywait)

    @pytest.mark.sanity
    def test_saveformwithinvoiceNumber(self):
        self.log.info("----------------Test Case test_saveformwithinvoiceNumber Starterd----------------")

        for r in range(3, 4):
            self.usernameData = utills.readData(self.file, 'SmokTestData', r, 5)
            self.passwordData = utills.readData(self.file, 'SmokTestData', r, 6)
            self.selectIMPORTERData = utills.readData(self.file, 'SmokTestData', r, 140)


            # Login
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            self.lp.loadingScreenHandling()


            # Go to 7501 Page
            self.esf = EntryFormPage(self.driver, self.mywait)
            self.esf.shipment()
            self.esf.selectImporter(self.selectIMPORTERData)
            self.esf.form7501()
            self.log.info("Entered in Form 7501")

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
                self.esf.close() # I have included close at conftest that's why I am commenting this line
            else:
                self.driver.save_screenshot(".\\screenshots\\" + "test_saveformwithinvoiceNumber_scr.png")  # Screenshot
                self.esf.formSavedConfirmationMsg()
                self.log.error("Test Case 'save form with invoice Number' Failed")
                # self.lp.logout()
                assert False
        self.log.info("----------------Test Case test_saveformwithinvoiceNumber End----------------")

    @pytest.mark.sanity
    def test_saveformwithoutinvoiceNumber(self):
        self.log.info("----------------Test Case test_saveformwithoutinvoiceNumber Starterd----------------")

        for r in range(3, 4):
            self.usernameData = utills.readData(self.file, 'SmokTestData', r, 5)
            self.passwordData = utills.readData(self.file, 'SmokTestData', r, 6)
            self.selectIMPORTERData = utills.readData(self.file, 'SmokTestData', r, 140)

            # Login
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            self.lp.loadingScreenHandling()

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
                self.esf.close() # I have included close at conftest that's why I am commenting this line
            else:
                self.driver.save_screenshot(".\\screenshots\\" + "test_saveformwithoutinvoiceNumber_scr.png")  # Screenshot
                self.esf.formSavedConfirmationMsg()
                self.log.info("Test Case 'save form without invoice Number' Failed")
                # self.lp.logout()
                assert False
        self.log.info("----------------Test Case test_saveformwithoutinvoiceNumber End----------------")

    @pytest.mark.sanity
    def test_saveformwithExistinginvoiceNumber(self):
        self.log.info("----------------Test Case test_saveformwithExistinginvoiceNumber Starterd----------------")

        for r in range(3, 4):
            self.usernameData = utills.readData(self.file, 'SmokTestData', r, 5)
            self.passwordData = utills.readData(self.file, 'SmokTestData', r, 6)
            self.selectIMPORTERData = utills.readData(self.file, 'SmokTestData', r, 140)

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
            self.esf.close() # I have included close at conftest that's why I am commenting this line
            self.log.info("----------------Test Case test_saveformwithExistinginvoiceNumber End----------------")

    @pytest.mark.sanity
    def test_saveAndSubmitFormwithInvoiceNumberOnly(self):
        self.log.info("----------------Test Case test_saveAndSubmitFormwithInvoiceNumberOnly Starterd----------------")

        for r in range(3, 4):
            self.usernameData = utills.readData(self.file, 'SmokTestData', r, 5)
            self.passwordData = utills.readData(self.file, 'SmokTestData', r, 6)
            self.selectIMPORTERData = utills.readData(self.file, 'SmokTestData', r, 140)


            # Login
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            self.lp.loadingScreenHandling()


            # Go to 7501 Page
            self.esf = EntryFormPage(self.driver, self.mywait)
            self.esf.shipment()
            self.esf.selectImporter(self.selectIMPORTERData)
            self.esf.form7501()
            self.log.info("Entered in Form 7501")

            # Add Invoice Number
            self.esf.invoicenumber(self.randomPlus)

            # Save the form
            self.esf.saveform()
            self.esf.formSavedConfirmationMsg()
            self.log.info("Form Saved")
            self.esf.submitform()
            self.esf.MandatoryFieldMsg()
            self.log.info("Test Case 'save And Submit Form with Invoice Number Only ' Passed")



            # Verify that form should be saved
            # self.msg = self.driver.find_element(By.TAG_NAME, "body").text

            # if 'Form saved succesfully!' in self.msg:
            #     self.esf.formSavedConfirmationMsg()
            #     self.log.info("Form Saved")
            #     self.esf.submitform()
            #     if 'Fill Mandatory Fields!' in self.msg:
            #         self.esf.MandatoryFieldMsg()
            #         self.log.info("Test Case 'save And Submit Form with Invoice Number Only ' Passed")
            #     self.lp.logout()
            #     self.esf.close() # I have included close at conftest that's why I am commenting this line
            # else:
            #     self.driver.save_screenshot(".\\screenshots\\" + "test_saveAndSubmitFormwithInvoiceNumberOnly_scr.png")  # Screenshot
            #     self.log.error("Test Case 'save And Submit Form with Invoice Number Only' Failed")
            #     # self.lp.logout()
        self.log.info("----------------Test Case test_saveAndSubmitFormwithInvoiceNumberOnly End----------------")




# pytest -v -s testcases/test_smokTestCases.py
# pytest -v -s testcases/test_smokTestCases.py --browser chrome
# pytest -v -s testcases/test_smokTestCases.py --browser firefox
# pytest -v -s --html=reports\smokTestReport.html testcases/test_smokTestCases.py
# pytest -v --html=reports\smokTestReport.html testcases/test_smokTestCases.py
# pytest -v --html=reports\smokTestReport.html testcases/test_smokTestCases.py --browser chrome   #if in html report if logs are not getting genrated then remove -s and try
# pytest -v -s -n=3 --html=reports\smokTestReport.html testcases/test_smokTestCases.py --browser chrome

# pytest -v -s -m "sanity"  --html=reports\report.html testcases/

# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.integration