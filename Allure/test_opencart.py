import allure
PRODUCT_NAME = "Iphone13"


@allure.title("Add product to wishlist")
def test_add_to_wish_list(main_page):
    product_name = main_page.get_product_name()
    product_page = main_page.open_first_product()
    product_page.add_to_wishlist()
    login_page = product_page.open_login_page()
    account_page = login_page.login_user()
    wishlist_page = account_page.click_wishlist_link()
    wishlist_page.check_name_present(product_name)


@allure.title("Add product to shopping cart")
def test_add_to_cart(main_page):
    product_name = main_page.get_product_name()
    product_page = main_page.open_first_product()
    product_page.add_to_shopping_cart()
    shopping_cart = product_page.open_shopping_cart()
    shopping_cart.check_name_shopping_cart(product_name)
    login_page = shopping_cart.click_checkout_button()
    account_page = login_page.login_user()
    account_page.check_new_payment()


@allure.title("Add product to cart from comparison page")
def test_add_to_cart_from_comparison(main_page):
    product_name = main_page.get_product_name()
    product_page = main_page.open_first_product()
    product_page.compare_this_product()
    product_comparison_page = product_page.click_product_comparison_link()
    product_comparison_page.check_name_product_comparison_cart(product_name)
    product_comparison_page.add_to_cart_product_comparison_page()
    shopping_cart = product_comparison_page.open_shopping_cart()
    shopping_cart.check_name_shopping_cart(product_name)
    login_page = shopping_cart.click_checkout_button()
    account_page = login_page.login_user()
    account_page.check_new_payment()


@allure.title("Add new product in the admin panel")
def test_add_product_admin_page(admin_page):
    products_page = admin_page.open_admin_products()
    add_product_form = products_page.add_product()
    add_product_form.fill_product_data(PRODUCT_NAME)
    products_page = add_product_form.save_product_data()
    products_page.check_name_added_product(PRODUCT_NAME)


@allure.title("Delete product in the admin panel")
def test_delete_product_admin_page(admin_page):
    products_page = admin_page.open_admin_products()
    products_page.click_product_checkbox(PRODUCT_NAME)
    products_page.delete_product()
    products_page.confirm_delete_product()
    products_page.check_product_delete()


@allure.title("New user registration")
def test_account_registration(main_page):
    registration_page = main_page.open_registration_page()
    registration_page.fill_account_data()
    success_page = registration_page.continue_registration()
    success_page.check_success_button()


@allure.title("Change currency to euro")
def test_currency_to_euro(main_page):
    main_page.change_currency_to_euro()
    main_page.check_euro_currency()


@allure.title("Change currency to gbp")
def test_currency_to_gbp(main_page):
    main_page.change_currency_to_gbp()
    main_page.check_gbp_currency()
