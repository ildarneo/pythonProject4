from selenium.webdriver import ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import chromedriver_binary
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome import Options as ChromeOptions

from selenium.webdriver import ChromeService
def run_script():
    options = ChromeOptions
    options.healess = True


# Устанавливаем драйвер и запускаем браузер
    driver = ChromeService(options=options)
# Открываем тестируемый сайт
    driver.get("https://skillbox.ru")
# Закрываем браузер
    driver.quit()
if __name__ == "__main__":
    run_script()