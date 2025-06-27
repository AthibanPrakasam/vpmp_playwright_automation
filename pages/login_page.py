from config.settings import LOGIN_URL
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "//input[@name='user_name']"
        self.password_input = "//input[@name='password']"
        self.login_btn = "//button[@type='submit']"

    def load(self):
        self.navigate(LOGIN_URL)

    def login(self, username, password):
        self.browser.fill(self.username_input, username)
        self.browser.fill(self.password_input, password)
        self.browser.click(self.login_btn)
     

