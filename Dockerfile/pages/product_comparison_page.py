from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Dockerfile.pages.base_page import BasePage
from Dockerfile.pages.shopping_cart import ShoppingCart
import allure


class ProductComparisonPage(BasePage):
    COMPARISON_PAGE_CONTENT = (By.CSS_SELECTOR, "#content")
    COMPARISON_PAGE_ADD_TO_CART = (By.CSS_SELECTOR, "input[value='Add to Cart']")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    SHOPPING_CART_LINK_TEXT = (By.LINK_TEXT, "shopping cart")

    def check_name_product_comparison_cart(self, name):
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, name)))

    @allure.step("Add product to cart from comparison page")
    def add_to_cart_product_comparison_page(self):
        self.wait.until(EC.visibility_of_element_located(self.COMPARISON_PAGE_CONTENT))
        self.logger.info("Clicking element: {}".format(self.COMPARISON_PAGE_ADD_TO_CART))
        add_to_cart_on_comparison_page = self.wait.until(EC.element_to_be_clickable(self.COMPARISON_PAGE_ADD_TO_CART))
        add_to_cart_on_comparison_page.click()
        return self

    @allure.step("Open shopping cart")
    def open_shopping_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.ALERT_SUCCESS))
        self.logger.info("Clicking element: {}".format(self.SHOPPING_CART_LINK_TEXT))
        shopping_cart_link = self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART_LINK_TEXT))
        shopping_cart_link.click()
        return ShoppingCart(self.driver, self.url)
