from config.settings import LOGIN_URL , TOOL
from pages.base_page import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

TOOL = TOOL.lower()  # Ensure TOOL is in lowercase for consistency

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.username_input = "//input[@name='user_name']"
        self.password_input = "//input[@name='password']"
        self.login_btn = "//button[@type='submit']"

    def load(self):
        self.navigate(LOGIN_URL)

    def login(self, username, password):

        if TOOL == "selenium":
            # For Selenium, we use find_element and send_keys
            WebDriverWait(self.page, 10).until(EC.presence_of_element_located((By.XPATH, self.username_input)))
            self.page.find_element(By.XPATH, self.username_input).send_keys(username)
            self.page.find_element(By.XPATH, self.password_input).send_keys(password)
            self.page.find_element(By.XPATH, self.login_btn).click()
        elif TOOL == "playwright":
            # For Playwright, we use fill and click methods
            self.page.fill(self.username_input, username)
            self.page.fill(self.password_input, password)
            self.page.click(self.login_btn)
     

