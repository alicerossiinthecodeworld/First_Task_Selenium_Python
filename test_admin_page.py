from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

ADMIN_URL = "http://demo-opencart.ru/admin/index.php"


def test_logo(browser):
    driver = browser
    driver.get(ADMIN_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "header-logo")))


def test_login_button(browser):
    driver = browser
    driver.get(ADMIN_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-primary")))


def test_forgot_password(browser):
    driver = browser
    driver.get(ADMIN_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Забыли пароль?')]")))


def test_login_field_input(browser):
    driver = browser
    driver.get(ADMIN_URL)
    login_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username")))
    login_field.send_keys("alicerossi")


def test_password_field_input(browser):
    driver = browser
    driver.get(ADMIN_URL)
    login_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password")))
    login_field.send_keys("sekret123")
