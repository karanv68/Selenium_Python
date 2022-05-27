from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class web_element_attribute():
    def web_ele_attribute(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        attribute = driver.find_element(By.XPATH,"//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").get_attribute("value")
        print(attribute)
        time.sleep(2)
        driver.quit()

findbyid = web_element_attribute()
findbyid.web_ele_attribute()