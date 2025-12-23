import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def set_up_browser():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    yield driver
    driver.quit()


class TestPraktik5:

    def test_case1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/issues")
        search_input = driver.find_element(By.CSS_SELECTOR, "input[name='repository-inputname']")
        search_input.send_keys(Keys.CONTROL + "a")
        search_input.send_keys(Keys.DELETE)
        search_input.send_keys("in:title bug")

        time.sleep(1)
        search_input.send_keys(Keys.ENTER)
        time.sleep(5)
        element = driver.find_element(By.XPATH, '//a[@href="/microsoft/vscode/issues/284816"]')

        # Получить текст элемента
        text = element.text

        # Проверка через assert
        assert 'bug' in text
        print("Проверка прошла успешно: в тексте есть слово 'bug'.")

        driver.quit()
        pass

    def test_case2(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/issues")
        driver.maximize_window()

        driver.find_element(By.XPATH, "//span[text()='Author']").click()
        search_input = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Filter authors']")
        search_input.clear()
        search_input.send_keys("bpasero")
        search_input.click()
        time.sleep(3)

        # Получаем значение поля поиска
        author_filter_value = search_input.get_attribute('value')
        assert 'bpasero' in author_filter_value
        if 'bpasero1' in author_filter_value:
            print('найдены совпадения с автором bpasero ')


        time.sleep(3)
        driver.quit()

    def test_case3(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/search/advanced")
        driver.find_element(By.ID, "search_language").click()
        time.sleep(1)
        select_element = driver.find_element(By.ID, "search_user_language")

        select = Select(select_element)

        # Выбрать опцию по значени
        select.select_by_value("Python")
        time.sleep(1)

        driver.find_element(By.ID, "search_stars").send_keys(">20000")
        time.sleep(1)

        driver.find_element(By.ID, "search_filename").send_keys("environment.yml")

        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "button.btn.flex-auto").click()
        time.sleep(3)
        elements = driver.find_elements(By.CSS_SELECTOR, ".Text__StyledText-sc-1klmep6-0.prc-Text-Text-9mHv3")

        driver.quit()

    def test_case4(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru/code/")
        driver.maximize_window()
        time.sleep(2)

        driver.find_element(By.XPATH, "//button[contains(text(), 'Фильтры')]").click()
        driver.find_element(By.XPATH,
                            "//span[contains(@class, 'ui-tab__text') and contains(text(), 'Профессия')]").click()

        time.sleep(2)
        el = driver.find_element(By.XPATH,
                                 "//span[contains(@class, 'ui-tab__text') and contains(text(), 'От 6 до 12 мес.')]")

        driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'nearest'});", el)
        el.click()

        driver.find_element(By.XPATH,
                            "//span[contains(@class, 'ui-tab__text f f--m') and contains(text(), '1С')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Применить')]") \
            .click()

        time.sleep(3)
        element_text = driver.find_element(By.CSS_SELECTOR, ".programs-filtered-block__total.t.t--1").text
        assert 'Нашли' in element_text
        driver.quit()

    # def test_case4_old(self, set_up_browser):
    #     driver = set_up_browser
    #     driver.get("https://skillbox.ru/code/")
    #     driver.maximize_window()
    #     time.sleep(5)
    #
    #     driver.find_element(By.XPATH,
    #                         "//span[contains(text(), 'Профессия')]").click()
    #
    #     driver.find_element(By.XPATH,
    #                         "//span[contains(@class, 'ui-round-select__field-title') and contains(text(), 'Длительность')]") \
    #         .click()
    #     driver.find_element(By.XPATH,
    #                         "//li[contains(text(), 'От 6 до 12 мес.')]") \
    #         .click()
    #     driver.find_element(By.XPATH,
    #                         "//span[contains(text(), 'Тематика')]") \
    #         .click()
    #     time.sleep(3)
    #     driver.find_element(By.XPATH, "//li[contains(text(), 'Pentest')]") \
    #         .click()
    #     driver.find_element(By.XPATH, "//button[contains(text(), 'Применить')]") \
    #         .click()
    #
    #     time.sleep(3)
    #     driver.quit()

    def test_case5(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/graphs/commit-activity")
        driver.maximize_window()
        el = driver.find_element(By.CSS_SELECTOR, 'path.highcharts-point.highcharts-color-0')
        actions = ActionChains(driver)
        time.sleep(2)

        actions.move_to_element(el).perform()

        time.sleep(3)
        tooltip = driver.find_element(By.CSS_SELECTOR, ".highcharts-tooltip")
        tooltip_text = tooltip.text
        print("Тултип:", tooltip_text)

        # Проверка подскажите пожалуйста в каком направлении смотреть данный текст не проходит.
        expected_text = "Commits 15"
        assert expected_text == tooltip_text, f"Ожидали '{expected_text}', получили '{tooltip_text}'"
        driver.quit()
