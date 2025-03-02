from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyttsx3
import re

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
        service = Service(executable_path='D:/python/driver/chromedriver.exe')
        driver = webdriver.Chrome(service=service)

        try:
            # Open Google
            driver.get('https://www.google.com')

            # Find the search box using By.NAME
            search_box = driver.find_element(By.NAME, 'q')
            search_box.send_keys(search_for)
            search_box.send_keys(Keys.RETURN)
        except Exception as e:
            speak(f"An error occurred: {e}")
        finally:
            # Optional: close the driver after a delay or when done
            driver.quit()

