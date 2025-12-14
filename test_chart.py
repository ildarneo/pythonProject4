import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def set_up_browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


class TestCharts:
    def test_tooltip(self, set_up_browser):
        # найти элемент сейф и в выпадающем меню сейф дважды кликнуть +
        driver = set_up_browser
        driver.get('https://38j5ts.csb.app/demo/TooltipDemo.html')
        button = driver.find_element(By.CSS_SELECTOR, "a.btn-answer#btn-answer-yes")
        button.click()
        time.sleep(10)
        el = driver.find_element(By.XPATH, "//span[@role='img' and @aria-label='save']")
        action_chains = webdriver.ActionChains(driver)
        action_chains.move_to_element(el).perform()
        driver.find_element(By.XPATH, '//span[contains(@class,"ant - btn - icon")]/parent::button').click()

        driver.find_element(By.XPATH, '//span[contains(@class,"plus")]/parent::button').click()
        driver.find_element(By.XPATH, '//span[contains(@class,"plus")]/parent::button').click()


        pass

    def test_canvas_pie(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://mo1n471m5j.csb.app/')
        button = driver.find_element(By.CSS_SELECTOR, "a.btn-answer#btn-answer-yes")
        button.click()

        action_chains = webdriver.ActionChains(driver)
        time.sleep(10)
        action_chains.move_to_element(
            driver.find_element(By.CSS_SELECTOR, '.highcharts-point,highcharts-color-2')).perform()
        action_chains.click_and_hold()
        action_chains.release()
        pass

    def test_url(self, set_up_browser):
        driver = set_up_browser
        driver.get('https://rz7b08.csb.app/demo/DataTableDemo.html')
        driver.find_element(By.CSS_SELECTOR, '[placeholder = "Keyword Search"]').send_keys("Egypt")
        driver.find_element(By.XPATH, '[placeholder = "Keyword Search"]').send_keys("Egypt")

        driver.find_element(By.XPATH, '//button/span/[contains(text(),"Name"').click()
        pass







        time.sleep(10)
