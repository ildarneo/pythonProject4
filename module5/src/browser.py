import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

path_to_driver = 'C:/Chromedriver/chromedriver.exe'  # это пример пути как нужно указать а так driver нужно скачать от сюда https://googlechromelabs.github.io/chrome-for-testing/ и тут указать путь до него


@pytest.fixture()
def set_up_browser():
    options = Options()
    options.page_load_strategy = 'normal'
    # Создаем драйвер локально с помощью webdriver_manager
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    driver.implicitly_wait(30)
    yield driver
    driver.quit()
