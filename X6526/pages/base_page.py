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

    # 判断元素是否可以点击
    def check_element_click(self,*loc):
        return self.driver.find_element(*loc).is_enabled()

    #  获取界面中所有元素开关
    def get_all_buttons(self,*loc):
        return self.driver.find_elements(*loc)

    #  检查元素开关状态
    def check_element_button(self,*loc):
        return self.driver.find_element(*loc).get_attribute("checked")

    # 判断元素开关为开  如果为关则打开
    def element_button_ison(self,loc):
        if loc.get_attribute("checked")=='true':
            pass
        else:
            loc.click()

    # 判断元素开关为关  如果为开则关闭
    def element_button_isoff(self,loc):
        if loc.get_attribute("checked")=='false':
            pass
        else:
            loc.click()





