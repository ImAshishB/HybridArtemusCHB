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

    #PGA Form
    #PG01
    commercialDescription_XPATH = "//label[normalize-space()='Commercial Description:']//parent::div//following-sibling::div//input[@id='commercialDescription']"
    desclaimerDrp_XPATH = "//label[text()='Disclaimer:']//parent::div//following-sibling::div//select[@name='disclaimer']"
    pgaLineValue_XPATH = "//label[text()='PGA Line Value:']//parent::div//following-sibling::div//input[@name='pgaLineValue']"

    #PG21
    individualQualifier_XPATH = "//span[normalize-space()='Individual Qualifier:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic']"
    mailOrFax_XPATH = "//span[normalize-space()='Email or Fax:']//parent::div//following-sibling::div/input[@name='email']"
    individualName_XPATH = "//span[text()='Individual Name:']//parent::div//following-sibling::div/input[@name='individualName']"
    telephoneNo_XPATH = "//span[text()='Telephone No:']//parent::div//following-sibling::div/input[@name='telephoneNo']"

    #PG22
    entityRoleCode_XPATH = "//span[text()='Entity Role Code:']//parent::div//following-sibling::div/input[@type='text' and @id='typeahead-basic']"
    declarationCode_XPATH = "//span[text()='Declaration Code:']//parent::div//following-sibling::div/input[@name='declarationCode']"
    declarationCertification_XPATH = "//span[text()='Declaration Certification:']//parent::div//following-sibling::div/select[@name='declarationCertification']"
    dateSignature_XPATH = "//span[text()='Date Signature:']//parent::div//following-sibling::div//input[@name='dateSignature']"
    dateSignatureOutClick_XPATH = "//span[normalize-space()='Date Signature:']"

    # Save Buttons
    saveAndClosePGAButton_XPATH = "//button[normalize-space()='Save & Close']"
    alertDataIsValidButton_XPATH = "//button[@type='button'][normalize-space()='Save & Close']"
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

    # PG01
    def commercialDescription(self, descriptionData):
        commercialDescriptionTxt = self.driver.find_element(By.XPATH, self.commercialDescription_XPATH)
        commercialDescriptionTxt.send_keys(descriptionData)


    def desclaimer(self,disclaimerdata):
        desclaimerDrp = self.driver.find_element(By.XPATH,self.desclaimerDrp_XPATH)
        desclaimerDrp.click()
        desclaimerDrp.send_keys(disclaimerdata)
        desclaimerDrp.send_keys(Keys.ENTER)

    def pgaLineValue(self, pgaLineValueData):
        pgaLineValueTxt = self.driver.find_element(By.XPATH, self.pgaLineValue_XPATH)
        pgaLineValueTxt.send_keys(pgaLineValueData)

    # PG21
    def individualQualifier(self, individualQualifierdata):
        individualQualifierTxt = self.driver.find_element(By.XPATH, self.individualQualifier_XPATH)
        individualQualifierTxt.send_keys(individualQualifierdata)
        time.sleep(2)
        individualQualifierTxt.send_keys(Keys.ENTER)

    def mailOrFax(self, mailOrFaxdata):
        mailOrFaxTxt = self.driver.find_element(By.XPATH, self.mailOrFax_XPATH)
        mailOrFaxTxt.send_keys(mailOrFaxdata)

    def individualName(self, individualNameData):
        individualNameTxt = self.driver.find_element(By.XPATH,self.individualName_XPATH)
        individualNameTxt.send_keys(individualNameData)

    def telephoneNo(self, telephoneNoData):
        telephoneNoTxt = self.driver.find_element(By.XPATH, self.telephoneNo_XPATH)
        telephoneNoTxt.send_keys(telephoneNoData)

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

    def saveAndClosePGA(self):
        saveAndCloseButton = self.driver.find_element(By.XPATH, self.saveAndClosePGAButton_XPATH)
        saveAndCloseButton.click()
        time.sleep(2)

    def alertDataIsValid(self):
        alertDataIsValidButton = self.driver.find_element(By.XPATH, self.alertDataIsValidButton_XPATH)
        alertDataIsValidButton.click()
    def pgaFormClosedalert(self):
        pgaFormClosedalertOkButton= self.driver.find_element(By.XPATH, self.pgaFormClosedalertOkButton_XPATH)
        pgaFormClosedalertOkButton.click()






