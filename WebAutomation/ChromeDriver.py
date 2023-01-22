from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('C:/Users/vhmir/PycharmProjects/pythonProject/WebAutomation/chromedriver.exe')
driver.get("https://www.python.org")
print(driver.title)
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
<<<<<<< HEAD
driver.close()
=======
driver.close()
>>>>>>> origin/master
