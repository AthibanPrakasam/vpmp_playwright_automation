from pages.login_page import LoginPage
from utils.logger import get_logger

logger = get_logger(__name__)

def test_valid_login(setup_browser):
    page = setup_browser
    login = LoginPage(page)
    logger.info("Starting valid login test")
    login.load()
    login.login("admin", "admin@123")
    logger.info("Login form filled and submitted")
    # Wait for the page to load after login
    page.wait_for_load_state("networkidle")
    logger.info("Waiting for the page to load after login")
    # Assert that the login was successful by checking the title or URL
    assert "Visteon" in page.title()
