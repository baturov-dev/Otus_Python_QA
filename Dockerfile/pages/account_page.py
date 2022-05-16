from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Dockerfile.pages.base_page import BasePage
from Dockerfile.pages.wishlist_page import WishListPage
import allure


class AccountPage(BasePage):
    WISHLIST_LINK_TEXT = (By.LINK_TEXT, "Wish List")
    NEW_PAYMENT = (By.ID, "payment-new")

    @allure.step("Click the wishlist link")
    def click_wishlist_link(self):
        self.logger.info("Clicking element: {}".format(self.WISHLIST_LINK_TEXT))
        footer_wishlist_link = self.wait.until(EC.element_to_be_clickable(self.WISHLIST_LINK_TEXT))
        footer_wishlist_link.click()
        return WishListPage(self.driver, self.url)

    @allure.step("Check new payment")
    def check_new_payment(self):
        self.wait.until(EC.visibility_of_element_located(self.NEW_PAYMENT))
