import time
import pytest
from pages.loginPage import Loginpage
from pages.queryPage import Querypage
from pages.entryformPage import EntryFormPage
from pages.getAttributes import getAtributesOfText
from utilites.utils import utills
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup")
class TestQuery():
    log = utills.custom_logger()  # we can change logging level
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)
        self.qp = Querypage(self.driver, self.mywait)

    def test_Query(self):
        self.log.info("----Test Case test_Query Started----")

        # Login
        #lp = Loginpage(self.driver, self.mywait)
        self.lp.userName("tnash")
        self.lp.password("tnash1")
        self.lp.login()
        self.log.info("----Login Done----")
        time.sleep(4)

        #Go to Query Page
        # self.qp = Querypage(self.driver, self.mywait)
        self.qp.query()
        self.qp.misc()
        self.qp.tariffquery()
        self.log.info("----tariffquery Form Opened----")

        self.qp.hts(8518298000)
        self.qp.dateofquery("2023/09/06")
        self.qp.submitButton()
        time.sleep(10)

        try:
            notonfile=self.driver.find_element(By.XPATH,"//span[text()='Narrative Message:']//parent::div//following-sibling::div[normalize-space()='NOT ON FILE OR EXPIRED']")
            time.sleep(1)
            if notonfile:
                print("This HTS is not on file", 8518298000)
        except:
            print("This HTS is queried", 8518298000)
            time.sleep(1)

        self.log.info("----Test Case test_Query Done----")



# pytest -v -s testcases/test_query.py
# pytest -v -s testcases/test_query.py --browser chrome
# pytest -v -s testcases/test_query.py --browser firefox
# pytest -v -s --html=reports\report.html testcases/test_query.py    #if in html report if logs are not getting genrated then remove -s and try