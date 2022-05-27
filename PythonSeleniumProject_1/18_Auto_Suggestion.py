from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.yatra.com/flights")
depart_from = driver.find_element_by_id("BE_flight_origin_city")
depart_from.click()
time.sleep(3)

depart_from.send_keys("New Delhi")
depart_from.send_keys(Keys.ENTER)
time.sleep(3)

going_to = driver.find_element_by_xpath("//input[@id='BE_flight_arrival_city']")
going_to.send_keys("New")
time.sleep(3)
search_results = driver.find_elements(By.XPATH, "//div[@class='viewport']//div[1]/li")
print(len(search_results))

for results in search_results:
    print(results.text)
    if "New York (jfk)" in results.text:
        results.click()
        time.sleep(3)
        break


driver.quit()

