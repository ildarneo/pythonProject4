# Путь к папке с тестами (по умолчанию)
TEST_PATH=src/tests

# Общие параметры pytest
PYTEST_PARAMS=--disable-warnings --reruns 3 --maxfail=1 --tb=short --testpaths=$(TEST_PATH)

.PHONY: show_cases
show_cases:
    pytest --collect-only $(PYTEST_PARAMS)

.PHONY: run_tests
run_tests:
    pytest $(PYTEST_PARAMS)