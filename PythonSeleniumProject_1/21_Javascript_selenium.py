from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.get("https://training.rcvacademy.com/")
driver.execute_script("window.open('https://training.rcvacademy.com/','_self');")
time.sleep(3)
demo_element = driver.execute_script("return document.getElementsByTagName('p')[1];")
driver.execute_script("arguments[0].click();",demo_element)
time.sleep(3)

driver.quit()

