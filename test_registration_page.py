from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

REGISTER_URL = "https://www.opencart.ru/register/"


def test_first_name_input(browser):
    driver = browser
    driver.get(REGISTER_URL
               )
    firstname_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "firstname")))
    firstname_input.send_keys("alice")


def test_lastname_input(browser):
    driver = browser
    driver.get(REGISTER_URL)
    lastname_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "lastname")))
    lastname_input.send_keys("rossi")


def test_continue_button(browser):
    driver = browser
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-primary")))


def test_forgot_password_button(browser):
    driver = browser
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Забыли пароль?')]")))


def test_login_button(browser):
    driver = browser
    driver.get(REGISTER_URL)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(),'Вход')]")))
