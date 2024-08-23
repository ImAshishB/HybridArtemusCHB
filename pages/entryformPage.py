import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver
from utilites.utils import utills

class EntryFormPage(BaseDriver):
    def __init__(self, driver, mywait):
        super().__init__(driver)
        self.driver = driver
        self.mywait = mywait

    # Locators

    # Select Importer
    selectImporterTxt_XPATH = "//input[@id='typeahead-basic']"

    shipment_LINK_TEXT = "Shipments"
    form7501_LINK_TEXT = "Form 7501"

    # Upper Part locators
    entryfillingtypecodeDrpDwn_ID = "entryFilingTypeCode"
    actionCodeTxt_ID = "actionCode"
    modeOfTransport_ID = "modeOfTransport"
    invoicenumberTxt_CSS = "input#invoiceNumber"
    ivcnumberoutclick_XPATH = "//span[normalize-space()='Invoice Number:']"

    # Bill of lading locators

    BillTypeDRP_XPATH = "(//select[@id='billTypeCode'])[1]"
    scaccodeTxt_XPATH = "//span[text()='SCAC:']//parent::div//following-sibling::div/input[@id='typeahead-basic']"
    billTxt_XPATH = "//input[@name='billOfLading']"
    outclick_XPATH = "//span[normalize-space()='Split Shipment:']"
    uomTxt_XPATH = "//span[text()='UOM:']//parent::div//following-sibling::div/input[@id='typeahead-basic']"
    quantityTxt_XPATH = "//input[@id='quantity']"
    addBillButton_XPATH = "//button[normalize-space()='Add a Bill']"
    # scaccodeTxt_XPATH = "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='scac']"
    # billTxt_XPATH = "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='billOfLading']"
    # outclick_XPATH = "// span[normalize-space()='Split Shipment:']"
    # uomTxt_XPATH = "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='uom']"
    # quantityTxt_XPATH = "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='quantity']"
    # addBillButton_XPATH = "//button[normalize-space()='Add a Bill']"

    # In Bound Information
    itNumberTxt_XPATH = "//app-inbound-transportation//input[@id='itNumber']"
    itDateTxt_XPATH = "//app-inbound-transportation//input[@name='docsReceivedDate']"
    portOfUnLadingTxt_XPATH = "//app-inbound-transportation//input[@id='portofUnlading']"
    itBOLDrp_XPATH = "//app-inbound-transportation//select[@id='itBol']"

    # Vessel Inforrmation locators
    vesselNameTxt_CSS = "input#vesselName"
    vesselFlightNoTxt_CSS = "input#vesselFlightNo"
    addEditContiner_link_XPATH = "// a[contains(text(), 'Add/Edit container')]"
    containerTxt_XPATH = "//app-vessel-container//div[@class='row new-form-row'][1]//div[@class='col-md-4 form-lable'][1]//input[@type='text']"
    AddNewContainerButton_XPATH = "//app-vessel-container//div[@class='row new-form-row'][4]//button[normalize-space()='Add new container']"
    saveContainerButton_XPATH = "//button[@type='button'][normalize-space()='Save']"

    # Trading Partners 1 locators
    manufacturerTxt_NAME = "manufacturer"
    sellerTxt_NAME = "seller"
    consigneeTxt_XPATH = "//input[@name='consignee']"
    buyerTxt_XPATH = "//input[@name='buyer']"

    # Save Form Locators
    saveButton_XPATH = "//button[contains(text(),'Save')]"

    # Trading Partners 2 locators
    countryOfOriginTxt1_XPATH = "//div[@class='formBorderBill']//div[@class='row new-form-row'][1]//div[@class='col-md-3 form-lable'][2]//input[@id='typeahead-basic']"
    release_portTxt_Name = "releasePort"
    selectCurrencyTxt_XPATH = "//div[@class='formBorderBill']//input[@name='currency']"
    selectCurrencyOutclick_XPATH = "//div[@class='formBorderBill']//span[contains(text(),'Currency:')]"
    countryOfExportTxt1_XPATH = "//div[@class='formBorderBill']//div[@class='row new-form-row'][2]//div[@class='col-md-3 form-lable'][2]//input[@id='typeahead-basic']"
    ladingportTxt_XPATH = "//div[@class='formBorderBill']//div[@class='row new-form-row'][4]//div[@class='col-md-3 form-lable'][1]//input[@id='typeahead-basic']"
    weightTxt_ID = "grossWeight"
    chargesTxt_NAME = "charges"
    unladingportTxt_XPATH = "//div[@class='formBorderBill']//div[@class='row new-form-row'][5]//div[@class='col-md-3 form-lable'][1]//input[@id='typeahead-basic']"
    manifestDescriptionTxt_NAME  = "manifestDescription"
    arrivaldateBox_XPATH = "//input[@name='arrivalDate']"
    exportdateBox_XPATH = "//input[@name='exportDate']"
    selectCurrencyOutClick_XPATH = "//div[@class='formBorderBill']//span[contains(text(),'Currency:')]"

    # Line Items Locators
    invoiceTotalTxt_CSS = "input#invoiceTotal"
    tariffnoTxt_XPATH = "//span[text()='Tariff #1:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @class='form-control ng-untouched ng-pristine ng-valid']"
    countryOfOriginTxt2_XPATH = "//span[text()='Country of Origin:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @required]"
    countryOfExportTxt2_XPATH = "//span[text()='Country of Export:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @required]"
    linevaluesaddTxt_XPATH = "//span[text()='Line Value (USD):']//parent::div//following-sibling::div/input[@name='linevalue']"
    addlineitembutton_XPATH = "//button[normalize-space()='Add New Line']"
    partTxt_XPATH = "//span[text()='Part:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @class='form-control ng-untouched ng-pristine ng-valid']"
    foreignLineValueTxt_XPATH = "//span[text()='Foreign Line Value:']//parent::div//following-sibling::div/input[@name='linevalue']"
    foreignLineValueOutClick_XPATH = "//span[text()='Foreign Line Value:']"
    NumberOfLineItem_XPATH = "//button[@aria-expanded='true' and @class='btn btn-link']//div[2]"
    textOfHTSWhenCollapsed_XPATH="//button[@class='btn btn-link container-fluid text-left pl-0 collapsed']/div/div[1]/span"
    textOfHTSWhenCollapsed_XPATH_ForChina = "(//button[@class='btn btn-link container-fluid text-left pl-0 collapsed'])[2]/div/div[1]/span"
    textOfHTSWhenExpanded_XPATH = "//button[@class='btn btn-link container-fluid text-left pl-0']/div/div[1]/span"
    textOfHTSWhenExpanded_XPATH_ForChina = "(//button[@class='btn btn-link container-fluid text-left pl-0'])[2]/div/div[1]/span"

    # Home Page
    def selectImporter(self, selectImporterData):
        selectImporterTxt = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.selectImporterTxt_XPATH)))
        selectImporterTxt.click()
        selectImporterTxt.send_keys(selectImporterData)
        time.sleep(2)
        selectImporterTxt.send_keys(Keys.BACKSPACE)
        time.sleep(2)
        selectImporterTxt.send_keys(Keys.ENTER)
        time.sleep(2)
    def shipment(self):
        shipmentlink = self.mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.shipment_LINK_TEXT)))
        shipmentlink.click()
        time.sleep(2)
    def form7501(self):
        form7501link = self.mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.form7501_LINK_TEXT)))
        form7501link.click()
        time.sleep(1)

    # Entry Summary Form
    # Upper Part
    def entryFillingTypecode(self, entfilltype):
        entryfillingtypecodeDrpDwn = self.driver.find_element(By.ID, self.entryfillingtypecodeDrpDwn_ID)
        entryfillingtypecodeDrpDwn.click()
        entryfillingtypecodeDrpDwn.send_keys(entfilltype)
        entryfillingtypecodeDrpDwn.send_keys(Keys.ENTER)
    def actionCode(self, actionC):
        actionCodeTxt = self.driver.find_element(By.ID, self.actionCodeTxt_ID)
        actionCodeTxt.click()
        actionCodeTxt.send_keys(actionC)
        actionCodeTxt.send_keys(Keys.ENTER)
    def modeOfTransport(self, trnpmode):
        if trnpmode != 11:
            modeOfTransportDrpDwn = self.driver.find_element(By.ID, self.modeOfTransport_ID)
            modeOfTransportDrpDwn.click()
            modeOfTransportDrpDwn.send_keys(trnpmode)
            modeOfTransportDrpDwn.send_keys(Keys.ENTER)
    def invoicenumber(self,invoiceno):
        ivcnumberTxt = self.driver.find_element(By.CSS_SELECTOR, self.invoicenumberTxt_CSS)
        ivcnumberTxt.send_keys(invoiceno)
        time.sleep(1)
        ivcnumberoutclick = self.driver.find_element(By.XPATH, self.ivcnumberoutclick_XPATH)
        ivcnumberoutclick.click()
        time.sleep(2)

    # Bill of Lading


    def BillTypeRegular(self):
        BillTypeDRP = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.BillTypeDRP_XPATH)))
        BillTypeDRP.click()
        BillTypeDRP.send_keys("r")
        time.sleep(1)
        BillTypeDRP.send_keys(Keys.ENTER)

    def scaccode(self, scac):
        scaccodeTxt = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.scaccodeTxt_XPATH)))
        scaccodeTxt.click()
        scaccodeTxt.send_keys(scac)
        time.sleep(2)
        scaccodeTxt.send_keys(Keys.ENTER)
        time.sleep(1)
    def bill(self, bill):
        # billTxt = self.driver.find_element(By.XPATH, self.billTxt_XPATH)
        billTxt = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.billTxt_XPATH)))
        billTxt.click()
        billTxt.send_keys(bill)
        outclick = self.driver.find_element(By.XPATH, self.outclick_XPATH)
        outclick.click()
        time.sleep(2)
    def uom(self, uom):
        uomTxt = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.uomTxt_XPATH)))
        uomTxt.click()
        uomTxt.send_keys(uom)
        time.sleep(2)
        uomTxt.send_keys(Keys.ENTER)
        time.sleep(1)
    def quantity(self, quantity):
        quantityTxt = self.driver.find_element(By.XPATH, self.quantityTxt_XPATH)
        quantityTxt.click()
        quantityTxt.send_keys(quantity)
    def addBill(self):
        addBillButton = self.driver.find_element(By.XPATH, self.addBillButton_XPATH)
        addBillButton.click()


    # In Bound Information
    def itNumber(self, itNumberData):
        itNumberTxt = self.driver.find_element(By.XPATH, self.itNumberTxt_XPATH)
        itNumberTxt.send_keys(itNumberData)
    def itDate(self, itDateData):
        itDateTxt = self.driver.find_element(By.XPATH, self.itDateTxt_XPATH)
        itDateTxt.send_keys(itDateData)
    def portOfUnLading(self, portOfUnLadingData):
        portOfUnLadingTxt = self.driver.find_element(By.XPATH, self.portOfUnLadingTxt_XPATH)
        portOfUnLadingTxt.click()
        portOfUnLadingTxt.send_keys(portOfUnLadingData)
        time.sleep(2)
        portOfUnLadingTxt.send_keys(Keys.ENTER)
    def itBOLindividualBill(self):
        itBOLDrp = self.driver.find_element(By.XPATH, self.itBOLDrp_XPATH)
        itBOLDrp.click()
        itBOLDrp.send_keys("i")
        time.sleep(1)
        itBOLDrp.send_keys(Keys.ENTER)

    # Vessel Inforrmation
    def vesselName(self, vesselsname):
        vesselNameTxt = self.driver.find_element(By.CSS_SELECTOR, self.vesselNameTxt_CSS)
        vesselNameTxt.send_keys(vesselsname)
    def vesselFlightNo(self, vessellsno):
        vesselFlightNoTxt = self.driver.find_element(By.CSS_SELECTOR, self.vesselFlightNoTxt_CSS)
        vesselFlightNoTxt.send_keys(vessellsno)
    def addEditContiner(self):
        addEditContiner_link = self.driver.find_element(By.XPATH, self.addEditContiner_link_XPATH)
        addEditContiner_link.click()
    def containers(self, cont):
        containerTxt = self.driver.find_element(By.XPATH, self.containerTxt_XPATH)
        containerTxt.send_keys(cont)
        time.sleep(1)
    def AddNewContainer(self):
        AddNewContainerButton = self.driver.find_element(By.XPATH, self.AddNewContainerButton_XPATH)
        AddNewContainerButton.click()
        time.sleep(1)
    def saveContainer(self):
        saveContainerButton = self.driver.find_element(By.XPATH, self.saveContainerButton_XPATH)
        saveContainerButton.click()

    # Trading Partners 1
    def manufarture(self,manufacture):
        manufacturerTxt = self.driver.find_element(By.NAME, self.manufacturerTxt_NAME)
        manufacturerTxt.click()
        manufacturerTxt.send_keys(manufacture)
        time.sleep(2)
        manufacturerTxt.send_keys(Keys.ENTER)
        time.sleep(1)
    def seller(self, seller):
        sellerTxt = self.driver.find_element(By.NAME, self.sellerTxt_NAME)
        sellerTxt.click()
        sellerTxt.send_keys(seller)
        time.sleep(2)
        sellerTxt.send_keys(Keys.ENTER)
        time.sleep(1)
    def consignee(self, consignee):
        consigneeTxt = self.driver.find_element(By.XPATH, self.consigneeTxt_XPATH)
        consigneeTxt.click()
        consigneeTxt.send_keys(consignee)
        time.sleep(2)
        consigneeTxt.send_keys(Keys.ENTER)
        time.sleep(1)
    def buyer(self, buyer):
        buyerTxt = self.driver.find_element(By.XPATH, self.buyerTxt_XPATH)
        buyerTxt.click()
        buyerTxt.send_keys(buyer)
        time.sleep(2)
        buyerTxt.send_keys(Keys.ENTER)
        time.sleep(1)

    # Trading Partners 2
    def currency(self,currencyData):
        selectCurrency = self.driver.find_element(By.XPATH, self.selectCurrencyTxt_XPATH)
        selectCurrency.click()
        selectCurrency.send_keys(Keys.CONTROL, 'a')
        selectCurrency.send_keys(Keys.DELETE)
        time.sleep(1)
        selectCurrency.send_keys(currencyData)
        time.sleep(2)
        selectCurrency.send_keys(Keys.ENTER)
        self.driver.find_element(By.XPATH, self.selectCurrencyOutClick_XPATH).click()

    def countryOfOrigin1(self,countryOfOrigindata1):
        countryOfOriginTxt1 = self.driver.find_element(By.XPATH, self.countryOfOriginTxt1_XPATH)
        countryOfOriginTxt1.click()
        countryOfOriginTxt1.send_keys(countryOfOrigindata1)
        time.sleep(2)
        countryOfOriginTxt1.send_keys(Keys.ENTER)
    def release_port(self, release_portdata):
        release_portTxt = self.driver.find_element(By.NAME, self.release_portTxt_Name)
        release_portTxt.click()
        release_portTxt.send_keys(release_portdata)
        time.sleep(2)
        release_portTxt.send_keys(Keys.ENTER)
    def selectCurrency(self, currencyData):
        selectCurrencyTxt = self.driver.find_element(By.XPATH, self.selectCurrencyTxt_XPATH)
        selectCurrencyTxt.click()
        selectCurrencyTxt.send_keys(Keys.CONTROL, 'a')
        selectCurrencyTxt.send_keys(Keys.DELETE)
        time.sleep(1)
        selectCurrencyTxt.send_keys(currencyData)
        time.sleep(2)
        selectCurrencyTxt.send_keys(Keys.ENTER)
        selectCurrencyOutclick = self.driver.find_element(By.XPATH, self.selectCurrencyOutclick_XPATH)
        selectCurrencyOutclick.click()
    def countryOfExport1(self, countryOfExportdata1):
        countryOfExportTxt1 = self.driver.find_element(By.XPATH, self.countryOfExportTxt1_XPATH)
        countryOfExportTxt1.click()
        countryOfExportTxt1.send_keys(countryOfExportdata1)
        time.sleep(2)
        countryOfExportTxt1.send_keys(Keys.ENTER)
    def ladingport(self, ladingportdata):
        ladingportTxt = self.driver.find_element(By.XPATH, self.ladingportTxt_XPATH)
        ladingportTxt.click()
        ladingportTxt.send_keys(ladingportdata)
        time.sleep(2)
        ladingportTxt.send_keys(Keys.ENTER)
    def weight(self, grossWeightdata):
        weightTxt = self.driver.find_element(By.ID, self.weightTxt_ID)
        weightTxt.clear()
        weightTxt.send_keys(grossWeightdata)
    def charges(self, chargedata):
        chargesTxt = self.driver.find_element(By.NAME, self.chargesTxt_NAME)
        chargesTxt.clear()
        chargesTxt.send_keys(chargedata)
    def unladingport(self, unladingportdata):
        unladingportTxt = self.driver.find_element(By.XPATH, self.unladingportTxt_XPATH)
        unladingportTxt.click()
        unladingportTxt.send_keys(unladingportdata)
        time.sleep(2)
        unladingportTxt.send_keys(Keys.ENTER)
    def manifestDescription(self, manifestDescriptiondata):
        manifestDescriptionTxt = self.driver.find_element(By.NAME, self.manifestDescriptionTxt_NAME)
        manifestDescriptionTxt.send_keys(manifestDescriptiondata)
    def arrivaldate(self, manifestDescriptiondata):
        arrivaldateBox = self.driver.find_element(By.XPATH, self.arrivaldateBox_XPATH)
        arrivaldateBox.send_keys(manifestDescriptiondata)
    def exportdate(self, manifestDescriptiondata):
        exportdateBox = self.driver.find_element(By.XPATH, self.exportdateBox_XPATH)
        exportdateBox.send_keys(manifestDescriptiondata)

    # Line Items
    def countryOfOrigin2(self,valcorgn):
        countryOfOriginTxt2 = self.driver.find_element(By.XPATH, self.countryOfOriginTxt2_XPATH)
        countryOfOriginTxt2.click()
        countryOfOriginTxt2.send_keys(valcorgn)
        time.sleep(2)
        countryOfOriginTxt2.send_keys(Keys.ENTER)
        time.sleep(1)
    def countryOfExport2(self,valcexprt):
        countryOfExportTxt2 = self.driver.find_element(By.XPATH, self.countryOfExportTxt2_XPATH)
        countryOfExportTxt2.click()
        countryOfExportTxt2.send_keys(valcexprt)
        time.sleep(2)
        countryOfExportTxt2.send_keys(Keys.ENTER)
        time.sleep(1)
    def tariffno(self,valhts):
        tariffnoTxt = self.driver.find_element(By.XPATH, self.tariffnoTxt_XPATH)
        tariffnoTxt.click()
        tariffnoTxt.send_keys(valhts)
        time.sleep(2)
        tariffnoTxt.send_keys(Keys.ENTER)
        time.sleep(1)
    def part(self,partdata):
        scaccodeTxt = self.mywait.until(EC.element_to_be_clickable((By.XPATH, self.partTxt_XPATH)))
        scaccodeTxt.click()
        scaccodeTxt.send_keys(partdata)
        time.sleep(2)
        scaccodeTxt.send_keys(Keys.ENTER)
        time.sleep(1)
    def invoiceTotal(self, invoiceTotaldata):
        invoiceTotalTxt = self.driver.find_element(By.CSS_SELECTOR, self.invoiceTotalTxt_CSS)
        invoiceTotalTxt.send_keys(invoiceTotaldata)

    def chinaHTSToAdd(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
        time.sleep(1)
    def chinaHTSNotToAdd(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
        time.sleep(1)
    def cottonHTSToExempt(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Yes']").click()
        time.sleep(1)
    def cottonHTSNotToExempt(self):
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Cancel']").click()
        time.sleep(1)
    def lineValue(self,lnvl):
        NumberOfLineItem = self.driver.find_element(By.XPATH, self.NumberOfLineItem_XPATH).text
        linevalueTxt = self.driver.find_element(By.XPATH,"(//span[text()='Line Value (USD):']//parent::div//following-sibling::div/input[@name='linevalue'])[" + str(NumberOfLineItem) + "]")
        linevalueTxt.send_keys(Keys.CONTROL + 'a')
        linevalueTxt.send_keys(Keys.BACKSPACE)
        linevalueTxt.send_keys(lnvl)
    def foreinValue(self, foreinlinevalueData):
        foreignLineValueTxt = self.driver.find_element(By.XPATH, self.foreignLineValueTxt_XPATH)
        foreignLineValueTxt.send_keys(foreinlinevalueData)
        foreignLineValueOutClick = self.driver.find_element(By.XPATH, self.foreignLineValueOutClick_XPATH)
        foreignLineValueOutClick.click()
        time.sleep(2)


    def addCvd(self, addcaseNumber, cvdcaseNumber):#, cvdcaseNumber
        NumberOfLineItem = self.driver.find_element(By.XPATH, self.NumberOfLineItem_XPATH).text
        showHideAddCVDLink = self.driver.find_element(By.XPATH, "(//a[normalize-space()='Show/Hide ADD/CVD'])[" + str(NumberOfLineItem) + "]")
        showHideAddCVDLink.click()
        addTxt = self.driver.find_element(By.XPATH, "(//input[@id='addCaseNumber'])[" + str(NumberOfLineItem) + "]")
        addTxt.send_keys(addcaseNumber)
        addOutclick = self.driver.find_element(By.XPATH,"(//span[normalize-space()='ADD Case Number:'])[" + str(NumberOfLineItem) + "]")
        addOutclick.click()
        time.sleep(1)
        cvdInput = self.driver.find_element(By.XPATH, "(//input[@id='cvdCaseNumber'])[" + str(NumberOfLineItem) + "]")
        cvdInput.send_keys(cvdcaseNumber)
        cvdOutclick = self.driver.find_element(By.XPATH,"(//span[normalize-space()='CVD Case Number:'])[" + str(NumberOfLineItem) + "]")
        cvdOutclick.click()
        time.sleep(1)

    def maximizeQtySection(self):
        textOfHTS = self.driver.find_element(By.XPATH, self.textOfHTSWhenCollapsed_XPATH).text
        maximizeQtySectionButton = self.mywait.until(EC.element_to_be_clickable((By.XPATH, "//button//span[normalize-space()=" + textOfHTS + "]")))
        maximizeQtySectionButton.click()

    def minimizeQtySection(self):
        textOfHTS = self.driver.find_element(By.XPATH, self.textOfHTSWhenExpanded_XPATH).text
        minimizeQtySectionButton = self.mywait.until(EC.element_to_be_clickable((By.XPATH, "//button//span[normalize-space()=" + textOfHTS + "]")))
        minimizeQtySectionButton.click()
    def maximizeQtySectionForChina(self):
        textOfHTSForChina = self.driver.find_element(By.XPATH, self.textOfHTSWhenCollapsed_XPATH_ForChina).text
        maximizeQtySectionForChinaButton = self.mywait.until(EC.element_to_be_clickable((By.XPATH, "//button//span[normalize-space()=" + textOfHTSForChina + "]")))
        maximizeQtySectionForChinaButton.click()

    def minimizeQtySectionForChina(self):
        textOfHTSForChina = self.driver.find_element(By.XPATH, self.textOfHTSWhenExpanded_XPATH_ForChina).text
        minimizeQtySectionForChinaButton = self.mywait.until(EC.element_to_be_clickable((By.XPATH, "//button//span[normalize-space()=" + textOfHTSForChina + "]")))
        minimizeQtySectionForChinaButton.click()
    def addCottonValues(self,htsqty1,htsqty2):
        CottonQty1 = self.driver.find_element(By.XPATH, "(//input[@name='linevalue'])[2]")
        CottonQty1.send_keys(htsqty1)
        CottonQty2 = self.driver.find_element(By.XPATH, "(//input[@name='linevalue'])[3]")
        CottonQty2.send_keys(htsqty2)

    def addCottonValuesForChina(self,htsqty1,htsqty2):
        CottonQty1 = self.driver.find_element(By.XPATH, "(//input[@name='linevalue'])[8]")
        CottonQty1.send_keys(htsqty1)
        CottonQty2 = self.driver.find_element(By.XPATH, "(//input[@name='linevalue'])[9]")
        CottonQty2.send_keys(htsqty2)

    def removelineitem(self,lineitmscount):
        removeLineItem = self.mywait.until(EC.element_to_be_clickable(
            (By.XPATH, "(//button[contains(text(),'Remove Line')])[" + str(lineitmscount + 1) + "]")))
        removeLineItem.click()
        print("Total Line Items are", lineitmscount)

    # Save Form
    def saveform(self):
        saveButton = self.mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Save')]")))
        saveButton.click()
        time.sleep(2)
    def formSavedConfirmationMsg(self):
        formSavedConfirmationMsgButton = self.driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
        formSavedConfirmationMsgButton.click()
        time.sleep(2)

    def submitform(self):
        submitButton = self.mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Submit')]")))
        submitButton.click()
        time.sleep(2)

    def validationFormsubmitButton(self):
        validationFormsubmitButton = self.mywait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='button'][normalize-space()='Submit']")))
        validationFormsubmitButton.click()
        time.sleep(2)

    def validationFormsubmitConfirmationMsg(self):
        validationFormsubmitConfirmationMsgButton = self.driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
        validationFormsubmitConfirmationMsgButton.click()
        time.sleep(2)

    def MandatoryFieldMsg(self):
        mandatoryFieldMsgButton = self.driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
        mandatoryFieldMsgButton.click()
        time.sleep(2)



    def close(self):
        self.driver.close()
