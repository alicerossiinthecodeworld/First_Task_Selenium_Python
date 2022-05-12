from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

MODULE_URL = "https://www.opencart.ru/modules/"


def test_link_photos(browser):
    driver = browser
    driver.get(MODULE_URL
               )
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "img-responsive")))


def test_search_button(browser):
    driver = browser
    driver.get(MODULE_URL
               )
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "button-filter")))


def test_price_filters(browser):
    driver = browser
    driver.get(MODULE_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "radio")))


def test_catalog_search(browser):
    driver = browser
    driver.get(MODULE_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "catalog_search")))


def test_buy_buttons(browser):
    driver = browser
    driver.get(MODULE_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "slider__item-btn")))
