from playwright.sync_api import Page, expect


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.upgrade_button = page.get_by_role("button", name="Upgrade")
        self.recruitment_link = page.get_by_role("link", name="Recruitment")
        self.performance_link = page.get_by_role("link", name="Performance")
        self.dashboard_link = page.get_by_role("link", name="Dashboard")
        self.recruitment_heading = page.get_by_role("heading", name="Recruitment")
        self.performance_heading = page.get_by_role("heading", name="Performance")
    
    def wait_for_dashboard_loaded(self):
        expect(self.dashboard_link).to_be_visible()

    def wait_for_recruitment_page_loaded(self):
        expect(self.recruitment_heading).to_be_visible()

    def wait_for_performance_page_loaded(self):
        expect(self.performance_heading).to_be_visible()
    
    def click_recruitment(self):
        self.recruitment_link.click()

    def click_performance(self):
        self.performance_link.click()

    def click_dashboard(self):
        self.dashboard_link.click()
