# # import pytest
# # from selenium import webdriver
# # from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
# #     ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.support.ui import WebDriverWait
# # @pytest.fixture(autouse=True)#scope="class"
# # def setup(request):
# #     # logging.basicConfig(filename="Art_7501Log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
# #     # logging.info('------------------------------------------------------------New Log Started From Here-----------------------------------------------------------------------')
# #     serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
# #     options = webdriver.ChromeOptions()
# #     options.add_experimental_option("detach", True)
# #     driver = webdriver.Chrome(options=options, service=serv_obj)
# #     mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
# #                                                                              ElementNotVisibleException,
# #                                                                              ElementNotSelectableException,
# #                                                                              ElementClickInterceptedException,
# #                                                                              ElementNotInteractableException,
# #                                                                              Exception])
# #
# #     # URL
# #     driver.get("http://52.54.244.138:8080/ArtemusChb/")
# #
# #     # Maximize page
# #     driver.maximize_window()
# #     request.cls.driver = driver
# #     request.cls.mywait = mywait
# #     #yield
# #     #driver.close()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# import pytest
# from selenium import webdriver
# from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
#     ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.firefox.options import Options
# @pytest.fixture(autouse=True)#scope="class"
# # @pytest.fixture()
# def setup(request, browser):#browser #request
#     # If I want to run in Chrome
#     if browser=='chrome':
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option("detach", True)
#         serv_obj = Service("C:/Drivers/chromedriver-win64/chromedriver.exe")
#         driver = webdriver.Chrome(options=options, service=serv_obj)
#         print("Launching chrome browser.........")
#         mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
#                                                                                  ElementNotVisibleException,
#                                                                                  ElementNotSelectableException,
#                                                                                  ElementClickInterceptedException,
#                                                                                  ElementNotInteractableException,
#                                                                                  Exception])
#     # If I want to run in Firefox
#
#     elif browser=='firefox':
#         driver = webdriver.Firefox()
#         print("Launching firefox browser.........")
#         mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
#                                                                                  ElementNotVisibleException,
#                                                                                  ElementNotSelectableException,
#                                                                                  ElementClickInterceptedException,
#                                                                                  ElementNotInteractableException,
#                                                                                  Exception])
#     # If I don't want to run in above then I am setting the deafult browser as Chrome
#     else:
#         # Internet Explorer
#         # driver = webdriver.Ie()
#         # Chrome
#         options = webdriver.ChromeOptions()
#         options.add_experimental_option("detach", True)
#         serv_obj = Service("C:/Drivers/chromedriver-win64/chromedriver.exe")
#         driver = webdriver.Chrome(options=options, service=serv_obj)
#
#         mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
#                                                                                  ElementNotVisibleException,
#                                                                                  ElementNotSelectableException,
#                                                                                  ElementClickInterceptedException,
#                                                                                  ElementNotInteractableException,
#                                                                                  Exception])
#
#     # return driver
#     # URL
#     driver.get("http://52.54.244.138:8080/ArtemusChb/")
#
#     # Maximize page
#     driver.maximize_window()
#     request.cls.driver = driver
#     request.cls.mywait = mywait
#     yield
#     driver.close()
#
# def pytest_addoption(parser):    # This will get the value from CLI /hooks
#     parser.addoption("--browser")
#
# @pytest.fixture(scope="class", autouse=True)
# def browser(request):  # This will return the Browser value to setup method
#     return request.config.getoption("--browser")
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     # serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
#     # options = webdriver.ChromeOptions()
#     # options.add_experimental_option("detach", True)
#     # driver = webdriver.Chrome(options=options, service=serv_obj)
#     # mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
#     #                                                                          ElementNotVisibleException,
#     #                                                                          ElementNotSelectableException,
#     #                                                                          ElementClickInterceptedException,
#     #                                                                          ElementNotInteractableException,
#     #                                                                          Exception])
#     #
#     # # URL
#     # driver.get("http://52.54.244.138:8080/ArtemusChb/")
#     #
#     # # Maximize page
#     # driver.maximize_window()
#     # request.cls.driver = driver
#     # request.cls.mywait = mywait
#     # #yield
#     # #driver.close()
















































