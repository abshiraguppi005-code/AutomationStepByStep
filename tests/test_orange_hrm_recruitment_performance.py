from playwright.sync_api import Page

from pageObject.orangehrm_home_page import HomePage
from pageObject.orangehrm_login_page import LoginPage


def test_orange_hrm_recruitment_performance(page: Page) -> None:
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    page.wait_for_url("**/dashboard/index", timeout=90000)
    home_page.wait_for_dashboard_loaded()

    home_page.click_recruitment()
    page.wait_for_url("**/recruitment/viewCandidates", timeout=90000)
    home_page.wait_for_recruitment_page_loaded()

    home_page.click_performance()
    page.wait_for_url("**/performance/searchEvaluatePerformanceReview", timeout=90000)
    home_page.wait_for_performance_page_loaded()
