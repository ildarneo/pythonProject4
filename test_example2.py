import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

@pytest.fixture()
def set_up_browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()




class TestExample:

    def test_find_element(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://the-internet.herokuapp.com/login")
        elem_name = driver.find_element(By.ID, 'username')
        elem_class = driver.find_element(By.CLASS_NAME, 'subheader')
        elem_xpath = driver.find_element(By.XPATH, '//form/descendant::input[@id="password"]')
        elem_css =driver.find_element(By.CSS_SELECTOR, 'form input#password')
        elem_css = driver.find_element(By.TAG_NAME, 'input')
        elem_part = driver.find_elements(By.PARTIAL_LINK_TEXT, "Auth")

        def test_find_element1(self, set_up_browser):
            driver = set_up_browser
            driver.get("https://the-internet.herokuapp.com/login")


            elem_css = driver.find_element(By.TAG_NAME, 'input')

        pass
