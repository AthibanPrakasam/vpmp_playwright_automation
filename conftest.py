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

@pytest.fixture(scope="function")
def setup_browser():
    if TOOL == "playwright":
        with sync_playwright() as p:
            if BROWSER == "chrome":
                browser = p.chromium.launch(headless=False)
            elif BROWSER == "firefox":
                browser = p.firefox.launch(headless=False)
            elif BROWSER == "edge":
                browser = p.chromium.launch(channel="msedge", headless=False)
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
        else:
            raise ValueError(f"Unsupported browser: {BROWSER}")
        yield driver
        driver.quit()
    else:
        raise ValueError(f"Unsupported tool: {TOOL}")