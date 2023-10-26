import time
import pytest
from pages.loginPage import Loginpage
from pages.entryformPage import EntryFormPage
from pages.getAttributes import getAtributesOfText
from selenium.webdriver.common.by import By
from utilites.utils import utills
@pytest.mark.usefixtures("setup")
class TestTradingPartners():
    log = utills.custom_logger()  # we can change logging level
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)
        self.esf = EntryFormPage(self.driver, self.mywait)
        self.getAtrbt = getAtributesOfText(self.driver, self.mywait)

    def test_tradingPartners1(self):
        self.log.info("----Test Case test_tradingPartners1 Started----")

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

        #Go to Trading Partners and perform the action
        # Trading Partners 1
        self.log.info("----Trading Partners 1 Started----")
        self.esf.manufarture("ARTTESTDEMO")
        self.esf.entererror()
        self.esf.seller("ARTTESTDEMO")
        self.esf.entererror()
        self.esf.consignee("ARTTESTDEMO")
        self.esf.entererror()
        self.esf.buyer("ARTTESTDEMO")
        self.esf.entererror()


        # Verification
        expected_manufacturer = "ARTTESTDEMO"
        expected_seller = "ARTTESTDEMO"
        expected_consignee = "ARTTESTDEMO"
        expected_buyer = "ARTTESTDEMO"

        actual_manufacturer = self.getAtrbt.get_manufacturer_text()
        actual_seller = self.getAtrbt.get_seller_text()
        actual_consignee = self.getAtrbt.get_consignee_text()
        actual_buyer = self.getAtrbt.get_buyer_text()

        if actual_manufacturer == expected_manufacturer and actual_seller == expected_seller and actual_consignee == expected_consignee and actual_buyer == expected_buyer:
            assert True
            self.log.info("----Text verification done----")
            self.lp.logout()
        else:
            self.log.error("----Text verification failed----")
            self.driver.save_screenshot(".\\screenshots\\" + "test_tradingPartners1_scr.png")  # Screenshot
            assert False

        self.log.info("----Test Case test_tradingPartners1 End----")

    def test_tradingPartners2(self):
        self.log.info("----Test Case test_tradingPartners2 Started----")
        # Login
        # lp = Loginpage(self.driver, self.mywait)
        self.lp.userName("tnash")
        self.lp.password("tnash1")
        self.lp.login()
        self.log.info("----Login Done----")
        time.sleep(4)

        # Go to 7501 Page
        # self.esf = EntryFormPage(self.driver, self.mywait)
        self.esf.shipment()
        self.esf.form7501()
        self.log.info("----7501 Form Opened----")

        # Go to Trading Partners and perform the action
        # Trading Partners 1
        self.log.info("----Trading Partners 2 Started----")
        self.esf.countryOfOrigin1("India")
        self.esf.entererror()
        self.esf.release_port("NORFOLK, VA")
        self.esf.entererror()
        self.esf.countryOfExport1("India")
        self.esf.entererror()
        self.esf.ladingport("NORFOLK, VA")
        self.esf.entererror()
        self.esf.weight("12")
        self.esf.charges("2000")
        self.esf.unladingport("NORFOLK, VA")
        self.esf.manifestDescription("Demo Purpose")
        self.esf.arrivaldate("2023-08-16")
        self.esf.exportdate("2023-07-15")
        # self.lp.logout()
        # self.log.info("----Trading Partners 2 Done----")

        # Verification
        expected_countryOfOrigin1 = "IN-INDIA"
        expected_release_port = "1401-NORFOLK, VA"
        expected_countryOfExport1 = "IN-INDIA"
        expected_ladingport = "1401-NORFOLK, VA"
        expected_weight = "12"
        expected_charges = "2000"
        expected_unladingport = "1401-NORFOLK, VA"
        expected_manifestDescription = "Demo Purpose"
        expected_arrivaldate = "2023-08-16"
        expected_exportdate = "2023-07-15"

        actual_countryOfOrigin1 = self.getAtrbt.get_countryOfOrigin1_text()
        actual_release_port = self.getAtrbt.get_release_port_text()
        actual_countryOfExport1 = self.getAtrbt.get_countryOfOrigin1_text()
        actual_ladingport = self.getAtrbt.get_ladingport_text()
        actual_weight = self.getAtrbt.get_weight_text()
        actual_charges = self.getAtrbt.get_charges_text()
        actual_unladingport = self.getAtrbt.get_unladingport_text()
        actual_manifestDescription = self.getAtrbt.get_manifestDescription_text()
        actual_arrivaldate = self.getAtrbt.get_arrivaldate_text()
        actual_exportdate = self.getAtrbt.get_exportdate_text()

        # assert actual_countryOfOrigin1 == expected_countryOfOrigin1
        # assert actual_release_port == expected_release_port
        # assert actual_countryOfExport1 == expected_countryOfExport1
        # assert actual_ladingport == expected_ladingport
        # assert actual_weight == expected_weight
        # assert actual_charges == expected_charges
        # assert actual_unladingport == expected_unladingport
        # assert actual_arrivaldate == expected_arrivaldate
        # assert actual_manifestDescription == expected_manifestDescription
        # assert actual_exportdate == expected_exportdate





        if actual_countryOfOrigin1 == expected_countryOfOrigin1 and actual_release_port == expected_release_port\
                and actual_countryOfExport1 == expected_countryOfExport1 and actual_ladingport == expected_ladingport\
                and actual_weight == expected_weight and actual_charges == expected_charges and actual_unladingport == expected_unladingport\
                and actual_arrivaldate == expected_arrivaldate  and actual_manifestDescription == expected_manifestDescription\
                and actual_exportdate == expected_exportdate:
            assert True
            self.log.info("----Text verification done----")
            self.lp.logout()
        else:
            self.log.error("----Text verification failed----")
            self.driver.save_screenshot(".\\screenshots\\" + "test_tradingPartners2_scr.png")  # Screenshot
            assert False

        self.log.info("----Test Case test_tradingPartners2 End----")


# pytest -v -s testcases/test_tradingPartners.py
# pytest -v -s testcases/test_tradingPartners.py --browser chrome
# pytest -v -s testcases/test_tradingPartners.py --browser firefox
# pytest -v --html=reports\report.html testcases/test_tradingPartners.py --browser chrome