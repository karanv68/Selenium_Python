from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemoFindElementByCSSselector():
    def locate_by_cssSelector_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_css_selector("#login-input").send_keys('test@test.com')
        time.sleep(4)

findbyid = DemoFindElementByCSSselector()
findbyid.locate_by_cssSelector_demo()