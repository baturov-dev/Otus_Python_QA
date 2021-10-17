from selenium.webdriver.common.by import By


class CatalogPage:
    LIST_VIEW_BUTTON = (By.XPATH, "//button[@id='list-view']")
    GRID_VIEW_BUTTON = (By.CSS_SELECTOR, "#grid-view")
    SORT_INPUT = (By.XPATH, "//select[@id='input-sort']")
    SHOW_LIMIT_INPUT = (By.XPATH, "//select[@id='input-limit']")
    PRODUCT_COMPARE_LINK = (By.CSS_SELECTOR, "#compare-total")
