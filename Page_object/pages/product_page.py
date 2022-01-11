from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.login_page import LoginPage
from pages.shopping_cart import ShoppingCart
from pages.product_comparison_page import ProductComparisonPage


class ProductPage(BasePage):
    ADD_TO_WISH_LIST_BUTTON = (By.XPATH, "//div[@class='col-sm-4']//button[@data-original-title='Add to Wish List']")
    LOGIN_PAGE_LINK = (By.LINK_TEXT, "login")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    SHOPPING_CART_LINK_TEXT = (By.LINK_TEXT, "shopping cart")
    COMPARE_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
    PRODUCT_COMPARISON_LINK_TEXT = (By.LINK_TEXT, "product comparison")

    def add_to_wishlist(self):
        wishlist_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_WISH_LIST_BUTTON))
        wishlist_button.click()
        return self

    def open_login_page(self):
        login_link = self.wait.until(EC.element_to_be_clickable(self.LOGIN_PAGE_LINK))
        login_link.click()
        return LoginPage(self.driver, self.url)

    def add_to_shopping_cart(self):
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        return self

    def open_shopping_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.ALERT_SUCCESS)) #Нужно ли???
        shopping_cart_link = self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART_LINK_TEXT))
        shopping_cart_link.click()
        return ShoppingCart(self.driver, self.url)

    def compare_this_product(self):
        compare_product_button = self.wait.until(EC.element_to_be_clickable(self.COMPARE_BUTTON))
        compare_product_button.click()
        return self

    def click_product_comparison_link(self):
        self.wait.until(EC.visibility_of_element_located(self.ALERT_SUCCESS))
        product_comparison_link = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_COMPARISON_LINK_TEXT))
        product_comparison_link.click()
        return ProductComparisonPage(self.driver, self.url)