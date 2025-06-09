from playwright.sync_api import sync_playwright

# Ожидаемый заголовок.
EXPECTED_TITLES = "Fast and reliable end-to-end testing for modern web apps | Playwright"

# Пути к неподдерживаемым браузерам. Я указал где у меня установлены, если не работает, то пропишите свои пути.
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
OPERA_PATH = r"C:\Program Files\Opera\opera.exe"

# Функции по запуску браузеров.
def run_test(playwright, browser_type: str):

    if browser_type == "msedge":
        browser = playwright.chromium.launch(executable_path=EDGE_PATH, headless=False)
    elif browser_type == "brave":
        browser = playwright.chromium.launch(executable_path=BRAVE_PATH, headless=False)
    elif browser_type == "opera":
        browser = playwright.chromium.launch(executable_path=OPERA_PATH, headless=False)
    else:
        browser_launcher = getattr(playwright, browser_type)
        browser = browser_launcher.launch(headless=False)

    # Смотрим заголовок.
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/")
    title = page.title()
    print(f"[{browser_type}] Фактический заголовок: {title}")

    try:
        assert title in EXPECTED_TITLES, f"[{browser_type}] Заголовок не совпадает: {title}"
        print(f"[{browser_type}] Тест пройден: заголовок совпадает.")
    except AssertionError as e:
        print(e)

    context.close()
    browser.close()


with sync_playwright() as playwright:
    for browser_type in ["chromium", "firefox", "webkit", "msedge", "brave", "opera"]:
        print(f"Запуск теста в браузере: {browser_type}")
        run_test(playwright, browser_type)
