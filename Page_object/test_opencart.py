import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_add_to_wish_list(main_page):
    product_name = main_page.get_product_name()
    product_page = main_page.open_first_product()
    product_page.add_to_wishlist()
    login_page = product_page.open_login_page()
    account_page = login_page.login_user()
    wishlist_page = account_page.click_wishlist_link()
    wishlist_page.check_name_present(product_name)


def test_add_to_cart(main_page):
    product_name = main_page.get_product_name()
    product_page = main_page.open_first_product()
    product_page.add_to_shopping_cart()
    shopping_cart = product_page.open_shopping_cart()
    shopping_cart.check_name_shopping_cart(product_name)
    login_page = shopping_cart.click_checkout_button()
    account_page = login_page.login_user()
    account_page.check_new_payment()


def test_add_to_cart_from_comparison(main_page):
    product_name = main_page.get_product_name()
    product_page = main_page.open_first_product()
    product_page.compare_this_product()
    product_comparison_page = product_page.click_product_comparison_link()
    product_comparison_page.check_name_product_comparison_cart(product_name)
    product_comparison_page.add_to_cart_product_comparison_page()
    shopping_cart = product_comparison_page.open_shopping_cart()
    shopping_cart.check_name_shopping_cart(product_name)
    shopping_cart.click_checkout_button()
    login_page = shopping_cart.click_checkout_button()
    account_page = login_page.login_user()
    account_page.check_new_payment()


def test_add_product_admin_page(admin_page):
    products_page = admin_page.open_admin_products()
    add_product_form = products_page.add_product()
    add_product_form.fill_product_data()
    products_page = add_product_form.save_product_data()
    products_page.check_name_added_product()
