from config.settings import TOOL

class BasePage:
    def __init__(self, page):
        self.page = page

    def navigate(self, url):
        if TOOL == "selenium":
            # For Selenium, we use get method
            self.page.get(url)
        elif TOOL == "playwright":
            # For Playwright, we use goto method
            self.page.goto(url)
        elif TOOL == "requests":
            # For Requests, we don't navigate in the same way
            raise NotImplementedError("Requests does not support navigation like a browser.")
        else:
            raise ValueError(f"Unsupported tool: {TOOL}")
        
    def wait_for_element(self, selector):
        self.page.wait_for_selector(selector)
