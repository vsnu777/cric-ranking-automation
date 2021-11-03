import logging
import os
import shutil
from traceback import print_stack

from selenium.common.exceptions import ElementNotSelectableException, ElementNotVisibleException, \
    NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from Configuration.Base import BaseClass
from Utility.readProperty import ReadConfig
from Utility.logger import customlogger as log


class utilities:
    @staticmethod
    def waitfor(driver,timeout=10, pollfrequency=0.5):
        wait = None
        try:
            wait = WebDriverWait(driver=driver, timeout=timeout, poll_frequency=pollfrequency, ignored_exceptions=[NoSuchElementException,
                                                                                 ElementNotVisibleException,
                                                                                 ElementNotSelectableException,StaleElementReferenceException])
        except:
            log().info("exception occured")
            print_stack()
        return wait

    @staticmethod
    def get_source_folder():
        source_folder = os.getcwd()
        return source_folder

    @staticmethod
    def move_log_file(source_folder, destination_folder):
        source_files = os.listdir(source_folder)
        print(source_files)
        print(destination_folder)
        for file in source_files:
            if file.endswith(".txt"):
                shutil.move(file, destination_folder)



    @staticmethod
    def copy_logs(source_folder):
        logsDirectory = "../reports_logs/"
        relativeFileName = logsDirectory
        currentDirectory = os.path.dirname(__file__)
        #destinationFile = os.path.join(currentDirectory, relativeFileName)
        destinationDirectory = os.path.join(currentDirectory, logsDirectory)

        try:
            if not os.path.exists(destinationDirectory):
                os.makedirs(destinationDirectory)
                utilities.move_log_file(source_folder=source_folder, destination_folder=logsDirectory)
            else:
                utilities.move_log_file(source_folder=source_folder, destination_folder=logsDirectory)
        except:
            log().error("### Exception Occurred while copying the logs")
            print_stack()

    @staticmethod
    def get_testcaseName():
        test_name = os.environ.get('PYTEST_CURRENT_TEST')
        print(test_name)
        return test_name