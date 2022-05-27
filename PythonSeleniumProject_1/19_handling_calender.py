from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.yatra.com/flights")
origin = driver.find_element_by_xpath("//input[@id='BE_flight_origin_date']")
origin.click()

time.sleep(3)
#driver.find_element_by_id("15/06/2022").click()
#time.sleep(2)

dates = driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
for date in dates:
    if date.get_attribute("data-date") == "30/05/2023":
        date.click()
        time.sleep(3)
        break


 