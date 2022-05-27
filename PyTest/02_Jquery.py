from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time 

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.jqueryscript.net/demo/Drop-Down-Combo-Tree/")

driver.find_element(By.ID,"justAnInputBox").click()

drop_list = driver.find_elements(By.CSS_SELECTOR,'span.comboTreeItemTitle')

for ele in drop_list:
    print(ele.text)
    if ele.text == 'choice 2':
        ele.click()
        break

