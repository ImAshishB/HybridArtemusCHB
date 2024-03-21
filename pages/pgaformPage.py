import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver
from utilites.utils import utills

class PGAFormPage(BaseDriver):
    def __init__(self, driver, mywait):
        super().__init__(driver)
        self.driver = driver
        self.mywait = mywait

    # Locators

    #CLick on the PGAs
    EP5Link_XPATH = "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='EP5']"
    EP7Link_XPATH = "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='EP7']"
    FD1Link_XPATH = "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='FD1']"
    FD2Link_XPATH = "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='FD2']"
    FD3Link_XPATH = "//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']//div[@class='col-md-3']//a[normalize-space()='FD3']"

    #PGA Form
    #PG01
    commercialDescription_XPATH = "//label[normalize-space()='Commercial Description:']//parent::div//following-sibling::div//input[@id='commercialDescription']"
    desclaimerDrp_XPATH = "//label[text()='Disclaimer:']//parent::div//following-sibling::div//select[@name='disclaimer']"
    pgaLineValue_XPATH = "//label[text()='PGA Line Value:']//parent::div//following-sibling::div//input[@name='pgaLineValue']"
    agencyProcessingCodeTxt_XPATH = "//label[normalize-space()='Agency Processing Code:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic']"

    #PG19,20
    addEntitiesTxt_XPATH = "//select[@id='entities']"
    selectFD1_XPATH = "//option[normalize-space()='FDA Importer 1 - FD1']"
    selectDP_XPATH = "//option[normalize-space()='Delivery party - DP']"
    selectDFP_XPATH = "//option[normalize-space()='Owner - DFP']"
    selectPNS_XPATH = "//option[normalize-space()='PN Submitter - PNS']"
    selectPNT_XPATH = "//option[normalize-space()='PN Transmitter - PNT']"
    selectFSV_XPATH = "//option[normalize-space()='Foreign Supplier Verification Program - FSV']"
    selectPK_XPATH = "//option[normalize-space()='Point Of Contact - PK']"
    mftTxt_XPATH = "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[1]"
    deqTxt_XPATH = "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[2]"
    fd1Txt_XPATH = "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[3]"
    dpTxt_XPATH = "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[4]"
    dfpTxt_XPATH = "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[4]"
    pnsTxt_XPATH = "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[5]"
    pntTxt_XPATH = "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[6]"
    ucTxt_XPATH = "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[7]"
    fsvTxt_XPATH = "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[8]"
    pkTxt_XPATH = "(//span[normalize-space()='Manufacturer of goods-MF:']//parent::div//following-sibling::div//input[@id='typeahead-basic'])[10]"

    #PG21
    individualQualifierTxt1_XPATH = "//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic']"
    individualQualifierTxt2_XPATH = "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[2]"
    individualQualifierTxt3_XPATH = "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[3]"
    individualQualifierTxt4_XPATH = "(//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic'])[4]"
    mailOrFaxTxt1_XPATH = "//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email']"
    mailOrFaxTxt2_XPATH = "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[2]"
    mailOrFaxTxt3_XPATH = "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[3]"
    mailOrFaxTxt4_XPATH = "(//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email'])[4]"
    individualNameTxt1_XPATH = "//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName']"
    individualNameTxt2_XPATH = "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[2]"
    individualNameTxt3_XPATH = "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[3]"
    individualNameTxt4_XPATH = "(//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName'])[4]"
    telephoneNoTxt1_XPATH = "//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo']"
    telephoneNoTxt2_XPATH = "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[2]"
    telephoneNoTxt3_XPATH = "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[3]"
    telephoneNoTxt4_XPATH = "(//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo'])[4]"
    AddNewIndividualBtn_XPATH = "(//button[contains(text(),'Add New Individual')])[1]"

    # PG02
    itemTypeDrp_XPATH = "//label[text()='Item Type:']//parent::div//following-sibling::div/select[@name='itemType']"
    productcodequalifierDrp_XPATH = "//label[text()='Product Code Qualifier:']//parent::div//following-sibling::div/select[@name='productCodeQualifier']"
    productCodNumberTxt_XPATH = "//label[text()='Product Code Number:']//parent::div//following-sibling::div/input[@name='productCodeNumber']"

    # PG04,05,06
    AddNewConstituent_btn_XPATH = "(//button[contains(text(),'Add New Constituent')])[1]"
    specialUseDesignationDrp1_XPATH = "(//label[text()='Special Use Designation:']//parent::div//following-sibling::div/select[@name='specialUseDesignation'])[1]"
    specialUseDesignationDrp2_XPATH = "(//label[text()='Special Use Designation:']//parent::div//following-sibling::div/select[@name='specialUseDesignation'])[2]"
    sourceTypeCodeDrp1_XPATH = "(//label[text()='Source Type Code:']//parent::div//following-sibling::div/select[@name='sourceTypeCode'])[1]"
    sourceTypeCodeDrp2_XPATH = "(//label[text()='Source Type Code:']//parent::div//following-sibling::div/select[@name='sourceTypeCode'])[2]"
    sourceTypeCodeDrp2Option_XPATH = "(//option[normalize-space()='CSH - CSH - Country of Shipment'])[2]"
    countryCodeTxt1_XPATH = "(//label[text()='Country Code:']//parent::div//following-sibling::div/input[@id='typeahead-basic'])[1]"
    countryCodeTxt2_XPATH = "(//label[text()='Country Code:']//parent::div//following-sibling::div/input[@id='typeahead-basic'])[2]"

    # PG10
    commodityCharacteristicDescriptionTxt_XPATH = "//span[text()='Commodity Characteristic Description:']//parent::div//following-sibling::div/input[@name='commodityCharacteristicDescription']"

    # PG23
    AddNewInfo_Button_XPATH = "//app-affirmation-compliance-list[@class='p-2 ng-valid ng-touched ng-dirty']//button[contains(text(),'Add New Info')]"
    afrmativecodeTxt1_XPATH = "(//select[@id='affirmationComplianceCode'])[1]"
    afrmativecodeTxt1Description_XPATH = "(//input[@id='description'])[1]"
    afrmativecodeTxt2_XPATH = "(//select[@id='affirmationComplianceCode'])[2]"
    afrmativecodeTxt2Description_XPATH = "(//input[@id='description'])[2]"
    afrmativecodeTxt3_XPATH = "(//select[@id='affirmationComplianceCode'])[3]"
    afrmativecodeTxt3Description_XPATH = "(//input[@id='description'])[3]"

    # Opnen PG30
    PG30CollapedSection_XPATH = "//span[text()='Anticipated Arrival Information - PG30']//parent::div"
    inspectionLabTestingStatusDrp_XPATH = "//label[text()='Inspection/Lab Testing Status:']//parent::div//following-sibling::div/select[@name='inspectionTestingStatEntity']"
    scheduledTimeOfInspectionTxt_XPATH = "//label[text()='Requested or Scheduled Time of Inspection; Time of previous Inspection; Arrival Time:']//parent::div//following-sibling::div/input[@name='scheduledTimeOfInspection']"
    scheduledDateOfInspectionTxt_XPATH = "//label[text()='Requested or Scheduled Date of Inspection; Date of previous Inspection; Arrival Date:']//parent::div//following-sibling::div//input[@name='scheduledDateInspection']"
    inspectionorArrivallocationTxt_XPATH = "//label[text()='Inspection or Arrival Location']//parent::div//following-sibling::div//input[@name='inspectionLocation']"
    inspectionorArrivallocationCodeDrp_XPATH = "//label[text()='Inspection or Arrival Location Code::']//parent::div//following-sibling::div/select[@name='arrivalLocationCode']"








    #PG22
    entityRoleCode_XPATH = "//span[text()='Entity Role Code:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic']"
    declarationCode_XPATH = "//span[text()='Declaration Code:']//parent::div//following-sibling::div/input[@name='declarationCode']"
    declarationCertification_XPATH = "//span[text()='Declaration Certification:']//parent::div//following-sibling::div/select[@name='declarationCertification']"
    dateSignature_XPATH = "//span[text()='Date Signature:']//parent::div//following-sibling::div//input[@name='dateSignature']"
    dateSignatureOutClick_XPATH = "//span[normalize-space()='Date Signature:']"

    # PG27
    containerNumberTxt_XPATH = "//input[@id='containerNumber']"

    # PG26
    packagingQualifierDrp_XPATH = "//span[text()='Packaging Qualifier:']//parent::div//following-sibling::div/select[@name='packagingQualifier']"
    unitOfMeasureTxt_XPATH = "//span[text()='Unit of Measure:']//parent::div//following-sibling::div/input[@role='combobox']"
    pgaqtyTxt_XPATH = "//span[text()='Quantity:']//parent::div//following-sibling::div/input[@name='quantity' and@id='quantity' and @maxlength='12']"



    # Save Buttons
    saveAndClosePGAButton_XPATH = "//button[normalize-space()='Save & Close']"
    alertDataIsValidButton_XPATH = "//button[@type='button'][normalize-space()='Save & Close']"
    alertSomeValidationIssueButton_XPATH = "//button[@type='button'][normalize-space()='Save & Close']"
    pgaFormClosedalertOkButton_XPATH = "//button[normalize-space()='OK']"





    # Click on PGA Form
    # PGA form
    def EP5(self):
        ep5Link = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.EP5Link_XPATH)))
        ep5Link.click()
        time.sleep(2)
    def EP7(self):
        ep7Link = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.EP7Link_XPATH)))
        ep7Link.click()
        time.sleep(2)

    def FD1(self):
        fd1Link = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.FD1Link_XPATH)))
        fd1Link.click()
        time.sleep(2)
    def FD2(self):
        fd2Link = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.FD2Link_XPATH)))
        fd2Link.click()
        time.sleep(2)
    def FD3(self):
        fd3Link = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.FD3Link_XPATH)))
        fd3Link.click()
        time.sleep(2)

    # PG01
    def agencyProcessingCode(self,agencyProcessingCodeData):
        agencyProcessingCodeTxt = self.driver.find_element(By.XPATH, self.agencyProcessingCodeTxt_XPATH)
        agencyProcessingCodeTxt.click()
        agencyProcessingCodeTxt.send_keys(agencyProcessingCodeData)
        time.sleep(2)
        agencyProcessingCodeTxt.send_keys(Keys.ENTER)
        time.sleep(1)
    def commercialDescription(self, descriptionData):
        commercialDescriptionTxt = self.driver.find_element(By.XPATH, self.commercialDescription_XPATH)
        commercialDescriptionTxt.send_keys(descriptionData)


    # PG19
    def addEntities(self):
        addEntitiesDrp = self.driver.find_element(By.XPATH, self.addEntitiesTxt_XPATH)
        addEntitiesDrp.click()

    # FD1
    def selectFD1(self):
        selectFD1 = self.driver.find_element(By.XPATH, self.selectFD1_XPATH)
        selectFD1.click()

    #DP
    def selectDP(self):
        selectDP = self.driver.find_element(By.XPATH, self.selectDP_XPATH)
        selectDP.click()
    # DFP
    def selectDFP(self):
        selectDFP = self.driver.find_element(By.XPATH, self.selectDFP_XPATH)
        selectDFP.click()
    # PNS
    def selectPNS(self):
        selectPNS = self.driver.find_element(By.XPATH, self.selectPNS_XPATH)
        selectPNS.click()
    #PNT
    def selectPNT(self):
        selectPNT = self.driver.find_element(By.XPATH, self.selectPNT_XPATH)
        selectPNT.click()
    #FSV
    def selectFSV(self):
        selectFSV = self.driver.find_element(By.XPATH, self.selectFSV_XPATH)
        selectFSV.click()
    #PK
    def selectPK(self):
        selectPK = self.driver.find_element(By.XPATH, self.selectPK_XPATH)
        selectPK.click()
    def mf(self, EntityMFData):
        mf = self.driver.find_element(By.XPATH,self.mftTxt_XPATH)
        mf.click()
        mf.send_keys(EntityMFData)
        time.sleep(2)
        mf.send_keys(Keys.ENTER)
    def deq(self, EntityDEQData):
        deq = self.driver.find_element(By.XPATH,self.deqTxt_XPATH)
        deq.click()
        deq.send_keys(EntityDEQData)
        time.sleep(2)
        deq.send_keys(Keys.ENTER)
    def fd1(self, EntityFD1Data):
        fd1 = self.driver.find_element(By.XPATH,self.fd1Txt_XPATH)
        fd1.click()
        fd1.send_keys(EntityFD1Data)
        time.sleep(2)
        fd1.send_keys(Keys.ARROW_DOWN)
        fd1.send_keys(Keys.ENTER)
    def dfp(self, EntityDFPData):
        dfp = self.driver.find_element(By.XPATH,self.dfpTxt_XPATH)
        dfp.click()
        dfp.send_keys(EntityDFPData)
        time.sleep(2)
        dfp.send_keys(Keys.ARROW_DOWN)
        dfp.send_keys(Keys.ENTER)

    def dp(self, EntityDPData):
        dp = self.driver.find_element(By.XPATH,self.dpTxt_XPATH)
        dp.click()
        dp.send_keys(EntityDPData)
        time.sleep(2)
        dp.send_keys(Keys.ARROW_DOWN)
        dp.send_keys(Keys.ENTER)

    def pns(self,EntityPNSData):
        pns = self.driver.find_element(By.XPATH,self.pnsTxt_XPATH)
        pns.click()
        pns.send_keys(EntityPNSData)
        time.sleep(2)
        pns.send_keys(Keys.ENTER)
    def pnt(self,EntityPNTData):
        pnt = self.driver.find_element(By.XPATH,self.pntTxt_XPATH)
        pnt.click()
        pnt.send_keys(EntityPNTData)
        time.sleep(2)
        pnt.send_keys(Keys.ENTER)
    def uc(self,EntityUCData):
        uc = self.driver.find_element(By.XPATH,self.ucTxt_XPATH)
        uc.click()
        uc.send_keys(EntityUCData)
        time.sleep(2)
        uc.send_keys(Keys.ARROW_DOWN)
        uc.send_keys(Keys.ENTER)
    def fsv(self,EntityFSVData):
        fsv = self.driver.find_element(By.XPATH,self.fsvTxt_XPATH)
        fsv.click()
        fsv.send_keys(EntityFSVData)
        time.sleep(2)
        fsv.send_keys(Keys.ENTER)
    def pk(self,EntityPKData):
        pk = self.driver.find_element(By.XPATH,self.pkTxt_XPATH)
        pk.click()
        pk.send_keys(EntityPKData)
        time.sleep(2)
        pk.send_keys(Keys.ENTER)

    def desclaimer(self,disclaimerdata):
        desclaimerDrp = self.driver.find_element(By.XPATH,self.desclaimerDrp_XPATH)
        desclaimerDrp.click()
        time.sleep(1)
        desclaimerDrp.send_keys(disclaimerdata)
        time.sleep(1)
        desclaimerDrp.send_keys(Keys.ENTER)
    def pgaLineValue(self, pgaLineValueData):
        pgaLineValueTxt = self.driver.find_element(By.XPATH, self.pgaLineValue_XPATH)
        pgaLineValueTxt.send_keys(pgaLineValueData)

    # PG21
    def addNewIndividual(self):
        addNewIndividual = self.driver.find_element(By.XPATH, self.AddNewIndividualBtn_XPATH)
        addNewIndividual.click()
    def individualQualifier(self, individualQualifier1Data):
        individualQualifierTxt1 = self.driver.find_element(By.XPATH, self.individualQualifierTxt1_XPATH)
        individualQualifierTxt1.send_keys(individualQualifier1Data)
        time.sleep(2)
        individualQualifierTxt1.send_keys(Keys.ENTER)
    def individualQualifier2(self, individualQualifier2Data):
        individualQualifierTxt2 = self.driver.find_element(By.XPATH, self.individualQualifierTxt2_XPATH)
        individualQualifierTxt2.send_keys(individualQualifier2Data)
        time.sleep(2)
        individualQualifierTxt2.send_keys(Keys.ENTER)
    def individualQualifier3(self, individualQualifier3Data):
        individualQualifierTxt3 = self.driver.find_element(By.XPATH, self.individualQualifierTxt3_XPATH)
        individualQualifierTxt3.send_keys(individualQualifier3Data)
        time.sleep(2)
        individualQualifierTxt3.send_keys(Keys.ENTER)
    def individualQualifier4(self, individualQualifier4Data):
        individualQualifierTxt4 = self.driver.find_element(By.XPATH, self.individualQualifierTxt4_XPATH)
        individualQualifierTxt4.send_keys(individualQualifier4Data)
        time.sleep(2)
        individualQualifierTxt4.send_keys(Keys.ENTER)
    def mailOrFax(self, mailOrFax1Data):
        mailOrFaxTxt1 = self.driver.find_element(By.XPATH, self.mailOrFaxTxt1_XPATH)
        mailOrFaxTxt1.send_keys(mailOrFax1Data)
    def mailOrFax2(self, mailOrFax2Data):
        mailOrFaxTxt2 = self.driver.find_element(By.XPATH, self.mailOrFaxTxt2_XPATH)
        mailOrFaxTxt2.send_keys(mailOrFax2Data)
    def mailOrFax3(self, mailOrFax3Data):
        mailOrFaxTxt3 = self.driver.find_element(By.XPATH, self.mailOrFaxTxt3_XPATH)
        mailOrFaxTxt3.send_keys(mailOrFax3Data)
    def mailOrFax4(self, mailOrFax4Data):
        mailOrFaxTxt4 = self.driver.find_element(By.XPATH, self.mailOrFaxTxt4_XPATH)
        mailOrFaxTxt4.send_keys(mailOrFax4Data)
    def individualName(self, individualName1Data):
        individualNameTxt1 = self.driver.find_element(By.XPATH, self.individualNameTxt1_XPATH)
        individualNameTxt1.send_keys(individualName1Data)
    def individualName2(self, individualName2Data):
        individualNameTxt2 = self.driver.find_element(By.XPATH, self.individualNameTxt2_XPATH)
        individualNameTxt2.send_keys(individualName2Data)
    def individualName3(self, individualName3Data):
        individualNameTxt3 = self.driver.find_element(By.XPATH, self.individualNameTxt3_XPATH)
        individualNameTxt3.send_keys(individualName3Data)
    def individualName4(self, individualName4Data):
        individualNameTxt4 = self.driver.find_element(By.XPATH, self.individualNameTxt4_XPATH)
        individualNameTxt4.send_keys(individualName4Data)
    def telephoneNo(self, telephoneNo1Data):
        telephoneNumberTxt1 = self.driver.find_element(By.XPATH, self.telephoneNoTxt1_XPATH)
        telephoneNumberTxt1.send_keys(telephoneNo1Data)
    def telephoneNo2(self, telephoneNo2Data):
        telephoneNumberTxt2 = self.driver.find_element(By.XPATH, self.telephoneNoTxt2_XPATH)
        telephoneNumberTxt2.send_keys(telephoneNo2Data)
    def telephoneNo3(self, telephoneNo3Data):
        telephoneNumberTxt2 = self.driver.find_element(By.XPATH, self.telephoneNoTxt3_XPATH)
        telephoneNumberTxt2.send_keys(telephoneNo3Data)
    def telephoneNo4(self, telephoneNo4Data):
        telephoneNumberTxt2 = self.driver.find_element(By.XPATH, self.telephoneNoTxt4_XPATH)
        telephoneNumberTxt2.send_keys(telephoneNo4Data)

    #PG02
    def itemType(self, itemTypeData):
        itemTypeDrp = self.driver.find_element(By.XPATH, self.itemTypeDrp_XPATH)
        itemTypeDrp.click()
        time.sleep(1)
        itemTypeDrp.send_keys(itemTypeData)
        time.sleep(1)
    def productcodequalifier(self, productcodequalifierData):
        productcodequalifier = self.driver.find_element(By.XPATH, self.productcodequalifierDrp_XPATH)
        productcodequalifier.click()
        time.sleep(1)
        productcodequalifier.send_keys(productcodequalifierData)
        time.sleep(1)
    def productcodenumber(self, productcodenumberData):
        productcodenumber = self.driver.find_element(By.XPATH, self.productCodNumberTxt_XPATH)
        productcodenumber.send_keys(productcodenumberData)

    # PG04,05,06
    def click_AddNewConstituent_btn(self):
        AddNewConstituent_btn = self.driver.find_element(By.XPATH, self.AddNewConstituent_btn_XPATH)
        AddNewConstituent_btn.click()
    def specialUseDesignation1(self, SpecialUseDesignationData1):
        specialUseDesignationTxt1 = self.driver.find_element(By.XPATH, self.specialUseDesignationDrp1_XPATH)
        specialUseDesignationTxt1.click()
        time.sleep(1)
        specialUseDesignationTxt1.send_keys(SpecialUseDesignationData1)
        time.sleep(1)
        specialUseDesignationTxt1.send_keys(Keys.ENTER)

    def specialUseDesignation2(self, SpecialUseDesignationData2):
        specialUseDesignationTxt2 = self.driver.find_element(By.XPATH, self.specialUseDesignationDrp2_XPATH)
        specialUseDesignationTxt2.click()
        time.sleep(1)
        specialUseDesignationTxt2.send_keys(SpecialUseDesignationData2)
        time.sleep(1)
        specialUseDesignationTxt2.send_keys(Keys.ENTER)

    def sourceTypeCode1(self, sourceTypeCodeData1):
        sourceTypeCodeTxt1 = self.driver.find_element(By.XPATH, self.sourceTypeCodeDrp1_XPATH)
        sourceTypeCodeTxt1.click()
        time.sleep(1)
        sourceTypeCodeTxt1.send_keys(sourceTypeCodeData1)
        time.sleep(1)
        sourceTypeCodeTxt1.send_keys(Keys.ENTER)
    def sourceTypeCode2(self):
        sourceTypeCodeTxt2 = self.driver.find_element(By.XPATH, self.sourceTypeCodeDrp2_XPATH)
        sourceTypeCodeTxt2.click()
        time.sleep(1)
        sourceTypeCodeDrp2Option = self.driver.find_element(By.XPATH, self.sourceTypeCodeDrp2Option_XPATH)
        time.sleep(1)
        sourceTypeCodeDrp2Option.click()
    def countryCode1(self, CountryCodeData1):
        countryCodeTxt1 = self.driver.find_element(By.XPATH, self.countryCodeTxt1_XPATH)
        countryCodeTxt1.click()
        countryCodeTxt1.send_keys(CountryCodeData1)
        time.sleep(2)
        countryCodeTxt1.send_keys(Keys.ENTER)
    def countryCode2(self, CountryCodeData2):
        countryCodeTxt1 = self.driver.find_element(By.XPATH, self.countryCodeTxt2_XPATH)
        countryCodeTxt1.click()
        countryCodeTxt1.send_keys(CountryCodeData2)
        time.sleep(2)
        countryCodeTxt1.send_keys(Keys.ENTER)

    # PG10
    def commodityCharacteristicDescription(self,commodityCharDescripData):
        commodityCharacteristicDescription =  self.driver.find_element(By.XPATH,self.commodityCharacteristicDescriptionTxt_XPATH)
        commodityCharacteristicDescription.send_keys(commodityCharDescripData)

    # PG23
    def click_AddNewInfo_Button(self):
        self.driver.find_element(By.XPATH, self.AddNewInfo_Button_XPATH).click()
    def afrmativecode1(self, afrmativecodeData1):
        afrmativecodeTxt1 = self.driver.find_element(By.XPATH, self.afrmativecodeTxt1_XPATH)
        afrmativecodeTxt1.click()
        time.sleep(1)
        afrmativecodeTxt1.send_keys(afrmativecodeData1)
        time.sleep(1)
        afrmativecodeTxt1.send_keys(Keys.ENTER)
    def afrmativecode2(self, afrmativecodeData2):
        afrmativecodeTxt2 = self.driver.find_element(By.XPATH, self.afrmativecodeTxt2_XPATH)
        afrmativecodeTxt2.click()
        time.sleep(1)
        afrmativecodeTxt2.send_keys(afrmativecodeData2)
        time.sleep(1)
        afrmativecodeTxt2.send_keys(Keys.ENTER)
    def afrmativecode3(self, afrmativecodeData3):
        afrmativecodeTxt3 = self.driver.find_element(By.XPATH, self.afrmativecodeTxt3_XPATH)
        afrmativecodeTxt3.click()
        time.sleep(1)
        afrmativecodeTxt3.send_keys(afrmativecodeData3)
        time.sleep(1)
        afrmativecodeTxt3.send_keys(Keys.ENTER)
    def afrmativecode1Description(self, afrmativecodeData1):
        afrmativecodeTxt1Description = self.driver.find_element(By.XPATH, self.afrmativecodeTxt1Description_XPATH)
        afrmativecodeTxt1Description.send_keys(afrmativecodeData1)
    def afrmativecode2Description(self, afrmativecodeData2):
        afrmativecodeTxt2Description = self.driver.find_element(By.XPATH, self.afrmativecodeTxt2Description_XPATH)
        afrmativecodeTxt2Description.send_keys(afrmativecodeData2)
    def afrmativecode3Description(self, afrmativecodeData3):
        afrmativecodeTxt3Description = self.driver.find_element(By.XPATH, self.afrmativecodeTxt3Description_XPATH)
        afrmativecodeTxt3Description.send_keys(afrmativecodeData3)

    # PG30
    def openPG30Section(self):
        PG30CollapedSection = self.driver.find_element(By.XPATH, self.PG30CollapedSection_XPATH)
        PG30CollapedSection.click()
        time.sleep(1)
    def inspectionLabTestingStatus(self, inspectionLabTestingStatusData):
        inspectionLabTestingStatusDrp = self.driver.find_element(By.XPATH, self.inspectionLabTestingStatusDrp_XPATH)
        inspectionLabTestingStatusDrp.click()
        time.sleep(1)
        inspectionLabTestingStatusDrp.send_keys(inspectionLabTestingStatusData)
        time.sleep(1)
        inspectionLabTestingStatusDrp.send_keys(Keys.ENTER)
    def scheduledTimeOfInspection(self, scheduledTimeOfInspectionData):
        scheduledTimeOfInspection = self.driver.find_element(By.XPATH, self.scheduledTimeOfInspectionTxt_XPATH)
        scheduledTimeOfInspection.send_keys(scheduledTimeOfInspectionData)
    def scheduledDateOfInspection(self, scheduledDateOfInspectionData):
        scheduledDateOfInspection = self.driver.find_element(By.XPATH, self.scheduledDateOfInspectionTxt_XPATH)
        scheduledDateOfInspection.send_keys(scheduledDateOfInspectionData)
    def inspectionorArrivallocation(self, inspectionorArrivallocationData):
        inspectionorArrivallocation = self.driver.find_element(By.XPATH, self.inspectionorArrivallocationTxt_XPATH)
        inspectionorArrivallocation.send_keys(inspectionorArrivallocationData)
    def inspectionorArrivallocationCode(self, inspectionorArrivallocationCodeData):
        inspectionorArrivallocationCodeDrp = self.driver.find_element(By.XPATH, self.inspectionorArrivallocationCodeDrp_XPATH)
        inspectionorArrivallocationCodeDrp.click()
        time.sleep(1)
        inspectionorArrivallocationCodeDrp.send_keys(inspectionorArrivallocationCodeData)
        time.sleep(1)
        inspectionorArrivallocationCodeDrp.send_keys(Keys.ENTER)



    #PG22
    def entityRoleCode(self, entityRoleCodeData):
        entityRoleCodeTxt = self.driver.find_element(By.XPATH, self.entityRoleCode_XPATH)
        entityRoleCodeTxt.send_keys(entityRoleCodeData)
        time.sleep(2)
        entityRoleCodeTxt.send_keys(Keys.ENTER)
    def declarationCode(self, declarationCodeData):
        declarationCodeTxt = self.driver.find_element(By.XPATH, self.declarationCode_XPATH)
        declarationCodeTxt.send_keys(declarationCodeData)
    def declarationCertification(self, declarationCertificationData):
        declarationCertificationTxt = self.driver.find_element(By.XPATH, self.declarationCertification_XPATH)
        declarationCertificationTxt.send_keys(declarationCertificationData)
        time.sleep(2)
        declarationCertificationTxt.send_keys(Keys.ENTER)
    def dateSignature(self, dateSignatureData):
        dateSignatureTxt = self.driver.find_element(By.XPATH, self.dateSignature_XPATH)
        dateSignatureTxt.send_keys(dateSignatureData)
        dateSignatureOutClick = self.driver.find_element(By.XPATH, self.dateSignatureOutClick_XPATH)
        dateSignatureOutClick.click()

    # PG27
    def containerNumber(self,containerNumberData):
        containerNumberTxt = self.driver.find_element(By.XPATH, self.containerNumberTxt_XPATH)
        containerNumberTxt.send_keys(containerNumberData)

    # PG26
    def packagingQualifier(self,packagingQualifierData):
        packagingQualifierDrp = self.driver.find_element(By.XPATH,self.packagingQualifierDrp_XPATH)
        packagingQualifierDrp.click()
        time.sleep(1)
        packagingQualifierDrp.send_keys(packagingQualifierData)
        time.sleep(1)
        packagingQualifierDrp.send_keys(Keys.ENTER)
    def unitOfMeasure(self,unitOfMeasureData):
        unitOfMeasureTxt = self.driver.find_element(By.XPATH,self.unitOfMeasureTxt_XPATH)
        unitOfMeasureTxt.send_keys(unitOfMeasureData)
        time.sleep(2)
        unitOfMeasureTxt.send_keys(Keys.ENTER)
    def pgaqtyTxt(self,pgaqtyData):
        pgaqtyTxt = self.driver.find_element(By.XPATH,self.pgaqtyTxt_XPATH)
        pgaqtyTxt.send_keys(pgaqtyData)


    # Save the PGA Form
    def saveAndClosePGA(self):
        saveAndCloseButton = self.driver.find_element(By.XPATH, self.saveAndClosePGAButton_XPATH)
        saveAndCloseButton.click()
        time.sleep(2)

    def alertDataIsValid(self):
        alertDataIsValidButton = self.driver.find_element(By.XPATH, self.alertDataIsValidButton_XPATH)
        alertDataIsValidButton.click()

    def alertSomeValidationIssue(self):
        alertSomeValidationIssueButton = self.driver.find_element(By.XPATH, self.alertSomeValidationIssueButton_XPATH)
        alertSomeValidationIssueButton.click()
    def pgaFormClosedalert(self):
        pgaFormClosedalertOkButton= self.driver.find_element(By.XPATH, self.pgaFormClosedalertOkButton_XPATH)
        pgaFormClosedalertOkButton.click()






