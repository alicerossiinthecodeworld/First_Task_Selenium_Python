from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.wait import WebDriverWait

MAIN_PAGE_URL = "https://www.opencart.ru/"


def test_logo(browser):
    driver = browser
    driver.get(MAIN_PAGE_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "header-logo")))


def test_contact_list(browser):
    driver = browser
    driver.get(MAIN_PAGE_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Контакты')]")))


def test_download_button(browser):
    driver = browser
    driver.get(MAIN_PAGE_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Скачать бесплатно')]")))


def test_demo_button(browser):
    driver = browser
    driver.get(MAIN_PAGE_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Онлайн-демо')]")))


def test_support_button(browser):
    driver = browser
    driver.get(MAIN_PAGE_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "suport__link")))
