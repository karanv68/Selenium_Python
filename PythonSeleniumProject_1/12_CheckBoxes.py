from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemoCheckBox():
    def locate_by_tag_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.find_element_by_id("//a[normalize-space()='Non Stop Flights']").click()
        time.sleep(3)

        state = driver.find_element_by_id("//a[normalize-space()='Non Stop Flights']").is_selected()
        print(state)
        
checkbox = DemoCheckBox()
checkbox.locate_by_tag_demo()