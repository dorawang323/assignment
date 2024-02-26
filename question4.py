import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from PIL import Image

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.twse.com.tw/zh/index.html')
driver.set_window_size(1440, 768)

driver.find_element(By.XPATH, '//*[@id="mega"]/ul/li[2]/a').click()
driver.find_element(By.XPATH, '//*[@id="mega"]/ul/li[2]/div/div/ul[1]/li[10]/a').click()
driver.find_element(By.XPATH, '//*[@id="label0"]').click()

select = Select(driver.find_element(By.XPATH,'//select[@name="yy"]'))
select.select_by_value('2023')

driver.find_element(By.XPATH, '//*[@id="form"]/div/div[1]/div[1]/label').click()

select = Select(driver.find_element(By.XPATH,'//select[@name="mm"]'))
select.select_by_value('1')

driver.find_element(By.XPATH, '//*[@id="label1"]').send_keys('2330')
driver.find_element(By.XPATH, '//*[@id="form"]/div/div[1]/div[3]/button').click()

driver.get_screenshot_as_file('page.png')



time.sleep(3)
driver.close()
