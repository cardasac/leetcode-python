COV = coverage
FOLDERS = solutions tests
TESTS := $(wildcard tests/*.py)
HTML := htmlcov
REPORT = ${HTML}/index.html
LINE_LENGTH := 79

.PHONY: install test coverage format clean

test:
	uv run pytest

format:
	uv run ruff check --fix

clean:
	@echo "Cleaning up..."
	@rm -rf htmlcov .pytest_cache .coverage
