import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver
from utilites.utils import utills


class Form5106Page(BaseDriver):
    def __init__(self, driver, mywait):
        super().__init__(driver)
        self.driver = driver
        self.mywait = mywait

    # Locators

    # Select Importer
    selectImporterTxt_XPATH = "//input[@id='typeahead-basic']"

    L5106_LINK_TEXT = "5106"
    form5106_XPATH = "//div[normalize-space()='Form 5106']"

    # Form locators
    importerNameTxt_ID = "importerName"
    importerNumberTxt_ID = "importerNumber"
    QualifierDropdown_ID = "nameQualifier"
    alternateImporterNameTxt_ID = "alternateImporterName"
    ImporterTypeDropdown_XPATH = "//select[@id='importerType']"
    IORCheckBx_XPATH = "//input[@id='importerOfRecordUtilized']"
    ConsigneeCheckBx_XPATH = "//input[@id='consigneeUtilized']"
    DrawbackCheckBx_XPATH = "//input[@id='drawbackClaimant']"
    RefundsCheckBx_XPATH = "//input[@id='refundsClaimant']"
    OthersCheckBx_XPATH = "//input[@id='othersClaimant']"
    OthersDescriptionText_XPATH = "//textarea[@id='othersClaimantDescription']"
    Line1Txt_ID = "lineOne"
    Line2Txt_ID = "lineTwo"
    CityTxt_ID = "city"
    StateTxt_ID = "state"
    ZipcodeTxt_ID = "postalCode"
    CountryTxt_XPATH = "(//span[text()='Country Code:']//parent::div//following-sibling::div/input[@id='typeahead-basic'])[1]"
    AddressTypeTxt_XPATH = "addressType"
    CopyMailingAddressTxt_LINK_TEXT = "Copy Mailing Address to Physical Address"
    phoneNumberTxt_ID = "phoneNumber"
    emailAddressTxt_ID = "emailAddress"
    saveButton_XPATH = "(//button[@class='btn btn-outline-info'][normalize-space()='Save'])[1]"

    # Action
    def L5106(self):
        L5106_LINK = self.driver.find_element(By.LINK_TEXT, self.L5106_LINK_TEXT)
        L5106_LINK.click()

    def form5106(self):
        form5106L = self.driver.find_element(By.XPATH, self.form5106_XPATH)
        form5106L.click()


    def importerName(self, importerNm):
        importerNameTxt = self.driver.find_element(By.ID, self.importerNameTxt_ID)
        importerNameTxt.send_keys(importerNm)

    def importerNumber(self, importerNmr):
        importerNumberTxt = self.driver.find_element(By.ID, self.importerNumberTxt_ID)
        importerNumberTxt.send_keys(importerNmr)

    def Qualifier(self, QualifierD):
        QualifierDropdown = self.driver.find_element(By.ID, self.QualifierDropdown_ID)
        QualifierDropdown.click()
        QualifierDropdown.send_keys(QualifierD)
        QualifierDropdown.send_keys(Keys.ENTER)

    def alternateImporterName(self, alternateImporterNm):
        importerNumberTxt = self.driver.find_element(By.ID, self.alternateImporterNameTxt_ID)
        importerNumberTxt.send_keys(alternateImporterNm)

    def ImporterType(self, ImporterTp):
        ImporterTypeDropdown = self.driver.find_element(By.ID, self.ImporterTypeDropdown_XPATH)
        ImporterTypeDropdown.click()
        ImporterTypeDropdown.send_keys(ImporterTp)
        ImporterTypeDropdown.send_keys(Keys.ENTER)

    def IOR(self):
        IORCheck = self.driver.find_element(By.XPATH, self.IORCheckBx_XPATH)
        IORCheck.click()

    def Consignee(self):
        ConsigneeCheck = self.driver.find_element(By.XPATH, self.ConsigneeCheckBx_XPATH)
        ConsigneeCheck.click()

    def Drawback(self):
        DrawbackCheck = self.driver.find_element(By.XPATH, self.DrawbackCheckBx_XPATH)
        DrawbackCheck.click()

    def Refunds(self):
        RefundsCheck = self.driver.find_element(By.XPATH, self.RefundsCheckBx_XPATH)
        RefundsCheck.click()

    def Others(self):
        OthersCheck = self.driver.find_element(By.XPATH, self.OthersCheckBx_XPATH)
        OthersCheck.click()

    def OthersDescription(self, othersDscrptn):
        OthersDescriptionText = self.driver.find_element(By.XPATH, self.OthersDescriptionText_XPATH)
        OthersDescriptionText.send_keys(othersDscrptn)

    def Line1(self, Line1Data):
        Line1Txt = self.driver.find_element(By.ID, self.Line1Txt_ID)
        Line1Txt.send_keys(Line1Data)

    def Line2(self, Line2Data):
        Line2Txt = self.driver.find_element(By.ID, self.Line2Txt_ID)
        Line2Txt.send_keys(Line2Data)

    def City(self, CityData):
        CityTxt = self.driver.find_element(By.ID, self.CityTxt_ID)
        CityTxt.send_keys(CityData)

    def State(self, StateData):
        StateTxt = self.driver.find_element(By.ID, self.StateTxt_ID)
        StateTxt.send_keys(StateData)

    def Zipcode(self, ZipcodeData):
        ZipcodeTxt = self.driver.find_element(By.ID, self.ZipcodeTxt_ID)
        ZipcodeTxt.send_keys(ZipcodeData)

    def AddressType(self, AddressTypeData):
        AddressTypeTxt = self.driver.find_element(By.ID, self.AddressTypeTxt_XPATH)
        AddressTypeTxt.click()
        AddressTypeTxt.send_keys(AddressTypeData)
        AddressTypeTxt.send_keys(Keys.ENTER)

    def Country(self, CountryCodeData):
        Country = self.driver.find_element(By.XPATH, self.CountryTxt_XPATH)
        Country.click()
        Country.send_keys(CountryCodeData)
        time.sleep(2)
        Country.send_keys(Keys.ENTER)

    def CopyMailingAddress(self):
        CopyMailingAddressTxt = self.driver.find_element(By.LINK_TEXT, self.CopyMailingAddressTxt_LINK_TEXT)
        CopyMailingAddressTxt.click()

    def PhoneNumber(self, PhoneData):
        phoneNumberTxt = self.driver.find_element(By.ID, self.phoneNumberTxt_ID)
        phoneNumberTxt.send_keys(PhoneData)

    def EmailAddress(self, EmailData):
        emailAddressTxt = self.driver.find_element(By.ID, self.emailAddressTxt_ID)
        emailAddressTxt.send_keys(EmailData)

    # Save Form
    def SaveButton(self):
        saveButton = self.driver.find_element(By.XPATH, self.saveButton_XPATH)
        saveButton.click()
        time.sleep(1)

    def ConfirmationOfSave(self):
        msg = self.driver.find_element(By.TAG_NAME, "body").text
        if 'Form Saved Successfully!' in msg:
            formSavedConfirmationMsgButton = self.driver.find_element(By.XPATH, "//button[normalize-space()='OK']")
            formSavedConfirmationMsgButton.click()
            time.sleep(1)
            print("Form Saved Successfully")
        else:
            print("Form not Saved")

    def AllButton(self):
        All = self.mywait.until(EC.element_to_be_clickable((By.LINK_TEXT, "All")))
        All.click()
        time.sleep(1)



