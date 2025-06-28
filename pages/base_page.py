from config.settings import TOOL
from utils.browser_adapter import BrowserAdapter


class BasePage:
    def __init__(self, page):
        self.browser = BrowserAdapter(TOOL, page)

    def navigate(self, url):
        self.browser.navigate(url)

    def wait_for_element(self, selector):
        """Wait for an element to be present in the DOM."""
        self.browser.page.wait_for_selector(selector)
    