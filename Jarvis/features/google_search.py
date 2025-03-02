from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyttsx3
import re
import time

def speak(text):
    """
    Use text-to-speech to say the provided text.
    """
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(text)
    engine.runAndWait()
    engine.setProperty('rate', 180)

def google_search(command):
    """
    Perform a Google search based on the command provided.
    """
    reg_ex = re.search(r'search google for (.*)', command)
    if reg_ex:
        search_for = reg_ex.group(1)
        speak("Okay sir!")
        speak(f"Searching for {search_for}")

        # Initialize the Chrome WebDriver
        chrome_driver_path = 'D:/python/driver/chromedriver.exe'  # Path to ChromeDriver
        chrome_binary_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe'  # Path to Chrome executable

        service = Service(executable_path=chrome_driver_path)
        
        # Create Chrome options object
        chrome_options = Options()
        chrome_options.binary_location = chrome_binary_path

        driver = None
        try:
            driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # Open Google
            driver.get('https://www.google.com')
            

            # Find the search box using By.NAME
            search_box = driver.find_element(By.NAME, 'q')
            search_box.send_keys(search_for)
            search_box.send_keys(Keys.RETURN)
            
            # Optional: wait for a few seconds to allow the search results to load
            time.sleep(5)
            
            # Optional: read the title of the search results page
            title = driver.title
            speak(f"The page title is {title}")

        except Exception as e:
            print(f"An error occurred: {e}")

        finally:
            # Make sure to quit the driver even if an error occurred
            if driver:
                driver.quit()
#google_search("search google for peter tarot")




