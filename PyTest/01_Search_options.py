from select import select
from tkinter.tix import Select
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def select_values(element,value):
    select = Select(element)
    select.select_by_visible_text(value)

def select_values_without_select(dropdownlist,value):
    print(len(dropdownlist))
    for ele in dropdownlist:
        print(ele.text)
        if ele.text == value:
            ele.click()
            break

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.get("https://www.orangehrm.com/orangehrm-30-day-trial/")
ele_indus = driver.find_element(By.ID,"Form_submitForm_Country")
select = Select(ele_indus)
#select.select_by_visible_text("India")
#select.select_by_index(10)
#select.select_by_value("India")
select_values(ele_indus,'India')
ele_list = select.options

#for element in ele_list:
#   print(element.text)
#   if element.text == 'India':
#       element.click()
#       break

#indus_options = driver.find_elements(By.XPATH,"//select[@id='Form_submitForm_Country']/option")
#print(len(indus_options))
#for ele in indus_options:
#    print(ele.text)
#    if ele.text == 'Austria':
#        ele.click()
#        break

indus_options = indus_options = driver.find_elements(By.XPATH,"//select[@id='Form_submitForm_Country']/option")
select_values_without_select(indus_options,'Austria')
    

driver.close()


