from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_driver_path = 'D:/python/driver/chromedriver.exe'
chrome_binary_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'

service = Service(executable_path=chrome_driver_path)
chrome_options = Options()
chrome_options.binary_location = chrome_binary_path

try:
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get('https://www.google.com')
    print("ChromeDriver started successfully.")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
