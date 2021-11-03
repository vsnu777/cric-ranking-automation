import os
import time

import pytest
from selenium import webdriver

from Utility.util import utilities


def pytest_addoption(parser):
    """This will get the value from hook or CLI"""
    parser.addoption(
        "--browser", action="store", default="chrome", help="my option: chrome"
    )

@pytest.fixture(scope="class")
def setup(request):
    """This is the method to select browser"""
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="C:\\Users\\Vishnu\\PycharmProjects\\Crickbuzz\\driver\\chromedriver.exe")
        print("Launching Chrome Driver")

    elif browser == "msedge":
        driver = webdriver.Edge(executable_path="C:\\Users\\Vishnu\\PycharmProjects\\ThinkBridge\\drivers\\edgedriver\\msedgedriver.exe")
        print("Launching Edge Driver")

    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.close()
    print("Execution has been completed")
    # source_folder = utilities.get_source_folder()
    # print("Move logs")
    # utilities.copy_logs(source_folder=source_folder)
    # print("logs moved")


def pytest_configure(config):
    """It is a hook to add environment in HTML report"""

    config._metadata["Project Name"] = "Cricbuzz"
    config._metadata["Developer Name"] = "Vishnu"
    config._metadata["Tester Name"] = "Vishnu"


