from playwright.sync_api import sync_playwright

def test_first_file(page):
    page.goto("https://www.google.com")
    page.screenshot(path="screenshots/google_homepage.png")
    assert page.title() == "Google"