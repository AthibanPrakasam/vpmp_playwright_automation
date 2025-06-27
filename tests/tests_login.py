from pages.login_page import LoginPage



def test_valid_login(setup_browser):
    page = setup_browser
    login = LoginPage(page)
    login.load()
    login.login("admin", "admin@123")

    assert "Visteon" in login.browser.get_title()

