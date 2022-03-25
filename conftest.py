import pytest

from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--url", action="store", default="https://www.opencart.ru/")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser == "chrome":
        driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    elif browser == "yandex":
        driver = webdriver.Chrome(executable_path="drivers/yandexdriver")
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "opera":
        driver = webdriver.Opera()
    elif browser == "safari":
        driver = webdriver.Safari()
    driver.maximize_window()
    request.addfinalizer(driver.close)
    return driver


@pytest.fixture()
def url(request):
    return request.config.getoption("--url")
