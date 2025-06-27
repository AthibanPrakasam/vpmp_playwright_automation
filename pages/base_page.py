from config.settings import TOOL
from utils.browser_adapter import BrowserAdapter

class BasePage:
    def __init__(self, page):
        self.browser = BrowserAdapter(TOOL, page)

    def navigate(self, url):
        self.browser.navigate(url)

    def wait_for_element(self, selector):
        # This method can be implemented using BrowserAdapter if needed
        pass
