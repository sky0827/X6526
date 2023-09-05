from selenium.common.exceptions import NoSuchElementException

class Base_page:
    def __init__(self,driver):
        self.driver=driver

    def get_element(self,*loc):
        return self.driver.find_element(*loc)

    def get_elements(self,*loc):
        return self.driver.find_elements(*loc)

    def back_button(self):
        return self.driver.keyevent(4)

    # 找不到元素就下滑,找到就点击
    def no_element_swipe(self,*loc):
        while True:
            try:
                self.driver.find_element(*loc).click()
                break
            except NoSuchElementException:
                self.driver.swipe(333,1319,333,1000)

    # 找不到元素不做操作，找到就点击
    def no_element_noactioin(self,*loc):
        while True:
            try:
                self.driver.find_element(*loc).click()
                break
            except NoSuchElementException:
                break
