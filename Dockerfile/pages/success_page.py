from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Dockerfile.pages.base_page import BasePage
import allure


class SuccessPage(BasePage):
    SUCCESS_CONTINUE_BUTTON = (By.XPATH, '//a[@class="btn btn-primary"]')

    @allure.step("Appearance of the success continue button after registration")
    def check_success_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SUCCESS_CONTINUE_BUTTON))
