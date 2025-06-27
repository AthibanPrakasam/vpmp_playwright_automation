from config.settings import LOGIN_URL
from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "//input[@name='user_name']"
        self.password_input = "//input[@name='password']"
        self.login_btn = "//button[@type='submit']"
        self.logout_btn = "(//button[contains(@class,'border rounded-md flex justify-center items-center p-3 hover:text-primary text-lg bg-white')])[1]"

    def load(self):
        self.navigate(LOGIN_URL)

    def login(self, username, password):
        self.browser.fill(self.username_input, username)
        self.browser.fill(self.password_input, password)
        self.browser.click(self.login_btn)
     
    def logout(self):
        # Assuming there's a logout button with a specific selector
        self.browser.click(self.logout_btn)
    