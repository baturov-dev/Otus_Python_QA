from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.admin_page import AdminPage
from pages.base_page import BasePage


class AdminLoginPage(BasePage):
    USERNAME_INPUT = (By.XPATH, "//input[@id='input-username']")
    PASSWORD_INPUT = (By.XPATH, "//input[@id='input-password']")
    LOGIN_BUTTON = (By.XPATH, "//button[@class='btn btn-primary']")

    def open(self):
        self.driver.get(self.url + "admin")
        return self

    def admin_login(self):
        login_username = self.wait.until(EC.element_to_be_clickable(self.USERNAME_INPUT))
        login_username.send_keys("user")
        login_password = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        login_password.send_keys("bitnami")
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()
        return AdminPage(self.driver, self.url)


