from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class web_element_text():
    def web_ele_text(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com")
        text = driver.find_element(By.XPATH,"//p[contains(text(),'On Yatra.com, you can tailor your trip from end-to')]").text
        print(text)
        time.sleep(2)
        driver.quit()

findbyid = web_element_text()
findbyid.web_ele_text()