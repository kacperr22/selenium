import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

## https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.122/win64/chromedriver-win64.zip

service = Service(executable_path='chromedriver.exe')
driver = webdriver.Chrome(service=service)


driver.get('https://google.com')

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'L2AGLb')))

accept_cookie_file = driver.find_element(By.ID, 'L2AGLb')
accept_cookie_file.click()

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'gLFyf')))

input_text = driver.find_element(By.CLASS_NAME, 'gLFyf')

input_text.send_keys("big white dogs" + Keys.ENTER)

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'big white dogs')))

link = driver.find_element(By.PARTIAL_LINK_TEXT, 'Top 10 Big White Dog')
link.click()

time.sleep(1000)
driver.quit()