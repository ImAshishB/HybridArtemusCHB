# In this Script, script will be record errors and will be continuing for next script.
import logging
import datetime
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
    ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException, TimeoutException
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilites.utils import utills
import time
file = "D:\Artmus Spec\Automation_Artemus\TestML.xlsx"
rows = utills.getRowCount(file, "Sheet1")
coloumns = utills.getColumnCount(file, "Sheet1")
print("Login Done")


for r in range(33, 34):
    i = 0
    i = i - 1
    billCounts = utills.readData(file, "Sheet1", r, 2)
    lineitmscount = utills.readData(file, "Sheet1", r, 3)
    testCasesNumber = utills.readData(file, "Sheet1", r, 10)
    # intlineitmscount = int(lineitmscount)

    # #Login
    usern = utills.readData(file, "Sheet1", r, 5)
    pasw = utills.readData(file, "Sheet1", r, 6)
    #
    # #Form
    entfilltype = utills.readData(file, "Sheet1", r, 7)
    actionC = utills.readData(file, "Sheet1", r, 8)
    trnpmode = utills.readData(file, "Sheet1", r, 9)
    invoicenoEx = utills.readData(file, "Sheet1", r, 10)

    scacData = utills.readData(file, "Sheet1", r, 11).split(",")
    uomData = utills.readData(file, "Sheet1", r, 13).split(",")
    qtyyData = utills.readData(file, "Sheet1", r, 14).split(",")

    scacData2 = "MFUS"
    scacData3 = "tk"
    uomData2 = "PKG"
    qtyyData2 = "50"

    vesselsname = utills.readData(file, "Sheet1", r, 15)
    vessellsno = utills.readData(file, "Sheet1", r, 16)
    containerscount = utills.readData(file, "Sheet1", r, 4)
    containerlist = utills.readData(file, "Sheet1", r, 17).split(",")

    manufacturerdata = utills.readData(file, "Sheet1", r, 18)
    sellerdata = utills.readData(file, "Sheet1", r, 19)
    consigneedata = utills.readData(file, "Sheet1", r, 20)
    buyerdata = utills.readData(file, "Sheet1", r, 21)

    countryOfOrigindata1 = utills.readData(file, "Sheet1", r, 22)
    release_portdata = utills.readData(file, "Sheet1", r, 23)
    countryOfExportdata1 = utills.readData(file, "Sheet1", r, 24)
    ladingportdata = utills.readData(file, "Sheet1", r, 25)
    grossWeightdata = utills.readData(file, "Sheet1", r, 26)
    chargedata = utills.readData(file, "Sheet1", r, 27)
    unladingportdata = utills.readData(file, "Sheet1", r, 28)
    manifestDescriptiondata = utills.readData(file, "Sheet1", r, 29)
    arrivaldatedata = utills.readData(file, "Sheet1", r, 30)
    exportdatedata = utills.readData(file, "Sheet1", r, 31)
    currencyData = utills.readData(file, "Sheet1", r, 112)

    invoiceTotaldata = utills.readData(file, "Sheet1", r, 32)
    tariffnodata = utills.readData(file, "Sheet1", r, 33).split(",")
    htsqty1 = utills.readData(file, "Sheet1", r, 34)
    htsqty2 = utills.readData(file, "Sheet1", r, 35)
    addcaseNumberData = utills.readData(file, "Sheet1", r, 111)
    cvdcaseNumberData = utills.readData(file, "Sheet1", r, 110)
    linevaluedata = utills.readData(file, "Sheet1", r, 36).split(",")
    countryOfOrigindata2 = utills.readData(file, "Sheet1", r, 37).split(",")
    countryOfExportdata2 = utills.readData(file, "Sheet1", r, 38).split(",")

    for valhts, valcorgn, valcexprt, lnvl in zip(tariffnodata, countryOfOrigindata2,
                                                 countryOfExportdata2, linevaluedata):

        print("hits numbewr is ",tariffnodata)
        print("entyfilltypi is ", entfilltype)
        ff = type(entfilltype)
        print("Type of entyfilltypi is ", ff)
        print("------------")
        if entfilltype == 23:
            print("23.....")
        elif entfilltype != 23:
            print("24.....")

