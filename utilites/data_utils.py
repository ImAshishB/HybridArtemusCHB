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

import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from base.base_driver import BaseDriver
from utilites.utils import utills


import inspect
import logging
import openpyxl
import string
import random
import os
from colorlog import ColoredFormatter
from openpyxl.styles import PatternFill

# class Data():
#     file = "D:\\LoginTestData22.xlsx"
#     log = utills.custom_logger()  # we can change logging level
#     rows = utills.getRowCount(file, "Sheet1")
#     coloumns = utills.getColumnCount(file, "Sheet1")
#     list_status = []  # Empty List Veriable

def excelData():
    usernameData = utills.readData(file, 'Sheet1', r, 1)
    passwordData = utills.readData(file, 'Sheet1', r, 2)
