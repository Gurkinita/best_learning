from selenium import webdriver
from selenium.webdriver.common.by import By
import time


from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Test1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test1(self):
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.LINK_TEXT, "File Download").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "1.txt").click()
        time.sleep(2)



class Test2():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test2(self):
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.LINK_TEXT, "Checkboxes").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(1)").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(3)").click()


class Test3():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test3(self):
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.set_window_size(1920, 1080)
        self.driver.find_element(By.LINK_TEXT, "Dynamic Loading").click()
        time.sleep(2)
        self.driver.find_element(By.LINK_TEXT, "Example 1: Element on page that is hidden").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "button").click()