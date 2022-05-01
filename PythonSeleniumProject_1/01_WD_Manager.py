from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Here we don't need to give the path of chrome extension it will get downloaded automatically.

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://www.gmail.com")
driver.maximize_window
print(driver.title)
driver.close()