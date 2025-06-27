import pytest
from config.settings import TOOL, BROWSER

# Playwright imports
from playwright.sync_api import sync_playwright

# Selenium imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

TOOL = TOOL.lower()  # Ensure TOOL is in lowercase for consistency
BROWSER = BROWSER.lower()  # Ensure BROWSER is in lowercase for consistency

@pytest.fixture(scope="session")
def setup_browser():
    if TOOL == "playwright":
        with sync_playwright() as p:
            
            if BROWSER == "chrome":
                browser = p.chromium.launch(headless=False, slow_mo=200)
            elif BROWSER == "firefox":
                browser = p.firefox.launch(headless=False, slow_mo=200)
            elif BROWSER == "safari":
                browser = p.webkit.launch(headless=False, slow_mo=200)  # Safari is supported via WebKit    
            elif BROWSER == "edge":
                browser = p.chromium.launch(channel="msedge", headless=False, slow_mo=200)
            else:
                raise ValueError(f"Unsupported browser: {BROWSER}")
            page = browser.new_page()
            yield page
            browser.close()
    elif TOOL == "selenium":
        if BROWSER == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif BROWSER == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        elif BROWSER == "edge":
            driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        elif BROWSER == "safari":
            driver = webdriver.Safari()  # Safari WebDriver must be enabled in macOS    
        else:
            raise ValueError(f"Unsupported browser: {BROWSER}")
        yield driver
        driver.quit()
    else:
        raise ValueError(f"Unsupported tool: {TOOL}")