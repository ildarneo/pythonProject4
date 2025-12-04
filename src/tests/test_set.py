class TestExample:

    def test_skillbox(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://skillbox.ru")
        print("Заголовок страницы:", driver.title)
        assert "Skillbox – образовательная платформа с онлайн-курсами." == driver.title

    def test_mail(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://mail.ru")
        print("Заголовок страницы:", driver.title)
        # Проверка заголовка
        assert "Mail" == driver.title

    def test_swim(self, set_up_browser):
        driver = set_up_browser
        driver.get("https://swimmasters.ru/")
        print("Заголовок страницы:", driver.title)
        # Проверка заголовка
        assert "Федерация" in driver.title