# from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
ser = Service(r"C:/Users/vhmir/PycharmProjects/pythonProject/Business Analytics/chromedriver.exe")
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

# driver = webdriver.Chrome('C:/Users/vhmir/PycharmProjects/pythonProject/Business Analytics/chromedriver.exe')

driver.get("https://www.python.org")
print(driver.title)
search_bar = driver.find_element("q")
search_bar.clear()
search_bar.send_keys("getting started with python")
search_bar.send_keys(Keys.RETURN)
print(driver.current_url)
driver.close()
