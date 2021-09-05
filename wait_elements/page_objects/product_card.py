from selenium.webdriver.common.by import By


class ProductCard:
    ADD_TO_WISH_LIST_BUTTON = (By.XPATH, "//div[@class='col-sm-4']//button[@data-original-title='Add to Wish List']")
    COMPARE_THIS_PRODUCT_BUTTON = (By.CSS_SELECTOR, "button[data-original-title='Compare this Product']")
    QUANTITY_INPUT = (By.NAME, "quantity")
    ADD_TO_CART_BUTTON = (By.XPATH, "//button[@id='button-cart']")
    SPECIFICATION = (By.LINK_TEXT, "Specification")
