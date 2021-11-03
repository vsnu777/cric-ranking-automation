from Utility import logger
from Utility.readProperty import ReadConfig

class nav:
    log = logger.customlogger()

    def __init__(self, driver):
        self.driver = driver

    def launch_App(self):
        application_url = ReadConfig.getApplicationUrl()
        self.driver.get(application_url)
        self.log.info("Launched Cricbuzz Application")
        self.driver.maximize_window()
        self.log.info("Maximized the Application")


