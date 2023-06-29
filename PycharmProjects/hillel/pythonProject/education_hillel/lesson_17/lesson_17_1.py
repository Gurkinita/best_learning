import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_1(browser):
    browser.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    browser.set_window_size(1920, 1080)

    wait = WebDriverWait(browser, 10)
    bank_manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button")))
    bank_manager_login_btn.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.center > button:nth-child(1)")))

    transfer_btn = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.center > button:nth-child(1)")
    transfer_btn.click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input")))

    input_field1 = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(1) > input")
    input_field1.send_keys("ЮЛИЯ")
    time.sleep(2)

    input_field2 = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(2) > input")
    input_field2.send_keys("Reach bitch")
    time.sleep(2)

    input_field3 = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > div:nth-child(3) > input")
    input_field3.send_keys("65000")
    time.sleep(2)

    button = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button")
    button.click()
    time.sleep(2)


def test_2(browser):
    browser.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    browser.set_window_size(1920, 1080)

    wait = WebDriverWait(browser, 10)
    bank_manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button")))
    bank_manager_login_btn.click()
    time.sleep(1)

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.center > button:nth-child(2)")))

    open_account_btn = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.center > button:nth-child(2)")
    open_account_btn.click()
    time.sleep(2)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#userSelect")))
    time.sleep(1)

    select_user = Select(browser.find_element(By.CSS_SELECTOR, "#userSelect"))
    select_user.select_by_index(2)
    time.sleep(1)

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#currency")))
    time.sleep(1)

    select_currency = Select(browser.find_element(By.CSS_SELECTOR, "#currency"))
    select_currency.select_by_index(3)
    time.sleep(1)

    submit_btn = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > form > button")
    submit_btn.click()


def test_3(browser):
    browser.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")
    browser.set_window_size(1920, 1080)

    wait = WebDriverWait(browser, 10)
    bank_manager_login_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.borderM.box.padT20 > div:nth-child(3) > button")))
    bank_manager_login_btn.click()

    wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "body > div > div > div.ng-scope > div > div.center > button:nth-child(3)")))

    button_3 = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.center > button:nth-child(3)")
    button_3.click()

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > button")))

    table_button = browser.find_element(By.CSS_SELECTOR,
    "body > div > div > div.ng-scope > div > div.ng-scope > div > div > table > tbody > tr:nth-child(1) > td:nth-child(5) > button")
    table_button.click()
