from playwright.sync_api import sync_playwright
 
def before_scenario(context, scenario):
    print("Scenario Started")
    context.playwright=sync_playwright().start()
    context.browser=context.playwright.chromium.launch(
        headless=False
    )
    context.page=context.browser.new_page()
 
 
def after_scenario(context, scenario):
    print("Scenario Ended")
    if hasattr(context, "browser"):
        context.browser.close()
 
    if hasattr(context, "playwright"):
        context.playwright.stop()