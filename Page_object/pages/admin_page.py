from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.admin_products_page import AdminProductsPage


class AdminPage(BasePage):
    CATALOG_LINK = (By.ID, "menu-catalog")
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog li:nth-child(2)")

    def open_admin_products(self):
        catalog_link = self.wait.until(EC.element_to_be_clickable(self.CATALOG_LINK))
        catalog_link.click()
        product_link = self.wait.until(EC.element_to_be_clickable(self.CATALOG_MENU))
        product_link.click()
        return AdminProductsPage(self.driver, self.url)


