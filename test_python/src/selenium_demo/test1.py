import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
driver = webdriver.Chrome()
driver.maximize_window()
# driver = webdriver.Chrome()
driver.get('https://ceshiren.com/')
time.sleep(1)
eles = driver.execute_script("return document.getElementsByClassName('ember-view')")
print(len(eles))
driver.execute_script("document.getElementsByClassName('ember-view')[0].removeAttribute('class')")
eles = driver.execute_script("return document.getElementsByClassName('ember-view')")
print(len(eles))
driver.execute_script("document.getElementsByClassName('ember-view')[0].setAttribute('class','wg')")
eles = driver.execute_script("return document.getElementsByClassName('wg')")
print(len(eles))
driver.execute_script("document.documentElement.scrollTop=1000")
time.sleep(3)
driver.quit()