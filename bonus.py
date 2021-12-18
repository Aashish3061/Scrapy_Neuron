#This is the code for the bonus task. It handles the automatic form filling but lacks in handling the reCaptcha part. It is yet to be completed but I am submitting it nonetheless.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

from bs4 import BeautifulSoup

from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1100,1000")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

s = Service(r"C:\Users\aasis\Downloads\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(options=options, service=s)
driver.get("https://safebrowsing.google.com/safebrowsing/report_phish/Captcha")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.53 Safari/537.36'})
time.sleep(1)

driver.find_element_by_xpath('/html/body/div/form/fieldset/div[1]/input[5]').send_keys("https://safebrowsing.google.com/safebrowsing/report_phish/Captcha")
#driver.find_element_by_xpath('/html/body/div/form/fieldset/div[2]').click()
driver.find_element_by_xpath('/html/body/div/form/fieldset/div[4]/input').click()
#WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/form/fieldset/div[2]"))).click()
