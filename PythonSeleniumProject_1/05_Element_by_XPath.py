from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemoFindElementByxPath():
    def locate_by_xpath_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_xpath("//input[@id='login-input]").send_keys('test@test.com')
        time.sleep(4)

findbyid = DemoFindElementByxPath()
findbyid.locate_by_xpath_demo()