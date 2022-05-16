from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Dockerfile.pages.base_page import BasePage
from Dockerfile.pages.login_page import LoginPage
import allure


class ShoppingCart(BasePage):
    SHOPPING_CART_BUTTONS = (By.CSS_SELECTOR, ".buttons")
    CHECKOUT_BUTTON = (By.XPATH, "//div[@class='pull-right']")

    @allure.step("Check the product in the shopping cart")
    def check_name_shopping_cart(self, name):
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, name)))

    def click_checkout_button(self):
        self.logger.info("Clicking element: {}".format(self.CHECKOUT_BUTTON))
        checkout_button = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        checkout_button.click()
        return LoginPage(self.driver, self.url)
