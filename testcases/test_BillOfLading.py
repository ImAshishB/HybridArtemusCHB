import time
import pytest
from pages.loginPage import Loginpage
from pages.entryformPage import EntryFormPage
from pages.getAttributes import getAtributesOfText
from utilites.utils import utills
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestBillOfLading():
    log = utills.custom_logger()  # we can change logging level
    randomInvoice = "ABTestInvc" + utills.random_invoceGenerator()  # random_invoceGenerator() came from utils
    randomBill = "M" + utills.random_BillGenerator()  # random_BillGenerator() came from utils
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)
        self.esf = EntryFormPage(self.driver, self.mywait)
        self.getAtrbt = getAtributesOfText(self.driver, self.mywait)

    def test_BillOfLading(self):
        self.log.info("----Test Case test_BillOfLading Started----")

        # Login
        #lp = Loginpage(self.driver, self.mywait)
        self.lp.userName("tnash")
        self.lp.password("tnash1")
        self.lp.login()
        self.log.info("----Login Done----")
        time.sleep(4)

        #Go to 7501 Page
        # self.esf = EntryFormPage(self.driver, self.mywait)
        self.esf.shipment()
        self.esf.form7501()
        self.log.info("----7501 Form Opened----")

        # Bill Of Lading
        self.log.info("----Bill Of lading Started----")
        self.esf.scaccode("MFUS")
        self.esf.entererror()
        self.esf.bill(self.randomBill)
        self.esf.uom("PKG")
        self.esf.entererror()
        self.esf.quantity("21")

        # Verification
        expected_scaccode = "MFUS"
        expected_uom = "PKG"
        expected_quantity = "21"

        actual_scaccode = self.getAtrbt.get_scaccode_text()
        actual_uom = self.getAtrbt.get_uom_text()
        actual_quantity = self.getAtrbt.get_quantity_text()

        if actual_scaccode == expected_scaccode and actual_uom == expected_uom and actual_quantity == expected_quantity:
            assert True
            self.log.info("----Text verification done----")
            self.lp.logout()
        else:
            self.log.error("----Text verification failed----")
            self.driver.save_screenshot(".\\screenshots\\" + "test_BillOfLading_scr.png")  # Screenshot
            assert False

        self.log.info("----Test Case test_BillOfLading End----")



# pytest -v -s testcases/test_BillOfLading.py
# pytest -v -s testcases/test_BillOfLading.py --browser chrome
# pytest -v -s testcases/test_BillOfLading.py --browser firefox
# pytest -v --html=reports\report.html testcases/test_BillOfLading.py --browser chrome