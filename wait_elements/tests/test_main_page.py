import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.main_page import MainPage


def test_login_admin_page(browser, url):
    browser.get(url)
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(MainPage.SEARCH_BUTTON))
    wait.until(EC.visibility_of_element_located(MainPage.SHOPPING_CART_BUTTON))
    wait.until(EC.visibility_of_element_located(MainPage.YOUR_STORE_LINK))
    wait.until(EC.visibility_of_element_located(MainPage.CURRENCY_BUTTON))
    wait.until(EC.visibility_of_element_located(MainPage.DESKTOPS_BUTTON))
    time.sleep(2)  # Для демонстрации