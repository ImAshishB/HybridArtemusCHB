import time
import pytest
from pages.loginPage import Loginpage
from pages.entryformPage import EntryFormPage
from pages.getAttributes import getAtributesOfText
from pages.pgaformPage import PGAFormPage
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
class Test_EntrySummary16():
    randomInvoice = "ABTstTC16_PGA3F_"+ utills.random_invoceGenerator() # random_invoceGenerator() came from utils
    randomBill = "M" + utills.random_BillGenerator()  # random_BillGenerator() came from utils
    file = "D:/Artmus Spec/Automation_Artemus/TestML.xlsx"
    log = utills.custom_logger()
    list_status = []  # Empty List Veriable


    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lp = Loginpage(self.driver, self.mywait)
        self.esf = EntryFormPage(self.driver, self.mywait)
        self.getvalues = getAtributesOfText(self.driver, self.mywait)
        self.pga = PGAFormPage(self.driver, self.mywait)


    def test_TC16_3FPGA_Vessel_Container(self):
        self.log.info("----------------Test Case test_TC16_3FPGA_Vessel_Container Starterd----------------")

        for r in range(18, 19):


            # Login

            # Add PGA Detail


            #PG01
            self.FD1agencyProcessingCodeData = utills.readData(self.file, "TcHybridArtemusData", r, 54)
            self.FD1pgaLineValueData = utills.readData(self.file, "TcHybridArtemusData", r, 55)
            self.FD1descriptionData = utills.readData(self.file, "TcHybridArtemusData", r, 56)

            #PG19
            self.FD1EntityMF = utills.readData(self.file, "TcHybridArtemusData", r, 58)
            self.FD1EntityDEQ = utills.readData(self.file, "TcHybridArtemusData", r, 59)
            self.FD1EntityFD1 = utills.readData(self.file, "TcHybridArtemusData", r, 60)
            self.FD1EntityDP = utills.readData(self.file, "TcHybridArtemusData", r, 61)

            # PG21
            self.FD1individualQualifierData1 = utills.readData(self.file, "TcHybridArtemusData", r, 68)
            self.FD1mailOrFaxData1 = utills.readData(self.file, "TcHybridArtemusData", r, 69)
            self.FD1individualNameData1 = utills.readData(self.file, "TcHybridArtemusData", r, 70)
            self.FD1telephoneNoData1 = utills.readData(self.file, "TcHybridArtemusData", r, 71)

            # PG02
            self.FD1itemTypeData = utills.readData(self.file, "TcHybridArtemusData", r, 73)
            self.FD1productcodequalifierData = utills.readData(self.file, "TcHybridArtemusData", r, 74)
            self.FD1productcodnumberData = utills.readData(self.file, "TcHybridArtemusData", r, 75)

            # PG26
            self.FD1packagingQualifierData = utills.readData(self.file, "TcHybridArtemusData", r, 77)
            self.FD1unitOfMeasureData = utills.readData(self.file, "TcHybridArtemusData", r, 78)
            self.FD1pg26qtyData = utills.readData(self.file, "TcHybridArtemusData", r, 79)

            # PG4,5,6
            self.FD1SpecialUseDesignationData1 = utills.readData(self.file, "TcHybridArtemusData", r, 81)
            self.FD1sourceTypeCodeData1 = utills.readData(self.file, "TcHybridArtemusData", r, 82)
            self.FD1countryCodeData1 = utills.readData(self.file, "TcHybridArtemusData", r, 83)

            # PG10
            self.FD1commodityCharDescripData = utills.readData(self.file, "TcHybridArtemusData", r, 85)

            # PG23
            self.FD1afrmativecodeData1 = utills.readData(self.file, "TcHybridArtemusData", r, 87)
            self.FD1afrmativedescriptionData1 = utills.readData(self.file, "TcHybridArtemusData", r, 89)
            self.FD1afrmativecodeData2 = utills.readData(self.file, "TcHybridArtemusData", r, 88)
            self.FD1afrmativedescriptionData2 = utills.readData(self.file, "TcHybridArtemusData", r, 90)

            # PG27
            self.FD1containerNumberData = utills.readData(self.file, "TcHybridArtemusData", r, 121)

            # EP5
            self.pga.EP5()
            self.log.info("----PGA EP5 form opened----")
            self.pga.commercialDescription(self.EP7descriptionData)
            self.pga.desclaimer(self.EP5desclaimerdata)
            # SavePGA EP5
            self.pga.saveAndClosePGA()
            try:
                alertDataIsValidMSG = self.driver.find_element(By.XPATH,
                                                               "//div[normalize-space()='1. The Data is Valid...']")
                if alertDataIsValidMSG:
                    self.pga.alertDataIsValid()
            except:
                self.log.error("Error while saving PGA form")
                pass
            time.sleep(1)
            self.pga.pgaFormClosedalert()
            self.esf.minimizeQtySection()
            self.log.info("----PGA EP5 form Closed----")

            #EP7
            self.pga.EP7()
            self.log.info("----PGA EP7 form opened----")
            #PG01
            self.pga.commercialDescription(self.EP7descriptionData)
            self.pga.pgaLineValue(self.EP7pgaLineValueData)

            #PG21
            self.pga.individualQualifier(self.EP7individualQualifierdata)
            self.pga.mailOrFax(self.EP7mailOrFaxdata)
            self.pga.individualName(self.EP7individualNameData)
            self.pga.telephoneNo(self.EP7telephoneNoData)

            #PG23
            self.pga.entityRoleCode(self.EP7entityRoleCodeData)
            self.pga.declarationCode(self.EP7declarationCodeData)
            self.pga.declarationCertification(self.EP7declarationCertificationData)
            self.pga.dateSignature(self.EP7dateSignatureData)

            #SavePGA EP7
            self.pga.saveAndClosePGA()
            try:
                alertDataIsValidMSG = self.driver.find_element(By.XPATH,"//div[normalize-space()='1. The Data is Valid...']")
                if alertDataIsValidMSG:
                    self.pga.alertDataIsValid()
            except:
                self.log.error("Error while saving PGA form")
                pass
            time.sleep(1)
            self.pga.pgaFormClosedalert()
            self.esf.minimizeQtySection()
            self.log.info("----PGA EP7 form closed----")

            # FD3
            self.pga.FD3()
            self.log.info("----PGA FD3 form opened----")
            # PG01
            self.pga.commercialDescription(self.EP7descriptionData)
            self.pga.pgaLineValue(self.EP7pgaLineValueData)

            # PG21
            self.pga.individualQualifier(self.EP7individualQualifierdata)
            self.pga.mailOrFax(self.EP7mailOrFaxdata)
            self.pga.individualName(self.EP7individualNameData)
            self.pga.telephoneNo(self.EP7telephoneNoData)

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

                if InvoiceValuesOfValidationForm != 0:
                    self.log.info("----The values are calculated properly----")
                    self.esf.validationFormsubmitButton()
                    self.log.info("----Clicked on Submit Button of Validation Form----")
                    self.esf.loadingScreenHandling()
                    if 'EDI send successfully' in self.msg:
                        self.esf.validationFormsubmitConfirmationMsg()
                        self.log.info("----Form Submitted Successfully----")
                    else:
                        self.esf.validationFormsubmitConfirmationMsg()
                    self.esf.close()

                else:
                    self.log.error("----The values are not calculated properly----")
            else:
                # self.driver.save_screenshot(".\\screenshots\\" + "test_HTC16_scr.png")  # Screenshot
                self.esf.formSavedConfirmationMsg()
                self.log.error("----Form Not Saved. Test Failed----")

        self.log.info("----------------Test Case test_TC16_3FPGA_Vessel_Container End----------------")



# pytest -v -s testcases/test_EntryTC16.py
# pytest -v -s testcases/test_EntryTC16.py --browser chrome
# pytest -v -s testcases/test_EntryTC16.py --browser firefox
# pytest -v -s --html=reports\EntryTC16Report.html testcases/test_EntryTC16.py
# pytest -v --html=reports\EntryTC16Report.html testcases/test_EntryTC16.py
# pytest -v --html=reports\EntryTC16Report.html testcases/test_EntryTC16.py --browser chrome   #if in html report if logs are not getting genrated then remove -s and try