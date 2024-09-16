import time
import pytest
from pages.loginPage import Loginpage
from pages.entryformPage import EntryFormPage
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
class Test_DEMO1(): # for class the Test name should be in capital
    randomInvoice = "ABTstTC1_Vsl_"+ utills.random_invoceGenerator() # random_invoceGenerator() came from utils
    randomBill = "M" + utills.random_BillGenerator()  # random_BillGenerator() came from utils
    file = "D:/Artmus Spec/Automation_Artemus/TestML.xlsx"
    log = utills.custom_logger()
    list_status = []  # Empty List Veriable


    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)
        self.esf = EntryFormPage(self.driver, self.mywait)
        self.getvalues = getAtributesOfText(self.driver, self.mywait)


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_DEMOTC_01_LoginOnly(self): # Country of origin india/No Duty HTS(NDC)
        self.log.info("----------------Test Case test_DEMOTC_01_LoginOnly Starterd----------------")

        for r in range(3, 4):
            self.selectIMPORTERData = utills.readData(self.file, 'TcHybridArtemusData', r, 140)

            self.usernameData = utills.readData(self.file, 'TcHybridArtemusData', r, 5)
            self.passwordData = utills.readData(self.file, 'TcHybridArtemusData', r, 6)

            # upper part
            self.entfilltypeData = utills.readData(self.file, 'TcHybridArtemusData', r, 7)
            self.actionCData = utills.readData(self.file, 'TcHybridArtemusData', r, 8)
            self.trnpmodeData = utills.readData(self.file, 'TcHybridArtemusData', r, 9)

            # Vessel Inforrmation
            self.vesselsnameData = utills.readData(self.file, "TcHybridArtemusData", r, 15)
            self.vessellsnoData = utills.readData(self.file, "TcHybridArtemusData", r, 16)
            self.containerscount = utills.readData(self.file, "TcHybridArtemusData", r, 4)
            self.containerlistData = utills.readData(self.file, "TcHybridArtemusData", r, 17)

            # Login
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            self.log.info("----Login Done----")
            self.lp.loadingScreenHandling()
        self.log.info("----------------Test Case test_DEMOTC_01_LoginOnly End----------------")

    @pytest.mark.regression
    def test_DEMOTC_02_HomePageOnly(self): # Country of origin india/No Duty HTS(NDC)
        self.log.info("----------------Test Case test_DEMOTC_02_HomePageOnly Starterd----------------")

        for r in range(3, 4):
            self.selectIMPORTERData = utills.readData(self.file, 'TcHybridArtemusData', r, 140)

            self.usernameData = utills.readData(self.file, 'TcHybridArtemusData', r, 5)
            self.passwordData = utills.readData(self.file, 'TcHybridArtemusData', r, 6)

            # upper part
            self.entfilltypeData = utills.readData(self.file, 'TcHybridArtemusData', r, 7)
            self.actionCData = utills.readData(self.file, 'TcHybridArtemusData', r, 8)
            self.trnpmodeData = utills.readData(self.file, 'TcHybridArtemusData', r, 9)

            # Login
            self.lp.userName(self.usernameData)
            self.lp.password(self.passwordData)
            self.lp.login()
            self.log.info("----Login Done----")
            self.lp.loadingScreenHandling()

            # Go to 7501 Page
            # self.esf = EntryFormPage(self.driver, self.mywait)
            self.esf.shipment()
            self.esf.selectImporter(self.selectIMPORTERData)

        self.log.info("----------------Test Case test_DEMOTC_02_HomePageOnly End----------------")



# pytest -v -s testcases/test_DEMO1.py
# pytest -v -s testcases/test_EntryTC1.py
# pytest -v -s testcases/test_DEMO1.py --browser chrome
# pytest -v -s testcases/test_DEMO1.py --browser firefox
# pytest -v -s --html=reports\EntryTC1Report.html testcases/test_DEMO1.py
# pytest -v --html=reports\EntryTC1Report.html testcases/test_DEMO1.py
# pytest -v --html=reports\EntryTC1Report.html testcases/test_DEMO1.py --browser chrome   #if in html report if logs are not getting genrated then remove -s and try
# pytest -v -s -n=1 --html=reports\report.html testcases/test_DEMO1.py    n=1 means each test cases running 1 by 1
# pytest -v -s -n=2 --html=reports\report.html testcases/test_DEMO1.py    n=2 means 2 test cases running at a time in 2 browsers




