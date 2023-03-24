import time
import re
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup
 



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

driver.get('https://www.facebook.com/shahbazabbasi00/')

time.sleep(10)
#class="x78zum5 x1n2onr6 xh8yej3"class="x1ey2m1c xds687c x5yr21d x10l6tqk x17qophe x13vifvy xh8yej3 xl1xv1r"
while True:
    soup=BeautifulSoup(driver.page_source,"html.parser")
    all_posts=soup.find_all("div",{"class":"x78zum5 x1n2onr6 xh8yej3"})
    for post in all_posts:
        try:
            name=post.find("img",{"class":"x1ey2m1c xds687c x5yr21d x10l6tqk x17qophe x13vifvy xh8yej3 xl1xv1r"}).img.get('src')
        except:
            name="not found"
        print(name)



# pic=driver.find_elements(By.XPATH,'//div[@class="x10l6tqk x13vifvy"]')
# pic.click()
# page_source=driver.page_source
# print(page_source)
