from lib2to3.pgen2 import driver
import unittest
import time
from pip import main
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains as AS

class Searching_the_web(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_search_on_google(self):
        driver = self.driver
        driver.get("https://www.google.com")
        self.assertIn("Google",driver.title)
        elem = driver.find_element_by_xpath("//input[@title='Search']")
        elem.send_keys("Gmail")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.",driver.page_source)
    
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
        