from time import sleep


from web.base import Base


class TestWait(Base):

    def test_wait1(self):
        self.driver.find_element_by_link_text("热门").click()
        self.driver.find_element_by_link_text("精华帖").click()
        print("hello")

