from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Allure.pages.base_page import BasePage
import allure


class WishListPage(BasePage):

    @allure.step("Check the product on the wishlist page")
    def check_name_present(self, name):
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, name)))
