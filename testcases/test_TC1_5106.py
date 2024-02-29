import time
import pytest
from pages.loginPage import Loginpage
from pages.entryformPage import EntryFormPage
from pages.form5106Page import  Form5106Page
from pages.getAttributes import getAtributesOfText
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
class Test_5106_TC1():
    ImporterNameData = "Imprtr CPMA_" + utills.random_importerNameGenerator() # random_importerNameGenerator() came from utils
    ImporterNumberData = "10-" + utills.random_importerNumberGenerator() # random_importerNumberGenerator() came from utils
    file = "D:/Artmus Spec/Automation_Artemus/TestML.xlsx"
    log = utills.custom_logger_5106()  # we can change logging level
    list_status = []  # Empty List Veriable


    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)
        self.esf = EntryFormPage(self.driver, self.mywait)
        self.getvalues = getAtributesOfText(self.driver, self.mywait)
        self.frm5106 = Form5106Page(self.driver, self.mywait)


    def test_ITTC1(self):
        self.log.info("----------------Test Case test_HTC1 Starterd----------------")

        for r in range(3, 4):
            self.usernameData = utills.readData(self.file, "Sheet5106", r, 4)
            self.passwordData = utills.readData(self.file, "Sheet5106", r, 5)
            self.UtilizedforChckBoxData = utills.readData(self.file, "Sheet5106", r, 3)
            self.ImporterNameEx = utills.readData(self.file, "Sheet5106", r, 6)
            self.AlternateImporterNameData = utills.readData(self.file, "Sheet5106", r, 9)
            self. OtherDescriptionData = utills.readData(self.file, "Sheet5106", r, 10)
            self.ImporterTypeData = utills.readData(self.file, "Sheet5106", r, 11)
            self.MailingAddressData = utills.readData(self.file, "Sheet5106", r, 12)
            self.Line1Data = utills.readData(self.file, "Sheet5106", r, 13)
            self.Line2Data = utills.readData(self.file, "Sheet5106", r, 14)
            self.ZipcodeData = utills.readData(self.file, "Sheet5106", r, 15)
            self.AddressTypeData = utills.readData(self.file, "Sheet5106", r, 16)
            self.cityData = utills.readData(self.file, "Sheet5106", r, 17)
            self.CountryCodeData = utills.readData(self.file, "Sheet5106", r, 18)
            self.StateData = utills.readData(self.file, "Sheet5106", r, 19)
            self.AddressExplanationData = utills.readData(self.file, "Sheet5106", r, 20)
            self.PhoneData = utills.readData(self.file, "Sheet5106", r, 21)
            self.EmailData = utills.readData(self.file, "Sheet5106", r, 22)

            # Login
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            self.log.info("----Login Done----")
            time.sleep(4)

            # Go to 5106 Page
            self.frm5106.L5106()
            time.sleep(1)
            self.frm5106.form5106()
            time.sleep(1)
            self.log.info("----Form 5106 Opened----")

            # Form
            self.log.info("----Form filling Started----")
            self.frm5106.importerName(self.ImporterNameData)
            self.frm5106.importerNumber(self.ImporterNumberData)

            self.frm5106.Line1(self.Line1Data)
            self.frm5106.Line2(self.Line2Data)
            self.frm5106.Zipcode(self.ZipcodeData)
            self.frm5106.AddressType(self.AddressTypeData)
            self.frm5106.City(self.cityData)
            self.frm5106.Country(self.CountryCodeData)
            time.sleep(1)
            self.frm5106.State(self.StateData)

            self.frm5106.CopyMailingAddress()

            self.frm5106.PhoneNumber(self.PhoneData)
            self.frm5106.EmailAddress(self.EmailData)

            self.frm5106.SaveButton()
            self.frm5106.ConfirmationOfSave()

            self.frm5106.AllButton()

            self.log.info("----Form filling Done----")


            # Save the form
            # self.esf.saveform()

            # Verify that form should be saved
            # self.msg = self.driver.find_element(By.TAG_NAME, "body").text
            #
            # if 'Form saved succesfully!' in self.msg:
            #     assert True
            #     self.esf.formSavedConfirmationMsg()
            #     self.log.info("----Form Saved Successfully----")
            #     self.lp.logout()
            # else:
            #     self.driver.save_screenshot(".\\screenshots\\" + "test_HTC1_scr.png")  # Screenshot
            #     self.esf.formSavedConfirmationMsg()
            #     self.log.error("----Form Not Saved. Test Failed----")
            #     self.lp.logout()
            #     assert False

        self.log.info("----------------Test Case test_IMTC1 End----------------")



# pytest -v -s testcases/test_TC1_5106.py
# pytest -v -s testcases/test_TC1.py --browser chrome
# pytest -v -s testcases/test_TC1.py --browser firefox
# pytest -v -s --html=reports\report.html testcases/test_TC1.py
# pytest -v --html=reports\report.html testcases/test_TC1.py --browser chrome   #if in html report if logs are not getting genrated then remove -s and try