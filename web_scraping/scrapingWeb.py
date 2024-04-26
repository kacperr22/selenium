from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import time
import pandas as pd
import os

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

website = 'https://www.adamchoi.co.uk/teamgoals/detailed'
path = (os.getcwd() + '\chromedriver.exe')
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

driver.get(website)

dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown_country = dropdown.options
countries = []
for country in dropdown_country:
    countries.append(country.text)

dropdown.select_by_visible_text('Spain')

time.sleep(10)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[contains(@data-btn-radio, 'TeamForOver2_5')]")))
over_2_5 = driver.find_element(By.XPATH, "//label[contains(@data-btn-radio, 'TeamForOver2_5')]")
over_2_5.click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//label[@analytics-event='All matches']")))
all_matches = driver.find_element(By.XPATH, "//label[@analytics-event='All matches']")
all_matches.click()
matches = driver.find_elements(By.TAG_NAME, 'tr')

date = []
home_team = []
away_team = []
score = []
for match in matches:
    date.append(match.find_element(By.XPATH, "./td[1]").text)
    home = match.find_element(By.XPATH, "./td[2]").text
    home_team.append(home)
    print(home)
    score.append(match.find_element(By.XPATH, "./td[3]").text)
    away_team.append(match.find_element(By.XPATH, "./td[4]").text)

df = pd.DataFrame({'date': date,
                    'home_team': home_team,
                    'score': score,
                    'away_team': away_team
              })
df.to_csv('Football_data.csv', index=False)
print(df)
time.sleep(500)
driver.quit()