from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.account_page import AccountPage
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_INPUT = (By.CSS_SELECTOR, "#input-email")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "#input-password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[value=Login]")

    def login_user(self):
        login_email = self.wait.until(EC.element_to_be_clickable(self.EMAIL_INPUT))
        login_email.send_keys("test2@mail.ru")
        login_password = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_INPUT))
        login_password.send_keys("test")
        login_button = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        login_button.click()
        return AccountPage(self.driver, self.url)