# import pytest
# from selenium import webdriver
# from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
#     ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.support.ui import WebDriverWait
# @pytest.fixture(autouse=True)#scope="class"
# def setup(request):
#     # logging.basicConfig(filename="Art_7501Log", level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
#     # logging.info('------------------------------------------------------------New Log Started From Here-----------------------------------------------------------------------')
#     serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
#     options = webdriver.ChromeOptions()
#     options.add_experimental_option("detach", True)
#     driver = webdriver.Chrome(options=options, service=serv_obj)
#     mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
#                                                                              ElementNotVisibleException,
#                                                                              ElementNotSelectableException,
#                                                                              ElementClickInterceptedException,
#                                                                              ElementNotInteractableException,
#                                                                              Exception])
#
#     # URL
#     driver.get("http://52.54.244.138:8080/ArtemusChb/")
#
#     # Maximize page
#     driver.maximize_window()
#     request.cls.driver = driver
#     request.cls.mywait = mywait
#     #yield
#     #driver.close()




















import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException, \
    ElementClickInterceptedException, ElementNotInteractableException, NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.options import Options
@pytest.fixture(autouse=True)#scope="class"
def setup(request, browser):#browser #request
    # If I want to run in Chrome
    if browser=='chrome':
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        serv_obj = Service("C:/Drivers/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=serv_obj)
        print("Launching chrome browser.........")
        mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                 ElementNotVisibleException,
                                                                                 ElementNotSelectableException,
                                                                                 ElementClickInterceptedException,
                                                                                 ElementNotInteractableException,
                                                                                 Exception])
    # If I want to run in Firefox

    elif browser == 'firefox':
        # Firefox setup
        firefox_options = Options()
        firefox_options.log.level = "trace"  # Set log level to trace
        driver = webdriver.Firefox(options=firefox_options)
        print("Launching firefox browser.........")
        mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                 ElementNotVisibleException,
                                                                                 ElementNotSelectableException,
                                                                                 ElementClickInterceptedException,
                                                                                 ElementNotInteractableException,
                                                                                 Exception])
    # If I don't want to run in above then I am setting the deafult browser as Chrome
    else:
        # Internet Explorer
        # driver = webdriver.Ie()
        # Chrome
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        serv_obj = Service("C:/Drivers/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(options=options, service=serv_obj)

        mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
                                                                                 ElementNotVisibleException,
                                                                                 ElementNotSelectableException,
                                                                                 ElementClickInterceptedException,
                                                                                 ElementNotInteractableException,
                                                                                 Exception])

    # return drivers
    # URL
    driver.get("http://52.54.244.138:8080/ArtemusChb/")

    # Maximize page
    driver.maximize_window()


    request.cls.driver = driver
    request.cls.mywait = mywait
    # yield # will  execute after every method
    # driver.close()

def pytest_addoption(parser):    # This will get the value from CLI /hooks
    parser.addoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")




######### Pytest HTML Report #########

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'Artemus CHB'
#     config._metadata['Module Name'] = 'KuchBhi'
#     config._metadata['Tester'] = 'Ashish'


# def pytest_configure(config):
#     config.option.html_metadata['Project Name'] = 'Artemus CHB'
#     config.option.html_metadata['Module Name'] = 'KuchBhi'
#     config.option.html_metadata['Tester'] = 'Ashish'
#
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugins", None)


















    # serv_obj = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
    # options = webdriver.ChromeOptions()
    # options.add_experimental_option("detach", True)
    # driver = webdriver.Chrome(options=options, service=serv_obj)
    # mywait = WebDriverWait(driver, 10, poll_frequency=2, ignored_exceptions=[NoSuchElementException,
    #                                                                          ElementNotVisibleException,
    #                                                                          ElementNotSelectableException,
    #                                                                          ElementClickInterceptedException,
    #                                                                          ElementNotInteractableException,
    #                                                                          Exception])
    #
    # # URL
    # driver.get("http://52.54.244.138:8080/ArtemusChb/")
    #
    # # Maximize page
    # driver.maximize_window()
    # request.cls.driver = driver
    # request.cls.mywait = mywait
    # #yield
    # #driver.close()