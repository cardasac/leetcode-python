COV = coverage
SRC := solutions
TESTS := $(wildcard tests/*.py)
HTML := htmlcov
REPORT = ${HTML}/index.html
FILES := tests/*.py solutions
MESSAGE := "Still some linting issues"

.PHONY: install test coverage format clean

test:
	@python -m pytest tests

coverage:
	@${COV} run -m pytest ${TESTS} && ${COV} report -m \
	 && ${COV} html && xdg-open ${REPORT} || echo "Needs more coverage"

format:
	@black ${FILES} --line-length 79
	@pylint ${FILES} || echo ${MESSAGE}
	@flake8 ${FILES} || echo ${MESSAGE}

clean:
	@echo "Cleaning up..."
	@rm -rf htmlcov .pytest_cache .coverage
