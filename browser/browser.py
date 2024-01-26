#import undetected_chromedriver.v2 as uc
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
import time, os
#from pyvirtualdisplay import Display 

def create_browser(proxy, user_agent):
    #display = Display(visible=1, size=(1920, 1080), backend="xvfb")
    #display.start()
    prefs = {
        "profile.default_content_setting_values.geolocation": 1,
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_experimental_option("useAutomationExtension", False)
    options.add_argument(f"--user_agent={user_agent}")
    options.add_argument(f'--proxy-server={proxy}')
    service = Service(f"./chromedriver" )
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=service, options=options)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})") 
    return driver

def main():
    driver = create_browser("http://38.154.227.167:5868", "None")
    driver.get("https://instagram.com/")
    time.sleep(1100)
    
if __name__ == "__main__":
    main()