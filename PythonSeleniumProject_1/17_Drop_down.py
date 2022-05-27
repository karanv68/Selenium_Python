from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.select import Select


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://www.salesforce.com/in/form/signup/freetrial-sales/?d=topnav2-btn-ft")
dropdown = driver.find_element_by_name("UserTitle")
dd = Select(dropdown)

dd.select_by_index(1)
time.sleep(3)
dd.select_by_visible_text("Marketing / PR Manager")
time.sleep(3)
dd.select_by_value("Customer_Service_Manager_AP")
time.sleep(3)

driver.quit()
