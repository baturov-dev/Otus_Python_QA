from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.wishlist_page import WishListPage


class AccountPage(BasePage):
    WISHLIST_LINK_TEXT = (By.LINK_TEXT, "Wish List")
    NEW_PAYMENT = (By.ID, "payment-new")

    def click_wishlist_link(self):
        footer_wishlist_link = self.wait.until(EC.element_to_be_clickable(self.WISHLIST_LINK_TEXT))
        footer_wishlist_link.click()
        return WishListPage(self.driver, self.url)

    def check_new_payment(self):
        self.wait.until(EC.visibility_of_element_located(self.NEW_PAYMENT))
