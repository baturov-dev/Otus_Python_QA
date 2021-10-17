from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class WishListPage(BasePage):
    def check_name_present(self, name):
        self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, name)))
