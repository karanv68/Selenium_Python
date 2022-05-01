# This script will help you understanding webdriver with selenium by installing the extensions

# Link :https://www.selenium.dev/selenium/docs/api/py/index.html

# 1. First we need to import the webdriver from the selenium package

from selenium import webdriver  # \note we could import whole selenium library but it will consume our memory.

driver = webdriver.Chrome(executable_path="c:/Program Files/Scripts/chromedriver.exe")

driver.get("https://www.google.com")  #.get will open the URL
driver.maximize_window()   # It will maximize the window
print(driver.title)   # It will print the title of the web page
driver.close()  # it will close the browser


