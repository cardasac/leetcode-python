COV = coverage
TESTS := $(wildcard tests/*.py)
HTML := htmlcov
REPORT = ${HTML}/index.html

.PHONY: install test coverage format clean deploy

install:
	@anaconda-project prepare

test:
	@python -m pytest tests

coverage:
	@anaconda-project run test_coverage

deploy:
	@conda-build .

format:
	@anaconda-project run format

clean:
	@echo "Cleaning up..."
	@rm -rf htmlcov .pytest_cache .coverage
