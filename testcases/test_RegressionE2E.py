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
class Test_RegressionE2E():
    randomInvoice = "ABTstRegressionE2E_"+ utills.random_invoceGenerator() # random_invoceGenerator() came from utils
    randomBill = "M" + utills.random_BillGenerator()  # random_BillGenerator() came from utils
    file = "D:/Artmus Spec/Automation_Artemus/TestML.xlsx"
    log = utills.custom_logger()
    list_status = []  # Empty List Veriable


    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)
        self.esf = EntryFormPage(self.driver, self.mywait)
        self.getvalues = getAtributesOfText(self.driver, self.mywait)


    def test_RegressionE2E_SimpleEntry_Vessel_Container(self): # Country of origin india/No Duty HTS(NDC)
        self.log.info("----------------Test Case test_RegressionE2E_SimpleEntry_Vessel_Container with Container Starterd----------------")

        for r in range(3, 4):
            self.selectIMPORTERData = utills.readData(self.file, 'TcHybridArtemusData', r, 140)
            self.addBillbutton = utills.readData(self.file, 'TcHybridArtemusData', r, 2)
            self.lineitmscount = utills.readData(self.file, 'TcHybridArtemusData', r, 3)

            self.usernameData = utills.readData(self.file, 'TcHybridArtemusData', r, 5)
            self.passwordData = utills.readData(self.file, 'TcHybridArtemusData', r, 6)

            # upper part
            self.entfilltypeData = utills.readData(self.file, 'TcHybridArtemusData', r, 7)
            self.actionCData = utills.readData(self.file, 'TcHybridArtemusData', r, 8)
            self.trnpmodeData = utills.readData(self.file, 'TcHybridArtemusData', r, 9)

            # Bill
            self.scacData = utills.readData(self.file, 'TcHybridArtemusData', r, 11)
            # billofladdingNo = utills.readData(file, "Sheet1", r, 12).split(",")
            self.uomData = utills.readData(self.file, 'TcHybridArtemusData', r, 13)#.split(",")
            self.qtyyData = utills.readData(self.file, 'TcHybridArtemusData', r, 14)#.split(",")

            # Vessel Inforrmation
            self.vesselsnameData = utills.readData(self.file, "TcHybridArtemusData", r, 15)
            self.vessellsnoData = utills.readData(self.file, "TcHybridArtemusData", r, 16)
            self.containerscount = utills.readData(self.file, "TcHybridArtemusData", r, 4)
            self.containerlistData = utills.readData(self.file, "TcHybridArtemusData", r, 17)

            # Trading Partners 1
            self.manufacturerData = utills.readData(self.file, 'TcHybridArtemusData', r, 18)
            self.sellerData = utills.readData(self.file, 'TcHybridArtemusData', r, 19)
            self.consigneeData = utills.readData(self.file, 'TcHybridArtemusData', r, 20)
            self.buyerData = utills.readData(self.file, 'TcHybridArtemusData', r, 21)

            # Trading Partners 2
            self.countryOfOrigin1Data = utills.readData(self.file, 'TcHybridArtemusData', r, 22)
            self.release_portData = utills.readData(self.file, 'TcHybridArtemusData', r, 23)
            self.countryOfExport1Data = utills.readData(self.file, 'TcHybridArtemusData', r, 24)
            self.ladingportData = utills.readData(self.file, 'TcHybridArtemusData', r, 25)
            self.grossWeightData = utills.readData(self.file, 'TcHybridArtemusData', r, 26)
            self.chargedata = utills.readData(self.file, 'TcHybridArtemusData', r, 27)
            self.unladingportData = utills.readData(self.file, 'TcHybridArtemusData', r, 28)
            self.manifestDescriptionData = utills.readData(self.file, 'TcHybridArtemusData', r, 29)
            self.arrivaldateData = utills.readData(self.file, 'TcHybridArtemusData', r, 30)
            self.exportdateData = utills.readData(self.file, 'TcHybridArtemusData', r, 31)
            self.currencyData = utills.readData(self.file, 'TcHybridArtemusData', r, 112)

            # Line Items
            self.invoiceTotalData = utills.readData(self.file, 'TcHybridArtemusData', r, 32)
            self.tariffnoData = utills.readData(self.file, 'TcHybridArtemusData', r, 33)#.split(",")
            self.htsqty1Data = utills.readData(self.file, 'TcHybridArtemusData', r, 34)
            self.htsqty2Data = utills.readData(self.file, 'TcHybridArtemusData', r, 35)
            self.addcaseNumberData = utills.readData(self.file, 'TcHybridArtemusData', r, 111)
            self.cvdcaseNumberData = utills.readData(self.file, 'TcHybridArtemusData', r, 111)
            self.linevalueData = utills.readData(self.file, 'TcHybridArtemusData', r, 36)#.split(",")
            self.countryOfOrigin2Data = utills.readData(self.file, 'TcHybridArtemusData', r, 37)#.split(",")
            self.countryOfExport2Data = utills.readData(self.file, 'TcHybridArtemusData', r, 38)#.split(",")

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
            self.esf.form7501()
            self.log.info("----Form 7501 Opened----")

            # Upper Part
            self.log.info("----Upper Part Started----")
            self.esf.invoicenumber(self.randomInvoice)
            self.esf.entryFillingTypecode(self.entfilltypeData)
            self.esf.actionCode(self.actionCData)
            self.esf.modeOfTransport(self.trnpmodeData)
            self.log.info("----Upper Part Done----")

            # Bill of Lading
            self.log.info("----Bill Of Lading Started----")
            self.esf.scaccode(self.scacData)
            self.esf.bill(self.randomBill)
            self.esf.uom(self.uomData)
            self.esf.quantity(self.qtyyData)
            self.log.info("----Bill Of Lading Done----")


            # Vessel Inforrmation
            self.log.info("----Vessel Information Started----")
            self.esf.vesselName(self.vesselsnameData)
            self.esf.vesselFlightNo(self.vessellsnoData)
            self.esf.addEditContiner()
            self.esf.containers(self.containerlistData)
            self.esf.saveContainer()
            self.log.info("----Vessel Information Done----")

            # Trading Partners 1
            self.log.info("----Trading Partners 1 Started----")
            self.esf.manufarture(self.manufacturerData)
            self.esf.seller(self.sellerData)
            self.esf.consignee(self.buyerData)
            self.esf.buyer(self.buyerData)
            self.log.info("----Trading Partners 1 Done----")

            # Trading Partners 2

            self.log.info("----Trading Partners 2 Started----")
            self.esf.countryOfOrigin1(self.countryOfOrigin1Data)
            self.esf.release_port(self.release_portData)
            self.esf.countryOfExport1(self.countryOfExport1Data)
            self.esf.ladingport(self.ladingportData)
            self.esf.weight(self.grossWeightData)
            self.esf.charges(self.chargedata)
            self.esf.unladingport(self.unladingportData)
            self.esf.manifestDescription(self.manifestDescriptionData)
            self.esf.arrivaldate(self.arrivaldateData)
            self.esf.exportdate(self.exportdateData)
            self.log.info("----Trading Partners 2 Done----")

            # Line Items
            self.log.info("----Line Items Started----")
            self.esf.invoiceTotal(self.invoiceTotalData)
            self.esf.countryOfOrigin2(self.countryOfOrigin2Data)
            self.esf.countryOfExport2(self.countryOfExport2Data)
            self.esf.tariffno(self.tariffnoData)
            self.esf.lineValue(self.linevalueData)
            self.log.info("----Line Items Done----")

            # Save the form
            self.esf.saveform()

            # Verify that form should be saved
            self.msg = self.driver.find_element(By.TAG_NAME, "body").text

            if 'Form saved succesfully!' in self.msg:
                self.esf.formSavedConfirmationMsg()
                self.log.info("----Form Saved Successfully----")
                self.esf.submitform()
                self.log.info("----Clicked on Submit Button----")

                if 'Confirm Entry Information' in self.msg:
                    self.log.info("----Validation Form opened----")
                InvoiceValuesOfValidationForm = self.driver.find_element(By.XPATH,"//p[@class='form-lable'][contains(text(),'Total Invoice Value:')]//span[1]").text
                InvoiceValuesOfValidationFormFloat = float(InvoiceValuesOfValidationForm)
                if InvoiceValuesOfValidationFormFloat != 0:
                    self.log.info("----The values are calculated properly----")
                    self.esf.validationFormsubmitButton()
                    self.log.info("----Clicked on Submit Button of Validation Form----")
                    self.esf.loadingScreenHandling()
                    if 'EDI send successfully' in self.msg:
                        self.esf.validationFormsubmitConfirmationMsg()
                        self.log.info("----Form Submitted Successfully----")
                        self.esf.close()
                    else:
                        self.esf.validationFormsubmitConfirmationMsg()
                        self.log.error("----Form edi sent but Error occured----")


                else:
                    self.log.error("----The values are not calculated properly----")
            else:
                # self.driver.save_screenshot(".\\screenshots\\" + "test_HRegressionE2E_scr.png")  # Screenshot
                self.esf.formSavedConfirmationMsg()
                self.log.error("----Form Not Saved. Test Failed----")

        self.log.info("----------------Test Case test_RegressionE2E_SimpleEntry_Vessel_Container with Container End----------------")



# pytest -v -s testcases/test_EntryRegressionE2E.py
# pytest -v -s testcases/test_EntryRegressionE2E.py --browser chrome
# pytest -v -s testcases/test_EntryRegressionE2E.py --browser firefox
# pytest -v -s --html=reports\EntryRegressionE2EReport.html testcases/test_EntryRegressionE2E.py
# pytest -v --html=reports\EntryRegressionE2EReport.html testcases/test_EntryRegressionE2E.py
# pytest -v --html=reports\EntryRegressionE2EReport.html testcases/test_EntryRegressionE2E.py --browser chrome   #if in html report if logs are not getting genrated then remove -s and try
# pytest -v -s -n=1 --html=reports\report.html testcases/test_Login.py    n=1 means each test cases running 1 by 1
# pytest -v -s -n=2 --html=reports\report.html testcases/test_Login.py    n=2 means 2 test cases running at a time in 2 browsers

# pytest -v -s -m "sanity"  --html=reports\report.html testcases/

# @pytest.mark.sanity
# @pytest.mark.regression
# @pytest.mark.integration