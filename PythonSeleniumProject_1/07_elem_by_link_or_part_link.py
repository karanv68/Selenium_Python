from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemoFindElementlink():
    def locate_by_link_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.find_element_by_link_text("Yatra for Business").click()
        time.sleep(4)
    
    def locate_by_Plink_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        driver.find_element_by_partial_link_text("Yatra for").click()
        time.sleep(4)

findbyid = DemoFindElementlink()
#findbyid.locate_by_link_demo()
findbyid.locate_by_Plink_demo()