from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import os


driver = webdriver.Chrome()
driver.get("https://www.serebii.net/attackdex-rby/")
ac=ActionChains(driver)
#There are no ID or specifing name attributes for these dropdowns so you have to
#find the location and move there manually
dropdowns = driver.find_elements(By.TAG_NAME, "select")
x_val=dropdowns[0].location['x']
y_val=dropdowns[0].location['y']

ac.move_to_element(dropdowns[0])
ac.click()
ac.perform()

select = Select(dropdowns[0])
options = select.options
os.open()
for index in range(1,len(options) - 1):
    select.select_by_index(index)
    link = driver.current_url
    driver.navigate().back()