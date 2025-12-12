import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def set_up_browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


class TestClick:

    # def test_send_keys(self, set_up_browser):
    #     driver = set_up_browser
    #     driver.get("https://l6nm9r.csb.app/demo/InputTextDemo.html")
    #     print("Заголовок страницы: ", driver.title)
    #     driver.find_element(By.ID, 'username1').send_keys('basic text')
    #     pass
    def test_click(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://www.python.org/")
        #print("Заголовок страницы: ", driver.title)
        driver.find_element(By.XPATH, '//but4ton').click()
        pass
        time.sleep(5)
        pass
    def test_clickavia(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://www.aviasales.ru/search/KZN1501LED18011")
        #print("Заголовок страницы: ", driver.title)
        driver.find_element(By.XPATH, "//button[@data-test-id='profile-button']").click()
        pass
        time.sleep(5)
        driver.quit()
        pass

    def test_clickavia1(self, set_up_browser):
        #поиск элемента, ожидание и клик
        driver = set_up_browser
        driver.get("https://www.aviasales.ru/")
        #print("Заголовок страницы: ", driver.title)
        profile_button = WebDriverWait(driver, 4).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test-id='profile-button']"))
        )
        profile_button.click()

        time.sleep(5)
        driver.quit()
        pass

    def testdoubleclick_google(self, set_up_browser):
        #двойной клик
        driver = set_up_browser
        driver.get("https://www.google.com/")
        print("Заголовок страницы: ", driver.title)
        assert "Google" == driver.title
        action_chains = webdriver.ActionChains(driver)
        action_chains.double_click(driver.find_element(By.XPATH, "//a[contains(@aria-label, 'Войти')]")).perform()
        time.sleep(2)
        driver.quit()
