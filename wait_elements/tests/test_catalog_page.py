import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.catalog_page import CatalogPage


def test_catalog_page(browser, url):
    browser.get(url + "index.php?route=product/category&path=25_28")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(CatalogPage.LIST_VIEW_BUTTON))
    wait.until(EC.visibility_of_element_located(CatalogPage.GRID_VIEW_BUTTON))
    wait.until(EC.visibility_of_element_located(CatalogPage.SORT_INPUT))
    wait.until(EC.visibility_of_element_located(CatalogPage.SHOW_LIMIT_INPUT))
    wait.until(EC.visibility_of_element_located(CatalogPage.PRODUCT_COMPARE_LINK))
    time.sleep(2)  # Для демонстрации