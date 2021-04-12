import selenium
from selenium import webdriver
import time

class TestHog():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        print("11111111")

    def teardown(self):
        self.driver.quit()

    def test_selenium(self):
        self.driver.get("http://ceshiren.com/")
        self.driver.find_element_by_link_text("热门").click()
        self.driver.find_element_by_link_text("精华帖").click()
        time.sleep(10)