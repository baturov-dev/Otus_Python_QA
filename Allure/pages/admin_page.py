from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from Allure.pages.base_page import BasePage
from Allure.pages.admin_products_page import AdminProductsPage
import allure


class AdminPage(BasePage):
    CATALOG_LINK = (By.ID, "menu-catalog")
    CATALOG_MENU = (By.CSS_SELECTOR, "#menu-catalog li:nth-child(2)")

    @allure.step("Open products page in the admin panel")
    def open_admin_products(self):
        self.logger.info("Clicking element: {}".format(self.CATALOG_LINK))
        catalog_link = self.wait.until(EC.element_to_be_clickable(self.CATALOG_LINK))
        catalog_link.click()
        self.logger.info("Clicking element: {}".format(self.CATALOG_MENU))
        product_link = self.wait.until(EC.element_to_be_clickable(self.CATALOG_MENU))
        product_link.click()
        return AdminProductsPage(self.driver, self.url)


