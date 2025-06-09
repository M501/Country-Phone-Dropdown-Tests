from playwright.sync_api import sync_playwright

# Ожидаемый заголовок.
EXPECTED_TITLES = "Fast and reliable end-to-end testing for modern web apps | Playwright",

# Пути к неподдерживаемым браузерам.
EDGE_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
BRAVE_PATH = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"
OPERA_PATH = r"C:\Program Files\Opera\opera.exe"
YANDEX_PATH = r"C:\Users\M25\AppData\Local\Yandex\YandexBrowser\Application\browser.exe"


# Функции по запуску браузеров.
def run_test(playwright, browser_type: str):
    if browser_type == "msedge":
        browser = playwright.chromium.launch(executable_path=EDGE_PATH, headless=False)
    elif browser_type == "brave":
        browser = playwright.chromium.launch(executable_path=BRAVE_PATH, headless=False)
    elif browser_type == "opera":
        browser = playwright.chromium.launch(executable_path=OPERA_PATH, headless=False)
    elif browser_type == "yandex":
        browser = playwright.chromium.launch(executable_path=YANDEX_PATH, headless=False)
    else:
        browser_launcher = getattr(playwright, browser_type)
        browser = browser_launcher.launch(headless=False)

    # Смотрим заголовок.
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/")

    # Ждем, пока страница полностью загрузится
    page.wait_for_load_state("load")

    title = page.title()
    print(f"[{browser_type}] Фактический заголовок: {title}")

    try:
        assert any(expected_title in title for expected_title in
                   EXPECTED_TITLES), f"[{browser_type}] Заголовок не совпадает: {title}"
        print(f"[{browser_type}] Тест пройден: заголовок совпадает.")
        return True
    except AssertionError as e:
        print(e)
        return False
    finally:
        context.close()
        browser.close()


with sync_playwright() as playwright:
    total_tests = 0
    passed_tests = 0
    failed_tests = 0

    for browser_type in ["chromium", "firefox", "webkit", "msedge", "brave", "opera", "yandex"]:
        print(f"Запуск теста в браузере: {browser_type}")
        total_tests += 1
        if run_test(playwright, browser_type):
            passed_tests += 1
        else:
            failed_tests += 1

    # Вывод результатов тестирования
    print("\nРезультаты тестирования:")
    print(f"Всего тестов: {total_tests}")
    print(f"Успешно пройдено: {passed_tests}")
    print(f"Не пройдено: {failed_tests}")
