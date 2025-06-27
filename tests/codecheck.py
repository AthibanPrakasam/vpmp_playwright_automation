import sys
import os
import time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import pytest
from config.settings import BASE_URL as url

#playwright modules
import playwright.sync_api as sync_playwright

#selenium modules

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def launchplaywrightbrowser():
    p = sync_playwright.sync_playwright().start()
    with p.chromium.launch(headless=True) as browser:
        #browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(5000)
        page.fill("//input[@name='user_name']", "admin")
        page.fill("//input[@name='password']", "admin@123")
        page.click("//button[@type='submit']")
        page.wait_for_load_state("networkidle")
        assert "Visteon" in page.title()
        print("Login successful, page title contains 'Visteon'")
        # Close the page and browser
        page.close()
        browser.close()

def launchseleniumbrowser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)  # Wait for elements to be available
    time.sleep(5)  # Adjust sleep time as necessary
    # Fill in the login form
    driver.find_element(By.NAME, "user_name").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("admin@123")
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    assert "Visteon" in driver.title
    print("Login successful, page title contains 'Visteon'")
    driver.quit()
    
#launchplaywrightbrowser()



launchseleniumbrowser()