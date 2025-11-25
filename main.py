import requests
response = requests.get("https://httpbin.org/get")
if response.status_code == 200:
    print("Библиотека requests работает корректно!")
    print("Ответ сервера (JSON):", response.json())
else:
    print("Ошибка:", response.status_code)

if response.status_code == 200:
    print("Библиотека requests работает корректно!")
    print("Ответ сервера (JSON):", response.json())
else:
    print("Ошибка:", response.status_code)

from selenium.webdriver import Chrome
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
def run_script():
# Устанавливаем драйвер и запускаем браузер
    driver = Chrome(service=ChromeService(ChromeDriverManager().install()))
# Открываем тестируемый сайт
    driver.get("https://skillbox.ru")
# Закрываем браузер
    driver.quit()
if __name__ == "__main__":
    run_script()
