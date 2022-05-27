from webbrowser import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemoFindElementsBYCLass():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element(By.ID,'login-input').send_keys('9718069416')
        time.sleep(3)
        driver.quit()
        
findelements = DemoFindElementsBYCLass()
findelements.locate_by_id_demo()