import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope="module")
def driver():
    # Setup the WebDriver (Chrome in this case)
    driver = webdriver.Chrome()
    driver.get("https://learn.artemusgroupusa.com/ArtemusLearningDev/#/home")
    yield driver
    driver.quit()

# def test_registration(driver):
#     driver.get("https://learn.artemusgroupusa.com/ArtemusLearningDev/#/home")
#     driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
#     driver.find_element(By.NAME, "username").send_keys("ashish.bisen@giantleapsystems.com")
#     driver.find_element(By.NAME, "password").send_keys("ashish")
#     driver.find_element(By.NAME, "confirm_password").send_keys("password123")
#     driver.find_element(By.NAME, "email").send_keys("testuser@example.com")
#     driver.find_element(By.NAME, "submit").click()
#
#     # Assert that registration was successful
#     assert "Registration successful" in driver.page_source

def test_login(driver):
    driver.get("https://learn.artemusgroupusa.com/ArtemusLearningDev/#/home")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    driver.find_element(By.NAME, "username").send_keys("ashish.bisen@giantleapsystems.com")
    driver.find_element(By.NAME, "password").send_keys("ashish")
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(2)

    # Assert that login was successful
    # assert "Welcome, testuser" in driver.page_source

def test_homepage(driver):
    time.sleep(2)
    driver.get("http://localhost:8000/home")

    # Assert that the homepage contains expected content
    assert "Home" in driver.title
    # assert "Welcome to the homepage!" in driver.page_source

def test_logout(driver):
    driver.get("https://learn.artemusgroupusa.com/ArtemusLearningDev/#/home")
    time.sleep(2)
    driver.find_element(By.XPATH, "//a[normalize-space()='Login']").click()
    driver.find_element(By.NAME, "username").send_keys("ashish.bisen@giantleapsystems.com")
    driver.find_element(By.NAME, "password").send_keys("ashish")
    driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, "//a[@id='navbarDropdownMenuLink']").click()
    driver.find_element(By.XPATH, "// label[normalize - space() = 'Sign Out']").click()
    time.sleep(2)

    # Assert that logout was successful
    # assert "You have been logged out" in driver.page_source
