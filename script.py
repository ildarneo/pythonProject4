from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def run_script():
    # Создаем объект настроек браузера
    options = Options()
    options.headless = True  # Запускать в фоновом режиме, без графического интерфейса

    # Создаем драйвер Chrome с помощью webdriver_manager
    driver = webdriver.Chrome(
        executable_path=ChromeDriverManager().install(),
        options=options
    )

    # Открываем сайт
    driver.get("https://skillbox.ru")
    print(driver.title)  # например, выводим название страницы

    # Закрываем браузер
    driver.quit()

if __name__ == "__main__":
    run_script()