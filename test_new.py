from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver

class TestExample:
    def test_new(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        try:
            driver.get("https://mail.ru/")
            print("Заголовок страницы:", driver.title)
            #assert "Skillbox – образовательная платформа с онлайн-курсами." == driver.title
            assert "Mail: Почта, Облако, Календарь, Заметки, Покупки — сервисы для работы и жизни" == driver.title



        finally:
            driver.quit()

if __name__ == "__main__":
    test = TestExample()
    test.test_new()