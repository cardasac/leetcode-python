COV = coverage
FOLDERS = solutions tests
TESTS := $(wildcard tests/*.py)
HTML := htmlcov
REPORT = ${HTML}/index.html
LINE_LENGTH := 79

.PHONY: install test coverage format clean deploy

test:
	poetry run pytest -n auto

type-check:
	poetry run mypy solutions

format:
	black $(FOLDERS) --line-length $(LINE_LENGTH)
	pylint $(FOLDERS)
	flake8 $(FOLDERS) --count --show-source --statistics --exit-zero --max-complexity=10 --max-line-length=$(LINE_LENGTH)

clean:
	@echo "Cleaning up..."
	@rm -rf htmlcov .pytest_cache .coverage
