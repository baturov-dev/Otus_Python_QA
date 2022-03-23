from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class SuccessPage(BasePage):
    SUCCESS_CONTINUE_BUTTON = (By.XPATH, '//a[@class="btn btn-primary"]')

    def check_success_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUCCESS_CONTINUE_BUTTON))
