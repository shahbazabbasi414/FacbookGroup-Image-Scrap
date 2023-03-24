import time
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




# chrome_options = webdriver.ChromeOptions()
# prefs = {"profile.default_content_setting_values.notifications" : 2}
# chrome_options.add_experimental_option("prefs",prefs)
# driver = webdriver.Chrome(chrome_options=chrome_options)

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.facebook.com/')
driver.maximize_window()

usr = "shahbazabbasi414@gmail.com"
pwd = "Nib@2233"


user_name=driver.find_element(By.XPATH,'//input[@type="text"]')
user_name.send_keys(usr)


password=driver.find_element(By.XPATH,'//input[@class="inputtext _55r1 _6luy _9npi"]')
password.send_keys(pwd)


login=driver.find_element(By.XPATH,'//button[@class="_42ft _4jy0 _6lth _4jy6 _4jy1 selected _51sy"]')
login.click()
time.sleep(10)

driver.get('https://www.facebook.com/zuck/photos')

time.sleep(10)

pic=driver.find_element(By.XPATH,'//div/div[@class="xqtp20y x1n2onr6 xh8yej3"]')
pic.click()
page_source=driver.page_source
print(page_source)
