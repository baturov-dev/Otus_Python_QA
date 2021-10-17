import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.product_card import ProductCard


def test_catalog_page(browser, url):
    browser.get(url + "index.php?route=product/product&product_id=43")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(ProductCard.ADD_TO_WISH_LIST_BUTTON))
    wait.until(EC.visibility_of_element_located(ProductCard.COMPARE_THIS_PRODUCT_BUTTON))
    wait.until(EC.visibility_of_element_located(ProductCard.QUANTITY_INPUT))
    wait.until(EC.visibility_of_element_located(ProductCard.ADD_TO_CART_BUTTON))
    wait.until(EC.visibility_of_element_located(ProductCard.SPECIFICATION))
    time.sleep(2)  # Для демонстрации