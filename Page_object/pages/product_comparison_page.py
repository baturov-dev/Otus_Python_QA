from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.shopping_cart import ShoppingCart


class ProductComparisonPage(BasePage):
    COMPARISON_PAGE_CONTENT = (By.CSS_SELECTOR, "#content")
    COMPARISON_PAGE_ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to Cart']")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    SHOPPING_CART_LINK_TEXT = (By.LINK_TEXT, "shopping cart")

    def check_name_product_comparison_cart(self, name):
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, name)))

    def add_to_cart_product_comparison_page(self):
        self.wait.until(EC.visibility_of_element_located(self.COMPARISON_PAGE_CONTENT)) #нужно ли?
        add_to_cart_on_comparison_page = self.wait.until(EC.element_to_be_clickable(self.COMPARISON_PAGE_ADD_TO_CART))
        add_to_cart_on_comparison_page.click()
        return self

    def open_shopping_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.ALERT_SUCCESS)) #Нужно ли???
        shopping_cart_link = self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART_LINK_TEXT))
        shopping_cart_link.click()
        return ShoppingCart(self.driver, self.url)
