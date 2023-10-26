import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver
from utilites.utils import utills

class getAtributesOfText(BaseDriver):
    def __init__(self, driver, mywait):
        super().__init__(driver)
        self.driver = driver
        self.mywait = mywait

    # Locators

    shipment_LINK_TEXT = "Shipments"
    form7501_LINK_TEXT = "Form 7501"

    # Upper Part locators
    entryfillingtypecodeDrpDwn_ID = "entryFilingTypeCode"
    actionCodeTxt_ID = "actionCode"
    modeOfTransport_ID = "modeOfTransport"
    invoicenumberTxt_CSS = "input#invoiceNumber"
    ivcnumberoutclick_XPATH = "//span[normalize-space()='Invoice Number:']"

    # Bill of lading locators
    # scaccodeTxt_XPATH = "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='scac']"
    # billTxt_XPATH = "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='billOfLading']"
    # outclick_XPATH = "// span[normalize-space()='Split Shipment:']"
    # uomTxt_XPATH = "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='uom']"
    # quantityTxt_XPATH = "//div[@class='ng-untouched ng-pristine ng-invalid']//fieldset//input[@name='quantity']"
    # addBillButton_XPATH = "//button[normalize-space()='Add a Bill']"

    scaccodeTxt_XPATH = "//span[text()='SCAC:']//parent::div//following-sibling::div/input[@id='typeahead-basic']"
    billTxt_XPATH = "//input[@name='billOfLading']"
    outclick_XPATH = "//span[normalize-space()='Split Shipment:']"
    uomTxt_XPATH = "//span[text()='UOM:']//parent::div//following-sibling::div/input[@id='typeahead-basic']"
    quantityTxt_XPATH = "//input[@id='quantity']"
    addBillButton_XPATH = "//button[normalize-space()='Add a Bill']"

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

    # Line Items Locators
    invoiceTotalTxt_CSS = "input#invoiceTotal"
    tariffnoTxt_XPATH = "//span[text()='Tariff #1:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @class='form-control ng-untouched ng-pristine ng-valid']"
    countryOfOriginTxt2_XPATH = "//span[text()='Country of Origin:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @required]"
    countryOfExportTxt2_XPATH = "//span[text()='Country of Export:']//parent::div//following-sibling::div/input[@id='typeahead-basic' and @required]"
    linevaluesaddTxt_XPATH = "//span[text()='Line Value (USD):']//parent::div//following-sibling::div/input[@name='linevalue']"

    # Entry Summary Form
    # Upper Part
    def get_invoicenumber_text(self):
        invoicenumber_element = self.driver.find_element(By.CSS_SELECTOR, self.invoicenumberTxt_CSS)
        return invoicenumber_element.get_attribute("value")
    # Bill of Lading
    def get_scaccode_text(self):
        scaccode_element = self.driver.find_element(By.XPATH, self.scaccodeTxt_XPATH)
        return scaccode_element.get_attribute("value")
    def get_uom_text(self):
        uom_element = self.driver.find_element(By.XPATH, self.uomTxt_XPATH)
        return uom_element.get_attribute("value")
    def get_quantity_text(self):
        quantity_element = self.driver.find_element(By.XPATH, self.quantityTxt_XPATH)
        return quantity_element.get_attribute("value")

    # Vessel Inforrmation
    def get_vesselName_text(self):
        vesselName_element = self.driver.find_element(By.CSS_SELECTOR, self.vesselNameTxt_CSS)
        return vesselName_element.get_attribute("value")
    def get_vesselFlightNo_text(self):
        vesselFlightNo_element = self.driver.find_element(By.CSS_SELECTOR, self.vesselFlightNoTxt_CSS)
        return vesselFlightNo_element.get_attribute("value")

    # Trading Partners 1
    def get_manufacturer_text(self):
        manufacturer_element = self.driver.find_element(By.NAME, self.manufacturerTxt_NAME) # Replace with actual element locator
        return manufacturer_element.get_attribute("value")
    def get_seller_text(self):
        seller_element = self.driver.find_element(By.NAME, self.sellerTxt_NAME)
        return seller_element.get_attribute("value")
    def get_consignee_text(self):
        consignee_element = self.driver.find_element(By.XPATH, self.consigneeTxt_XPATH)
        return consignee_element.get_attribute("value")
    def get_buyer_text(self):
        buyer_element = self.driver.find_element(By.XPATH, self.buyerTxt_XPATH)
        return buyer_element.get_attribute("value")

    # Trading Partners 2
    def get_countryOfOrigin1_text(self):
        countryOfOrigin1_element = self.driver.find_element(By.XPATH, self.countryOfOriginTxt1_XPATH)
        return countryOfOrigin1_element.get_attribute("value")
    def get_release_port_text(self):
        release_port_element = self.driver.find_element(By.NAME, self.release_portTxt_Name)
        return release_port_element.get_attribute("value")
    def get_countryOfExport1_text(self):
        countryOfExport1_element = self.driver.find_element(By.XPATH, self.countryOfExportTxt1_XPATH)
        return countryOfExport1_element.get_attribute("value")
    def get_ladingport_text(self):
        ladingport_element = self.driver.find_element(By.XPATH, self.ladingportTxt_XPATH)
        return ladingport_element.get_attribute("value")
    def get_weight_text(self):
        weight_element = self.driver.find_element(By.ID, self.weightTxt_ID)
        return weight_element.get_attribute("value")
    def get_charges_text(self):
        charges_element = self.driver.find_element(By.NAME, self.chargesTxt_NAME)
        return charges_element.get_attribute("value")
    def get_unladingport_text(self):
        unladingport_element = self.driver.find_element(By.XPATH, self.unladingportTxt_XPATH)
        return unladingport_element.get_attribute("value")
    def get_manifestDescription_text(self):
        manifestDescription_element = self.driver.find_element(By.NAME, self.manifestDescriptionTxt_NAME)
        return manifestDescription_element.get_attribute("value")
    def get_arrivaldate_text(self):
        arrivaldate_element = self.driver.find_element(By.XPATH, self.arrivaldateBox_XPATH)
        return arrivaldate_element.get_attribute("value")
    def get_exportdate_text(self):
        exportdate_element = self.driver.find_element(By.XPATH, self.exportdateBox_XPATH)
        return exportdate_element.get_attribute("value")

    def get_currency_text(self):
        currency_element = self.driver.find_element(By.XPATH, self.selectCurrencyTxt_XPATH)
        return currency_element.get_attribute("value")

    # # Line Items
    def get_countryOfOrigin2_text(self):
        countryOfOrigin2_element = self.driver.find_element(By.XPATH, self.countryOfOriginTxt2_XPATH)
        return countryOfOrigin2_element.get_attribute("value")
    def get_countryOfExport2_text(self):
        countryOfExport2_element = self.driver.find_element(By.XPATH, self.countryOfExportTxt2_XPATH)
        return countryOfExport2_element.get_attribute("value")
    def get_tariffno_text(self):
        tariffno_element = self.driver.find_element(By.XPATH, self.tariffnoTxt_XPATH)
        return tariffno_element.get_attribute("value")
    def get_invoiceTotal_text(self):
        invoiceTotal_element = self.driver.find_element(By.CSS_SELECTOR, self.invoiceTotalTxt_CSS)
        return invoiceTotal_element.get_attribute("value")
