# https://selenium-python.readthedocs.io/locating-elements.html 

'''
There are various strategies to locate elements in a page. You can use the most appropriate one for your case. Selenium provides the following methods to locate elements in a page:

find_element_by_id
find_element_by_name
find_element_by_xpath
find_element_by_link_text
find_element_by_partial_link_text
find_element_by_tag_name
find_element_by_class_name
find_element_by_css_selector
To find multiple elements (these methods will return a list):

find_elements_by_name
find_elements_by_xpath
find_elements_by_link_text
find_elements_by_partial_link_text
find_elements_by_tag_name
find_elements_by_class_name
find_elements_by_css_selector
Apart from the public methods given above, there are two private methods which might be useful for locating page elements:

find_element
find_elements
'''

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemoFindElementByID():
    def locate_by_id_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_id('login-input').send_keys('test@test.com')
        time.sleep(4)

    def locate_by_name_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://secure.yatra.com/social/common/yatra/signin.htm")
        driver.find_element_by_name('login-input').send_keys('test@test.com')
        time.sleep(4)


findbyid = DemoFindElementByID()
findbyid.locate_by_id_demo()
#findbyid.locate_by_name_demo()

