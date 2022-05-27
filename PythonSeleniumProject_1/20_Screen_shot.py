from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")

demo = driver.find_element(By.XPATH,"//button[@id='login-continue-btn']")
demo.screenshot(".\\test.png")

demo.click()
time.sleep(2)
driver.get_screenshot_as_file(".\\error.png")
time.sleep(3)
driver.save_screenshot(".\\ss.png")
