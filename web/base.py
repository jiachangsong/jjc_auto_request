from selenium import webdriver


class Base:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://ceshiren.com/")
        self.driver.implicitly_wait(3)

    def teardown(self):
        pass
        # self.driver.quit()