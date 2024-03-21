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
            # billofladdingNo = utills.readData(file, "TcHybridArtemusData", r, 12).split(",")
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

            # Add PGA Detail

            self.EP5descriptionData = utills.readData(self.file, "TcHybridArtemusData", r, 40)
            self.EP5desclaimerdata = utills.readData(self.file, "TcHybridArtemusData", r, 41)

            self.EP7descriptionData = utills.readData(self.file, "TcHybridArtemusData", r, 43)
            self.EP7pgaLineValueData = utills.readData(self.file, "TcHybridArtemusData", r, 36)

            self.EP7individualQualifierdata = utills.readData(self.file, "TcHybridArtemusData", r, 45)
            self.EP7mailOrFaxdata = utills.readData(self.file, "TcHybridArtemusData", r, 46)
            self.EP7individualNameData = utills.readData(self.file, "TcHybridArtemusData", r, 47)
            self.EP7telephoneNoData = utills.readData(self.file, "TcHybridArtemusData", r, 48)

            self.EP7entityRoleCodeData = utills.readData(self.file, "TcHybridArtemusData", r, 49)
            self.EP7declarationCodeData = utills.readData(self.file, "TcHybridArtemusData", r, 50)
            self.EP7declarationCertificationData = utills.readData(self.file, "TcHybridArtemusData", r, 51)
            self.EP7dateSignatureData = utills.readData(self.file, "TcHybridArtemusData", r, 52)

            #PG01
            self.FD1agencyProcessingCodeData = utills.readData(self.file, "TcHybridArtemusData", r, 54)
            self.FD1pgaLineValueData = utills.readData(self.file, "TcHybridArtemusData", r, 36)
            self.FD1descriptionData = utills.readData(self.file, "TcHybridArtemusData", r, 56)

            #PG19
            self.FD1EntityMFData = utills.readData(self.file, "TcHybridArtemusData", r, 58)
            self.FD1EntityDEQData = utills.readData(self.file, "TcHybridArtemusData", r, 59)
            self.FD1EntityFD1Data = utills.readData(self.file, "TcHybridArtemusData", r, 60)
            self.FD1EntityDPData = utills.readData(self.file, "TcHybridArtemusData", r, 61)

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
            self.FD1pg26qtyData = utills.readData(self.file, "TcHybridArtemusData", r, 14)

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

            # PG23
            self.FD1inspLabTestData = utills.readData(self.file, "Sheet1", r, 92)
            self.FD1schedTimeOfInspecData = utills.readData(self.file, "Sheet1", r, 93)
            self.FD1scheduledDateOfInspectionData = utills.readData(self.file, "Sheet1", r, 94)
            self.FD1inspectionorArrivallocationData = utills.readData(self.file, "Sheet1", r, 95)
            self.FD1inspectionorArrivallocationCodeData = utills.readData(self.file, "Sheet1", r, 96)

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
            self.pga.commercialDescription(self.FD1descriptionData)
            self.pga.agencyProcessingCode(self.FD1agencyProcessingCodeData)
            self.pga.pgaLineValue(self.FD1pgaLineValueData)

            # PG19
            self.pga.selectFD1()
            self.pga.selectDP()
            #Fill Data in PG19
            self.pga.mf(self.FD1EntityMFData)
            self.pga.deq(self.FD1EntityDEQData)
            self.pga.fd1(self.FD1EntityFD1Data)
            self.pga.dp(self.FD1EntityDPData)

            # PG21
            self.pga.individualQualifier(self.FD1individualQualifierData1)
            self.pga.mailOrFax(self.FD1mailOrFaxData1)
            self.pga.individualName(self.FD1individualNameData1)
            self.pga.telephoneNo(self.FD1telephoneNoData1)

            # PG02
            self.pga.itemType(self.FD1itemTypeData)
            self.pga.productcodequalifier(self.FD1productcodequalifierData)
            self.pga.productcodenumber(self.FD1productcodnumberData)

            # PG26
            self.pga.packagingQualifier(self.FD1packagingQualifierData)
            self.pga.unitOfMeasure(self.FD1unitOfMeasureData)
            self.pga.pgaqtyTxt(self.FD1pg26qtyData)

            # PG04,05,06
            self.pga.specialUseDesignation1(self.FD1SpecialUseDesignationData1)
            self.pga.sourceTypeCode1(self.FD1sourceTypeCodeData1)
            self.pga.countryCode1(self.FD1countryCodeData1)

            # PG10
            self.pga.commodityCharacteristicDescription(self.FD1commodityCharDescripData)

            # PG23
            self.pga.click_AddNewInfo_Button()
            self.pga.afrmativecode1(self.FD1afrmativecodeData1)
            self.pga.afrmativecode1Description(self.FD1afrmativedescriptionData1)
            self.pga.afrmativecode2(self.FD1afrmativecodeData2)
            self.pga.afrmativecode2Description(self.FD1afrmativedescriptionData2)

            # PG23
            self.pga.openPG30Section()
            self.pga.inspectionLabTestingStatus(self.FD1inspLabTestData)
            self.pga.scheduledTimeOfInspection(self.FD1schedTimeOfInspecData)
            self.pga.scheduledDateOfInspection(self.FD1scheduledDateOfInspectionData)
            self.pga.inspectionorArrivallocation(self.FD1inspectionorArrivallocationData)
            self.pga.inspectionorArrivallocationCode(self.FD1inspectionorArrivallocationCodeData)

            #PG27
            self.pga.containerNumber(self.FD1containerNumberData)

            # SavePGA FD3
            self.pga.saveAndClosePGA()
            try:
                alertDataIsValidMSG = self.driver.find_element(By.XPATH,
                                                               "//div[normalize-space()='1. The Data is Valid...']")
                if alertDataIsValidMSG:
                    self.pga.alertDataIsValid()
            except:
                self.log.error("Error while saving PGA form")
                pass
            try:
                someValidationsError = self.driver.find_element(By.TAG_NAME, "body").text
                if 'The Manufacturer record should have an entity number' in someValidationsError:
                    self.pga.alertSomeValidationIssue()
                    time.sleep(1)
                    print("PGA has some validations issues but still PGA form saved")
            except Exception as e:
                print("PGA has issues and PGA form saved")
                print(e)
            time.sleep(1)
            self.pga.pgaFormClosedalert()
            self.esf.minimizeQtySection()
            self.log.info("----PGA FD3 form closed----")


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
                        self.esf.close()
                    else:
                        self.esf.validationFormsubmitConfirmationMsg()
                        self.log.error("----Form edi sent but Error occured----")

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