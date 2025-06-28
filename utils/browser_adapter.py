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
        
    def wait_for_element(self, selector, timeout=10):
        if self.tool == "selenium":
            return WebDriverWait(self.page, timeout).until(EC.presence_of_element_located((By.XPATH, selector)))
        elif self.tool == "playwright":
            self.page.wait_for_selector(selector, timeout=timeout * 1000)
        else:
            raise ValueError(f"Unsupported tool: {self.tool}")
        
    def is_element_visible(self, selector):
        try:
            if self.tool == "selenium":
                return self.page.find_element(By.XPATH, selector).is_displayed()
            elif self.tool == "playwright":
                return self.page.is_visible(selector)
        except Exception:
            return False
        
    def get_attribute(self, selector, attr_name):
        if self.tool == "selenium":
            return self.page.find_element(By.XPATH, selector).get_attribute(attr_name)
        elif self.tool == "playwright":
            return self.page.get_attribute(selector, attr_name)
        else:
            raise ValueError(f"Unsupported tool: {self.tool}")
        
    def screenshot(self, path="screenshot.png"):
        if self.tool == "selenium":
            self.page.save_screenshot(path)
        elif self.tool == "playwright":
            self.page.screenshot(path=path)

    def press_key(self, selector, key):
        if self.tool == "selenium":
            elem = self.page.find_element(By.XPATH, selector)
            elem.send_keys(key)
        elif self.tool == "playwright":
            self.page.locator(selector).press(key)




