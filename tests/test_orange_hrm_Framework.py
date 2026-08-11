import re
from playwright.sync_api import Page, expect
from pageObject.orangehrm_login_page import LoginPage
from pageObject.orangehrm_home_page import HomePage


def test_orange_hrm(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(page)
    home_page = HomePage(page)

    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    expect(home_page.upgrade_button).to_be_visible()

    home_page.click_recruitment()
    home_page.click_performance()