import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# @pytest.fixture()
# def set_up_browser():
#     options = Options()
#     options.page_load_strategy = 'none'
#     # Создаем драйвер локально с помощью webdriver_manager
#     driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#     yield driver
#     driver.quit()

class TestPraktik5:
    def test_case1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/")
        driver.find_element(By.XPATH,'//*[contains(text(),"The future of building happens together")]')
        # добавьте ваши проверки или действия здесь
        pass
    def test_casewait(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/")
        driver.find_element(By.XPATH,'//*[contains(text(),"The future of building happens together")]')
        # добавьте ваши проверки или действия здесь
        pass
    def testwait_types(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/")
        #driver.find_element(By.XPATH,'//*[contains(text(),"The future of building happens together")]')
        # добавьте ваши проверки или действия здесь
        WebDriverWait(driver, timeout=3).until(
            lambda d: d.find_element(By.XPATH, '//*[contains(text(),"The future of building happens together")]')
        )
        pass

    def test_mail(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://mail.ru")
        print("Заголовок страницы:", driver.title)
        # Проверка заголовка
        assert "Mail" == driver.title

    def test_mail1(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://mail.ru")
        print("Заголовок страницы:", driver.title)
        # Проверка заголовка
        assert "Mail: Почта, Облако, Календарь, Заметки, Покупки — сервисы для работы и жизни" == driver.title


    def test_case2(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://github.com/microsoft/vscode/issues")
        driver.find_element(By.XPATH, "//span[text()='Author']").click()
        search_input = driver.find_element(By.CSS_SELECTOR, "input[aria-label='Filter authors']")
        search_input.send_keys("bpasero")
        search_input.click()
        time.sleep(3)
        #driver.find_element(By.CLASS_NAME, "prc-ActionList-ItemLabel-TmBhn").click()

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
        driver.find_element(By.ID, "search_filename").send_keys("environment.yml")

        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, "button.btn.flex-auto").click()
        time.sleep(3)
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
                            "//span[contains(@class, 'ui-tab__text') and contains(text(), 'Android')]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//button[contains(text(), 'Применить')]") \
            .click()

        time.sleep(3)
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
        time.sleep(6)

        # Навести мышку на элемент
        actions.move_to_element(el).perform()
        time.sleep(6)
        pass
        driver.quit()
