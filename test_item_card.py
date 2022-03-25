from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ITEM_URL = "https://www.opencart.ru/microdatapro"


def test_logo_pic(browser):
    driver = browser
    driver.get(ITEM_URL
               )
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "header-logo")))


def test_buy_button(browser):
    driver = browser
    driver.get(ITEM_URL
               )
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Купить')]")))


def test_price(browser):
    driver = browser
    driver.get(ITEM_URL
               )
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "purchase__price")))


def test_item_description(browser):
    driver = browser
    driver.get(ITEM_URL
               )
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Описание')]")))

def test_item_data(browser):
    driver = browser
    driver.get(ITEM_URL
               )
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Характеристики')]")))