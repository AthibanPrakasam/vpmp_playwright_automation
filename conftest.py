import pytest
from config.settings import TOOL

#playwright
from playwright.sync_api import sync_playwright

#selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

TOOL = TOOL.lower()  # Ensure TOOL is in lowercase for consistency
@pytest.fixture(scope="function")
def setup_browser():
    if TOOL == "playwright":        
       with sync_playwright() as p:
          browser = p.chromium.launch(headless=False)
          page = browser.new_page()
          yield page
          browser.close()
    elif TOOL == "selenium":
          driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
          yield driver
          driver.quit()
    else:
          raise ValueError(f"Unsupported tool: {TOOL}")
    # No setup needed for requests, as it doesn't require a browser context
    # Note: The yield statement allows the test to run with the browser context
    # and then closes the browser after the test completes.
    # For requests, you would typically return a session object or similar.
    # if TOOL == "requests":
    #     import requests
    #     session = requests.Session()
    #     yield session
    #     session.close()
    # else:
    #     raise ValueError(f"Unsupported tool: {TOOL}") 


