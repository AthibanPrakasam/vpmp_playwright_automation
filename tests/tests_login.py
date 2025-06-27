from pages.login_page import LoginPage
from utils.logger import get_logger
from config.settings import LOGIN_URL , TOOL

logger = get_logger(__name__)

def test_valid_login(setup_browser):
    page = setup_browser
    login = LoginPage(page)
    login.load()
    login.login("admin", "admin@123")

    if TOOL == "selenium":
        assert "Visteon" in page.title
    elif TOOL == "playwright":
        assert "Visteon" in page.title()

