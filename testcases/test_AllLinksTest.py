import time
import pytest
from pages.loginPage import Loginpage
from pages.entryformPage import EntryFormPage
from pages.queryPage import  Querypage
from pages.form5106Page import  Form5106Page
from pages.form7512Page import  Form7512Page
from pages.formisfPage import  FormISFPage
from pages.importerPage import  ImporterPage
from pages.invoicesPage import InvoicesPage
from pages.partiesPage import  PartiesPage
from pages.partsPage import  PartsPage
from pages.reportsPage import  ReportsPage
from pages.statementsPage import   StatementsPage
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
class Test_AllLinksTest():
    randomInvoice = "ABTstAllLinksTest_VslNCnt_"+ utills.random_invoceGenerator() # random_invoceGenerator() came from utils
    randomBill = "M" + utills.random_BillGenerator()  # random_BillGenerator() came from utils
    file = "D:/Artmus Spec/Automation_Artemus/TestML.xlsx"
    log = utills.custom_logger()
    selectIMPORTERData = "arttest"
    list_status = []  # Empty List Veriable

    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)
        self.esf = EntryFormPage(self.driver, self.mywait)
        self.qry = Querypage(self.driver, self.mywait)
        self.f5106 = Form5106Page(self.driver, self.mywait)
        self.f7512 = Form7512Page(self.driver, self.mywait)
        self.isf = FormISFPage(self.driver, self.mywait)
        self.imprtr = ImporterPage(self.driver, self.mywait)
        self.invc = InvoicesPage(self.driver, self.mywait)
        self.parties = PartiesPage(self.driver, self.mywait)
        self.parts = PartsPage(self.driver, self.mywait)
        self.rprts = ReportsPage(self.driver, self.mywait)
        self.stmnt = StatementsPage(self.driver, self.mywait)
        self.getvalues = getAtributesOfText(self.driver, self.mywait)

    @pytest.mark.sanity
    def test_AllLinksTest(self):
        self.log.info("----------------Test Case test_AllLinksTest Starterd----------------")

        # Login
        self.lp.userName("tnash")
        self.lp.password("tnash1")
        self.lp.login()
        self.log.info("----Clicked On Login Button----")
        self.lp.loadingScreenHandling()

        # HomePage
        HomePageText = self.driver.find_element(By.TAG_NAME, "body").text
        try:
            assert 'Welcome, tnash' in HomePageText
            self.log.info("Assertion passed: Valid User is on the home page.")
        except AssertionError:
            self.log.error("Assertion failed: Valid User is not on the home page.")
            print("Assertion failed: Valid User is not on the home page.")

        self.esf.shipment()
        self.log.info("----Clicked On Shipment Link----")
        self.lp.loadingScreenHandling()
        self.esf.selectImporter(self.selectIMPORTERData)

        try:
            ShipmentPageText = self.driver.find_element(By.TAG_NAME, "body").text
            entry_summary_count = ShipmentPageText.count("Entry Summary")
            assert entry_summary_count == 10 and 'All' in ShipmentPageText
            self.log.info("Assertion passed: Shipment Page is opened properly")
        except AssertionError:
            self.log.error("Assertion failed: Shipment Page is not opened properly")
            print("Assertion failed: Shipment Page is not opened properly")


        self.qry.query()
        self.log.info("----Clicked On Query Link----")
        self.lp.loadingScreenHandling()
        try:
            QueryPageText = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'All' in QueryPageText
            self.log.info("Assertion passed: Query Page is opened properly")
        except AssertionError:
            self.log.error("Assertion failed: Query Page is not opened properly")
            print("Assertion failed: Shipment Page is not opened properly")

        self.parties.parties()
        self.log.info("----Clicked On Parties Link----")
        self.lp.loadingScreenHandling()
        try:
            PartyPageText = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'All' in PartyPageText
            self.log.info("Assertion passed: Party Page is opened properly")
        except AssertionError:
            self.log.error("Assertion failed: Party Page is not opened properly")
            print("Assertion failed: Party Page is not opened properly")


        self.parts.parts()
        self.log.info("----Clicked On Parts Link----")
        self.lp.loadingScreenHandling()
        try:
            PartsPageText = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'AllPart' in PartsPageText
            self.log.info("Assertion passed: Parts Page is opened properly")
        except AssertionError:
            self.log.error("Assertion failed: Parts Page is not opened properly")
            print("Assertion failed: Parts Page is not opened properly")

        self.stmnt.statements()
        self.log.info("----Clicked On Statements Link----")
        self.lp.loadingScreenHandling()
        try:
            StatementsPageText = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'Statement View' in StatementsPageText
            self.log.info("Assertion passed: Statements Page is opened properly")
        except AssertionError:
            self.log.error("Assertion failed: Statements Page is not opened properly")
            print("Assertion failed: Statements Page is not opened properly")

        self.imprtr.importer()
        self.log.info("----Clicked On Importer Link----")
        self.lp.loadingScreenHandling()
        try:
            ImporterPageText = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'All Importers' in ImporterPageText
            self.log.info("Assertion passed: Importer Page is opened properly")
        except AssertionError:
            self.log.error("Assertion failed: Importer Page is not opened properly")
            print("Assertion failed: Importer Page is not opened properly")

        self.isf.isf()
        self.log.info("----Clicked On ISF Link----")
        self.lp.loadingScreenHandling()
        try:
            ISFPageText = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'ALL' in ISFPageText
            self.log.info("Assertion passed: ISF Page is opened properly")
        except AssertionError:
            self.log.error("Assertion failed: ISF Page is not opened properly")
            print("Assertion failed: ISF Page is not opened properly")

        self.f5106.L5106()
        self.log.info("----Clicked On Form 5106 Link----")
        self.lp.loadingScreenHandling()
        try:
            f5106PageText = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'ALL' in f5106PageText
            self.log.info("Assertion passed: 5106 Page is opened properly")
        except AssertionError:
            self.log.error("Assertion failed: 5106 Page is not opened properly")
            print("Assertion failed: Shipment 5106 is not opened properly")

        self.rprts.reports()
        self.log.info("----Clicked On Reports Link----")
        self.lp.loadingScreenHandling()
        try:
            ReportsPageText = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'CBP HOLD' in ReportsPageText
            self.log.info("Assertion passed: Reports Page is opened properly")
        except AssertionError:
            self.log.error("Assertion failed: Reports Page is not opened properly")
            print("Assertion failed: Reports Page is not opened properly")

        self.invc.invoices()
        self.log.info("----Clicked On Invoices Link----")
        self.lp.loadingScreenHandling()
        try:
            InvoicesPageText = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'Entry Invoices' in InvoicesPageText
            self.log.info("Assertion passed: Invoices Page is opened properly")
        except AssertionError:
            self.log.error("Assertion failed: Invoices Page is not opened properly")
            print("Assertion failed: Invoices Page is not opened properly")

        self.f7512.form7512()
        self.log.info("----Clicked On Form 7512 Link----")
        self.lp.loadingScreenHandling()
        try:
            f7512PageText = self.driver.find_element(By.TAG_NAME, "body").text
            assert 'All' in f7512PageText
            self.log.info("Assertion passed: 7512 Page is opened properly")
        except AssertionError:
            self.log.error("Assertion failed: 7512 Page is not opened properly")
            print("Assertion failed: 7512 Page is not opened properly")

        self.lp.logout()

        self.log.info("----------------Test Case test_AllLinksTest End----------------")



# pytest -v -s testcases/test_AllLinksTest.py
# pytest -v -s testcases/test_AllLinksTest.py --browser chrome
# pytest -v -s testcases/test_AllLinksTest.py --browser firefox
# pytest -v -s --html=reports\test_AllLinksTestReport.html testcases/test_EntryAllLinksTest.py
# pytest -v --html=reports\test_AllLinksTestReport.html testcases/test_EntryAllLinksTest.py
# pytest -v --html=reports\test_AllLinksTestReport.html testcases/test_EntryAllLinksTest.py --browser chrome   #if in html report if logs are not getting genrated then remove -s and try

# pytest -v -s -m "sanity"  --html=reports\report.html testcases/

# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.integration