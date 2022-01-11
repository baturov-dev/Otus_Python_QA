from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class AdminProductsPage(BasePage):
    ADD_PRODUCT = (By.XPATH, "//a[@data-original-title='Add New']")

    def add_product(self):
        add_product_button = self.wait.until(EC.element_to_be_clickable(self.ADD_PRODUCT))
        add_product_button.click()
        return AdminProductFormPage(self.driver, self.url)

    def check_name_added_product(self, name):
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, name)))


class AdminProductFormPage(BasePage):
    PRODUCT_NAME = (By.ID, "input-name1")
    META_TAG_TITLE = (By.ID, "input-meta-title1")
    PRODUCT_MODEL = (By.ID, "input-model")
    TAB_NAVIGATOR = (By.XPATH, "//ul[@class='nav nav-tabs']")
    SAVE_BUTTON = (By.XPATH, "//i[@class='fa fa-save']")

    def fill_product_data(self):
        product_name = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_NAME))
        product_name.send_keys("Iphone13")
        meta_tag_title = self.wait.until(EC.element_to_be_clickable(self.META_TAG_TITLE))
        meta_tag_title.send_keys("Iphone")
        data_tab = self.driver.find_elements(*self.TAB_NAVIGATOR)[1]
        data_tab.click()
        product_model = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_MODEL))
        product_model.send_keys("13")
        return self

    def save_product_data(self):
        save_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_button.click()
        return AdminProductsPage(self.driver, self.url)
