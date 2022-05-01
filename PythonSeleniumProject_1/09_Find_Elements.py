from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemoFindElements():
    def locate_by_tag_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/")
        lista=driver.find_elements_by_tag_name("a")
        print(len(lista))
        for i in lista:
            print(i.text)
        time.sleep(5)
    
findelements = DemoFindElements()
findelements.locate_by_tag_demo()