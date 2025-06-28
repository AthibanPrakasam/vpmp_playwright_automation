from pages.login_page import LoginPage


class Sequencepage(LoginPage):
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.select_plant = "//div[contains(@class,'text-xl font-semibold')]"
        self.dashboardtxt = "//div[contains(text(),'Dashboard')]"
        self.sequence_management = "//div[contains(@class,'font-medium')][normalize-space()='Sequences']"
        self.sequencetxt = "//div[@class=' font-semibold']"

    def portallogin(self):
         login = LoginPage(self.page)
         login.load()
         login.login("admin", "admin@123")

    def gotoseqmanagement(self):
        self.browser.wait_for_element(self.select_plant)
        self.browser.click(self.select_plant)
        self.browser.wait_for_element(self.dashboardtxt)
        self.browser.wait_for_element(self.sequence_management) 
        self.browser.click(self.sequence_management)
        assert "Sequences" in self.browser.get_element_text(self.sequencetxt), "Sequences text not found"

