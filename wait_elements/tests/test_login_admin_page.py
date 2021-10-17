import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.login_admin_page import LoginAdminPage


def test_login_admin_page(browser, url):
    browser.get(url + "/admin")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located(LoginAdminPage.USERNAME_INPUT))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.PASSWORD_INPUT))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.SUBMIT_BUTTON))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.FORGOTTEN_PASSWORD))
    wait.until(EC.visibility_of_element_located(LoginAdminPage.OPENCART_LINK))
    time.sleep(2)  # Для демонстрации
