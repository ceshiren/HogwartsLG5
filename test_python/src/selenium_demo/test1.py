from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = webdriver.ChromeOptions()
options.binary_location = "D:\chrome\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome()

# driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
