from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.product_page import ProductPage
from pages.registration_page import RegistrationPage


class MainPage(BasePage):
    PRODUCT = (By.XPATH, '//div[@class="image"]//img[@title="MacBook"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")
    MY_ACCOUNT = (By.XPATH, '//ul[@class="list-inline"]//li[2]')
    REGISTER = (By.XPATH, '//ul[@class="dropdown-menu dropdown-menu-right"]//li[1]')
    CURRENCY_BUTTON = (By.XPATH, '//div[@class="pull-left"]//button')
    EURO_BUTTON = (By.XPATH, '//button[@name="EUR"]')
    GBP_BUTTON = (By.XPATH, '//button[@name="GBP"]')
    EURO_CURRENCY = (By.XPATH, '//*[text()="€"]')
    GBP_CURRENCY = (By.XPATH, '//*[text()="£"]')

    def open(self):
        self.driver.get(self.url)
        return self

    def open_first_product(self):
        product = self.wait.until(EC.element_to_be_clickable(self.PRODUCT))
        product.click()
        return ProductPage(self.driver, self.url)

    def get_product_name(self):
        product = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME))
        return product.text

    def open_registration_page(self):
        my_account = self.wait.until(EC.element_to_be_clickable(self.MY_ACCOUNT))
        my_account.click()
        register = self.wait.until(EC.element_to_be_clickable(self.REGISTER))
        register.click()
        return RegistrationPage(self.driver, self.url)

    def change_currency_to_euro(self):
        currency_button = self.wait.until(EC.element_to_be_clickable(self.CURRENCY_BUTTON))
        currency_button.click()
        euro_button = self.wait.until(EC.element_to_be_clickable(self.EURO_BUTTON))
        euro_button.click()
        return self

    def check_euro_currency(self):
        self.wait.until(EC.presence_of_element_located(self.EURO_CURRENCY))

    def change_currency_to_gbp(self):
        currency_button = self.wait.until(EC.element_to_be_clickable(self.CURRENCY_BUTTON))
        currency_button.click()
        gbp_button = self.wait.until(EC.element_to_be_clickable(self.GBP_BUTTON))
        gbp_button.click()
        return self

    def check_gbp_currency(self):
        self.wait.until(EC.presence_of_element_located(self.GBP_CURRENCY))

