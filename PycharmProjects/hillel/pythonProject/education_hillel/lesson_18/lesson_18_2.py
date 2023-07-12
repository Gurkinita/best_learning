from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import allure


class Test1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_1(self):
        self.driver.get("http://uitestingplayground.com/home")
        self.driver.set_window_size(1920, 1080)
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Click").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "badButton").click()
        time.sleep(2)


class Test2():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_2(self):
        self.driver.get("http://uitestingplayground.com/home")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.LINK_TEXT, "Scrollbars").click()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(6)")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "hidingButton").click()
        self.driver.find_element(By.ID, "hidingButton").click()
        self.driver.find_element(By.ID, "hidingButton").click()
        element = self.driver.find_element(By.ID, "hidingButton")
        actions = ActionChains(self.driver)
        actions.double_click(element).perform()


class Test3():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_3(self):
        self.driver.get("http://uitestingplayground.com/home")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.LINK_TEXT, "Text Input").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "newButtonName").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "newButtonName").send_keys("test button ")
        time.sleep(2)
        self.driver.find_element(By.ID, "updatingButton").click()
        time.sleep(2)
        self.driver.find_element(By.ID, "updatingButton").click()
        time.sleep(2)