import os
import pytest
import datetime
import logging
import allure
from selenium import webdriver
from selenium.webdriver.opera.options import Options as OperaOptions
from pathlib import Path

from Dockerfile.pages.main_page import MainPage
from Dockerfile.pages.admin_login_page import AdminLoginPage

DRIVERS = os.path.expanduser("~/Downloads/drivers")


def pytest_addoption(parser):
    parser.addoption("--maximized", action="store_true", help="Maximize browser windows")
    parser.addoption("--headless", action="store_true", help="Run headless")
    parser.addoption("--browser", action="store", default="chrome", choices=["chrome", "firefox", "opera"])
    parser.addoption("--url", action="store", default="http://192.168.1.69:8081/")
    parser.addoption("--log_level", action="store", default="DEBUG")
    parser.addoption("--executor", action="store", default="192.168.1.69")


@pytest.fixture(scope="session", autouse=True)
def logs_folder():
    folder = Path(__file__).parent.joinpath("logs")
    if not folder.exists():
        folder.mkdir()
    return folder


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    try:
        if rep.when == 'call' and rep.failed:
            if 'browser' in item.fixturenames:
                web_driver = item.funcargs['browser']
            else:
                print('Fail to take screen-shot')
                return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        print('Fail to take screen-shot: {}'.format(e))


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    maximized = request.config.getoption("--maximized")
    log_level = request.config.getoption("--log_level")
    executor = request.config.getoption("--executor")

    logger = logging.getLogger("driver")
    test_name = request.node.name

    logger.addHandler(logging.FileHandler(f"logs/{test_name}.log"))
    logger.setLevel(level=log_level)

    logger.info("===> Test {} started at {}".format(test_name, datetime.datetime.now()))

    driver = None

    if executor == "local":
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.headless = True
            driver = webdriver.Chrome(executable_path=f"{DRIVERS}/chromedriver", options=options)
        elif browser == "opera":
            options = OperaOptions()
            if headless:
                options.headless = True
            driver = webdriver.Opera(executable_path=f"{DRIVERS}/operadriver", options=options)
        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.headless = True
            driver = webdriver.Firefox(executable_path=f"{DRIVERS}/geckodriver", options=options)
    else:
        executor_url = f"http://{executor}:4444/wd/hub"
        capabilities = {
            "browserName": browser,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities=capabilities)

    driver.test_name = test_name
    driver.log_level = log_level
    logger.info("Browser:{}".format(browser, driver.capabilities))

    if maximized:
        driver.maximize_window()

    def final():
        driver.quit()
        logger.info("===> Test {} finished at {}".format(test_name, datetime.datetime.now()))

    request.addfinalizer(final)

    return driver


@pytest.fixture
def main_page(browser, url):
    return MainPage(browser, url).open()


@pytest.fixture
def admin_page(browser, url):
    page = AdminLoginPage(browser, url).open()
    return page.admin_login()
