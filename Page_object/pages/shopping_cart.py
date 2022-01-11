from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.login_page import LoginPage


class ShoppingCart(BasePage):
    SHOPPING_CART_BUTTONS = (By.CSS_SELECTOR, ".buttons")
    CHECKOUT_BUTTON = (By.XPATH, "//div[@class='pull-right']")

    def check_name_shopping_cart(self, name):
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, name)))

    def click_checkout_button(self):
        checkout_button = self.wait.until(EC.element_to_be_clickable(self.CHECKOUT_BUTTON))
        checkout_button.click()
        return LoginPage(self.driver, self.url)
