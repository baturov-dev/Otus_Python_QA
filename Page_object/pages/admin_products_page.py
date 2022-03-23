from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class AdminProductsPage(BasePage):
    ADD_PRODUCT = (By.XPATH, '//a[@data-original-title="Add New"]')
    DELETE_PRODUCT = (By.XPATH, "//button[@data-original-title='Delete']")
    ALERT_SUCCESS = (By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')

    def add_product(self):
        add_product_button = self.wait.until(EC.element_to_be_clickable(self.ADD_PRODUCT))
        add_product_button.click()
        return AdminProductFormPage(self.driver, self.url)

    def check_name_added_product(self, name):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, f'//td[text()="{name}"]')))

    def delete_product(self):
        delete_product_button = self.wait.until(EC.element_to_be_clickable(self.DELETE_PRODUCT))
        delete_product_button.click()
        return AdminProductsPage(self.driver, self.url)

    def click_product_checkbox(self, name):
        product_checkbox = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, f'//td[text()="{name}"]/preceding-sibling::td/input'))
        )
        product_checkbox.click()

    def confirm_delete_product(self):
        alert = Alert(self.driver)
        alert.accept()

    def check_product_delete(self):
        self.wait.until(EC.visibility_of_element_located(self.ALERT_SUCCESS))


class AdminProductFormPage(BasePage):
    PRODUCT_NAME = (By.ID, "input-name1")
    META_TAG_TITLE = (By.ID, "input-meta-title1")
    PRODUCT_MODEL = (By.ID, "input-model")
    TAB_NAVIGATOR = (By.XPATH, "//ul[@class='nav nav-tabs']/li[2]")
    SAVE_BUTTON = (By.XPATH, "//i[@class='fa fa-save']")

    def fill_product_data(self, name):
        product_name = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_NAME))
        product_name.send_keys(name)
        meta_tag_title = self.wait.until(EC.element_to_be_clickable(self.META_TAG_TITLE))
        meta_tag_title.send_keys("Iphone")
        data_tab = self.wait.until(EC.element_to_be_clickable(self.TAB_NAVIGATOR))
        data_tab.click()
        product_model = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_MODEL))
        product_model.send_keys("13")
        return self

    def save_product_data(self):
        save_button = self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON))
        save_button.click()
        return AdminProductsPage(self.driver, self.url)
