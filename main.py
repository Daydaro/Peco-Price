from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from notify_run import Notify
import time

PATH = "D:\Python\chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://www.peco-online.ro/index.php")
location = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='nume_locatie']")))

location.clear()
location.send_keys("Bucuresti")

button = WebDriverWait(driver, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

notify = Notify()
notify.send("test message")

#driver.close()


