from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    # creating and returning a configured chrome webdriver instance.
    # centralizing this means every test starts the browser the same way.

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)  # ✅ pass the instance, not the class

    driver.maximize_window()
    # Implicit wait: for up to 10s, Selenium will keep retrying to find
    # an element before throwing a NoSuchElementException. This helps
    # absorb small page-load delays without hardcoding time.sleep().
    driver.implicitly_wait(10)

    return driver
