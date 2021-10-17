from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.admin_products_page import AdminProductsPage


class AdminLoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//input[@id='input-username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='input-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")

    def open(self):
        self.driver.get(self.url + "admin")
        return self

    def admin_login(self):
        login_username = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
        login_username.send_keys("demo")
        login_password = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        login_password.send_keys("demo")
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()
        return self


class AdminPage(BasePage):
    CATALOG_LINK = (By.ID, "menu-catalog")
    CATALOG_MENU = (By.ID, "collapse1")

    def open_admin_products(self):
        catalog_link = self.wait.until(EC.element_to_be_clickable(self.CATALOG_LINK))
        catalog_link.click()
        product_link = self.driver.find_elements(*self.CATALOG_MENU)[1]
        product_link.click()
        return AdminProductsPage(self.driver, self.url)
