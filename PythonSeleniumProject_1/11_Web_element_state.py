from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemoFindElementState():
    def locate_by_tag_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        State = driver.find_element_by_xpath("//button[@id='login-continue-btn']").is_enabled()
        print(State)
findelements = DemoFindElementState()
findelements.locate_by_tag_demo()

