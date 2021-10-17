from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.product_page import ProductPage


class MainPage(BasePage):
    PRODUCT = (By.XPATH, '//div[@class="image"]//img[@title="MacBook"]')
    PRODUCT_NAME = (By.CSS_SELECTOR, ".caption h4 a")

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
