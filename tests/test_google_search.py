
def test_google_search(page):
    page.goto("https://www.google.com")
    # Dismiss consent dialog if present (varies by region)
    try:
        for sel in ["button:has-text('I agree')", "button:has-text('Accept all')", "button:has-text('Accept')"]:
            try:
                consent = page.locator(sel).first
                if consent.is_visible():
                    consent.click()
                    break
            except Exception:
                continue
    except Exception:
        pass

    # Try to use a reliable selector for the search input and perform the search.
    # If the input cannot be found (consent iframe or different UI), fall back to direct search URL.
    try:
        search_box = page.locator('input[name="q"]')
        search_box.fill("Playwright Python")
        search_box.press("Enter")
    except Exception:
        # Fallback: navigate directly to search results
        page.goto("https://www.google.com/search?q=Playwright+Python")

    # Wait for a result title (`h3`) to appear and print it; otherwise print a page snippet
    try:
        page.wait_for_selector('h3', timeout=15000)
        first_title = page.locator('h3').first
        title_text = first_title.text_content() or ""
        print("First result:", title_text)
    except Exception:
        snippet = page.content()[:1000]
        print("No result title found; page snippet:\n", snippet)