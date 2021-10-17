from selenium.webdriver.common.by import By


class MainPage:
    SEARCH_BUTTON = (By.XPATH, "//div[@id='search']/span[@class='input-group-btn']")
    SHOPPING_CART_BUTTON = (By.ID, "cart")
    YOUR_STORE_LINK = (By.LINK_TEXT, "Your Store")
    CURRENCY_BUTTON = (By.CSS_SELECTOR, "button[class='btn btn-link dropdown-toggle']")
    DESKTOPS_BUTTON = (By.LINK_TEXT, "Desktops")
