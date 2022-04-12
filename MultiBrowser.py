from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
print('Sample test case started')
driver = webdriver.Chrome(executable_path="C:\\Users\\prathima\\Downloads\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.google.com/")
driver.find_element_by_name("q").send_keys("javapoint")
time.sleep(3)
driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
time.sleep(3)
print(driver.title)
print(driver.current_url)
driver.close()
print('Sample test case successfully completed')