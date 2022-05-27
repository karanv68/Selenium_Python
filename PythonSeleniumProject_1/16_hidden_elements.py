from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class DemohiddenElementState():
    def locate_by_tag_demo(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.yatra.com/hotels")
        driver.find_element_by_xpath("//span[@class='txt-ellipses hotel_passengerBox travellerPaxBox']").click()
        time.sleep(2)
        driver.find_element_by_xpath("//body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/span[2]").click()
        time.sleep(2)
        state = driver.find_element_by_xpath("//select[@class='ageselect']").is_displayed()
        print(state)
        time.sleep(2)
        driver.find_element_by_xpath("//body[1]/div[2]/div[1]/section[1]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[2]/div[3]/div[1]/div[1]/span[1]").click()
        state2 = driver.find_element_by_xpath("//select[@class='ageselect']").is_displayed()
        print(state2)

        driver.quit()
        
        
findelements = DemohiddenElementState()
findelements.locate_by_tag_demo()

