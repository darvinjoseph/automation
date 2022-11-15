from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains

#chrome driver
from selenium.webdriver.chrome.service import Service
#-- Chrome
from selenium.webdriver.common.by import By

service_obj = Service("E:/User2/Python-Automation/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(2)

driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("I am able to automate frames")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)












