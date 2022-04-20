from selenium.webdriver.support.wait import WebDriverWait
import logging


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 5, poll_frequency=1)
        self.__config_logger()

    def __config_logger(self):
        self.logger = logging.getLogger(type(self).__name__)
        self.logger.addHandler(logging.FileHandler(f"logs/{self.driver.test_name}.log"))
        self.logger.setLevel(level=self.driver.log_level)


