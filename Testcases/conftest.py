import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
from Utilities.readProperties import ReadConfig


@pytest.fixture()
def set_up(browser):
    if browser == "chrome":
        chrome_driver_path = ReadConfig.get_chrome_driver_path()
        serv= Service(chrome_driver_path)
        driver = webdriver.Chrome(service=serv)
        driver.maximize_window()
        print("Chrome browser launched")
    else:
        edge_driver_path = ReadConfig.get_edge_driver_path()
        serv= Service(edge_driver_path)
        driver = webdriver.Edge(service=serv)
        driver.maximize_window()
        print("Edge browser launched")
    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


def pytest_configure(config):
    config._metadata['Project Name'] = "ANZ_Finance"
    config._metadata['Module Name'] = "Loan Eligibility"



