from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Dockerfile.pages.base_page import BasePage
from Dockerfile.pages.login_page import LoginPage
from Dockerfile.pages.shopping_cart import ShoppingCart
from Dockerfile.pages.product_comparison_page import ProductComparisonPage
import allure


class ProductPage(BasePage):
    ADD_TO_WISH_LIST_BUTTON = (By.XPATH, "//div[@class='col-sm-4']//button[@data-original-title='Add to Wish List']")
    LOGIN_PAGE_LINK = (By.LINK_TEXT, "login")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    ALERT_SUCCESS = (By.CSS_SELECTOR, ".alert-success")
    SHOPPING_CART_LINK_TEXT = (By.LINK_TEXT, "shopping cart")
    COMPARE_BUTTON = (By.CSS_SELECTOR, "[data-original-title='Compare this Product']")
    PRODUCT_COMPARISON_LINK_TEXT = (By.LINK_TEXT, "product comparison")

    @allure.step("Add product to wishlist")
    def add_to_wishlist(self):
        self.logger.info("Clicking element: {}".format(self.ADD_TO_WISH_LIST_BUTTON))
        wishlist_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_WISH_LIST_BUTTON))
        wishlist_button.click()
        return self

    @allure.step("Open login page")
    def open_login_page(self):
        self.logger.info("Clicking element: {}".format(self.LOGIN_PAGE_LINK))
        login_link = self.wait.until(EC.element_to_be_clickable(self.LOGIN_PAGE_LINK))
        login_link.click()
        return LoginPage(self.driver, self.url)

    @allure.step("Add product to shopping cart")
    def add_to_shopping_cart(self):
        self.logger.info("Clicking element: {}".format(self.ADD_TO_CART_BUTTON))
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON))
        add_to_cart_button.click()
        return self

    @allure.step("Open shopping cart")
    def open_shopping_cart(self):
        self.wait.until(EC.visibility_of_element_located(self.ALERT_SUCCESS))
        self.logger.info("Clicking element: {}".format(self.SHOPPING_CART_LINK_TEXT))
        shopping_cart_link = self.wait.until(EC.element_to_be_clickable(self.SHOPPING_CART_LINK_TEXT))
        shopping_cart_link.click()
        return ShoppingCart(self.driver, self.url)

    @allure.step("Click compare product button")
    def compare_this_product(self):
        self.logger.info("Clicking element: {}".format(self.COMPARE_BUTTON))
        compare_product_button = self.wait.until(EC.element_to_be_clickable(self.COMPARE_BUTTON))
        compare_product_button.click()
        return self

    def click_product_comparison_link(self):
        self.wait.until(EC.visibility_of_element_located(self.ALERT_SUCCESS))
        self.logger.info("Clicking element: {}".format(self.PRODUCT_COMPARISON_LINK_TEXT))
        product_comparison_link = self.wait.until(EC.element_to_be_clickable(self.PRODUCT_COMPARISON_LINK_TEXT))
        product_comparison_link.click()
        return ProductComparisonPage(self.driver, self.url)