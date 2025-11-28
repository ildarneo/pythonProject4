# Makefile
run_tests:
	echo "before tests"
	pytest
	echo "after tests"


# Путь к папке с тестами
TEST_PATH=src/tests

.PHONY: show_cases run_tests

# Команда для отображения всех тестов (коллекция тестов)
show_cases:
    pytest --collect-only $(TEST_PATH)

# Команда для запуска всех тестов
run_tests:
    pytest $(TEST_PATH)