from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemoFindElementtagandClassname():
    def locate_by_tagName_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_tag_name("input").send_keys('test@test.com')
        time.sleep(4)

    def locate_by_className(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_class_name("email-login-box").send_keys('test@test.com')
        time.sleep(4)


findbyid = DemoFindElementtagandClassname()
findbyid.locate_by_className()