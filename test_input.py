import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.devtools.v85.debugger import pause
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture()
def set_up_browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()

class TestInput:

    # def test_send_keys(self, set_up_browser):
    #     driver = set_up_browser
    #     driver.get("https://l6nm9r.csb.app/demo/InputTextDemo.html")
    #     print("Заголовок страницы: ", driver.title)
    #     driver.find_element(By.ID, 'username1').send_keys('basic text')
    #     pass
    def test_send_keys1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://www.python.org/")
        print("Заголовок страницы: ", driver.title)
        driver.find_element(By.ID, 'id-search-field').send_keys('basic text')

        search_button = driver.find_element(By.ID, 'submit')
        search_button.click()

        pass

    def test_send_keysсlear(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://www.python.org/")
        print("Заголовок страницы: ", driver.title)
        el = driver.find_element(By.ID, 'id-search-field')
        el.send_keys('basic text')
        pass
        el.clear()
        pass


    def test_send_copypaste2(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://www.python.org/")
        print("Заголовок страницы: ", driver.title)
        el = driver.find_element(By.ID, 'id-search-field')
        el.send_keys('basic text')
        action_chains = webdriver.ActionChains(driver)

        modifier = Keys.CONTROL

        # Выделяем весь текст
        action_chains.key_down(modifier).send_keys('a').key_up(modifier).perform()
        time.sleep(3)

        # Копируем
        action_chains.key_down(modifier).send_keys('c').key_up(modifier).perform()
        time.sleep(3)

        # Очистка поля
        el.clear()
        time.sleep(3)

        # Клик по полю, чтобы установить фокус
        el.click()
        time.sleep(1.5)

        # Вставляем (Cmd/Ctrl + V)

        action_chains.key_down(modifier).send_keys('v').key_up(modifier).perform()
        time.sleep(3)



