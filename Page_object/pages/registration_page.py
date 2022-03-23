from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.success_page import SuccessPage


class RegistrationPage(BasePage):
    FIRST_NAME = (By.XPATH, '//input[@id="input-firstname"]')
    LAST_NAME = (By.XPATH, '//input[@id="input-lastname"]')
    E_MAIL = (By.XPATH, '//input[@id="input-email"]')
    TELEPHONE = (By.XPATH, '//input[@id="input-telephone"]')
    PASSWORD = (By.XPATH, '//input[@id="input-password"]')
    PASSWORD_CONFIRM = (By.XPATH, '//input[@id="input-confirm"]')
    CHECKBOX = (By.XPATH, '//input[@type="checkbox"]')
    CONTINUE_BUTTON = (By.XPATH, '//input[@type="submit"]')

    def fill_account_data(self):
        first_name = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME))
        first_name.send_keys("Test1")
        last_name = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME))
        last_name.send_keys("Test2")
        e_mail = self.wait.until(EC.element_to_be_clickable(self.E_MAIL))
        e_mail.send_keys("test4@mail.ru")
        telephone = self.wait.until(EC.element_to_be_clickable(self.TELEPHONE))
        telephone.send_keys("88888888")
        password = self.wait.until(EC.element_to_be_clickable(self.PASSWORD))
        password.send_keys("12345678")
        password_confirm = self.wait.until(EC.element_to_be_clickable(self.PASSWORD_CONFIRM))
        password_confirm.send_keys("12345678")
        checkbox = self.wait.until(EC.element_to_be_clickable(self.CHECKBOX))
        checkbox.click()

    def continue_registration(self):
        continue_button = self.wait.until(EC.element_to_be_clickable(self.CONTINUE_BUTTON))
        continue_button.click()
        return SuccessPage(self.driver, self.url)