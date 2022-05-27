'''Command
driver.get("https://training.rcvacademy.com")
driver.current_url
driver.back()
driver.forward()
driver.refresh()
driver.title
driver.maximize_window()
driver.minimize_window()
driver.fullscreen_window()
driver.close()
driver.quit()
'''

from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.google.com")
print(driver.current_url)
driver.refresh()
print(driver.title)
driver.maximize_window()
time.sleep(4)
driver.minimize_window()
driver.fullscreen_window()
time.sleep(4)
driver.quit()
