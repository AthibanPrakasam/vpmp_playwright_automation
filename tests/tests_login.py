from pages.login_page import LoginPage



def test_valid_login(setup_browser):
    page = setup_browser
    login = LoginPage(page)
    login.load()
    login.login("admin", "admin@123")

    assert "Visteon" in login.browser.get_title()

def test_invalid_login(setup_browser):
    page = setup_browser
    login = LoginPage(page)
    login.load()
    login.login("invalid_user", "invalid_pass")

    error_message = login.browser.get_element_text("//div[@class='text-red-500 text-xs pt-1']")
    assert "Invalid Credentials" in error_message  # Assuming the page displays an error message for invalid login 
