from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from playwright.sync_api import Page as PlaywrightPage

class BrowserAdapter:
    def __init__(self, tool, page):
        self.tool = tool.lower()
        self.page = page

    def navigate(self, url):
        if self.tool == "selenium":
            self.page.get(url)
        elif self.tool == "playwright":
            self.page.goto(url)
        else:
            raise ValueError(f"Unsupported tool: {self.tool}")

    def fill(self, selector, value):
        if self.tool == "selenium":
            WebDriverWait(self.page, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
            self.page.find_element(By.XPATH, selector).send_keys(value)
        elif self.tool == "playwright":
            self.page.fill(selector, value)
        else:
            raise ValueError(f"Unsupported tool: {self.tool}")

    def click(self, selector):
        if self.tool == "selenium":
            WebDriverWait(self.page, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
            self.page.find_element(By.XPATH, selector).click()
        elif self.tool == "playwright":
            self.page.click(selector)
        else:
            raise ValueError(f"Unsupported tool: {self.tool}")

    def get_title(self):
        if self.tool == "selenium":
            return self.page.title
        elif self.tool == "playwright":
            return self.page.title()
        else:
            raise ValueError(f"Unsupported tool: {self.tool}")
    def get_element_text(self, selector):
        if self.tool == "selenium":
            WebDriverWait(self.page, 10).until(EC.presence_of_element_located((By.XPATH, selector)))
            return self.page.find_element(By.XPATH, selector).text
        elif self.tool == "playwright":
            return self.page.locator(selector).inner_text()
        else:
            raise ValueError(f"Unsupported tool: {self.tool}")