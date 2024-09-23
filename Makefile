.PHONY: all clean poetry test

INSTALL_STAMP := .install.stamp
POETRY := $(shell command -v poetry 2> /dev/null)
src := demo_inference

all: test


clean:
	@find . -name \*.pyc -delete
	@find . -name __pycache__ -delete
	@rm -fr $(INSTALL_STAMP) .cache/ .coverage .mypy_cache/ .pytest_cache/ *.egg-info/ dist/ htmlcov/

install: $(INSTALL_STAMP)
poetry.lock:
$(INSTALL_STAMP): pyproject.toml poetry.lock
ifndef POETRY
	python3 -m pip install -upgrade poetry
endif
	@poetry install 
	@touch $(INSTALL_STAMP)

test: $(INSTALL_STAMP)
	@poetry run pytest --cov=$(src) --cov-report=term-missing --cov-fail-under=95;
	@poetry run pylint $(src) -j 4 --reports=y || true;
	@poetry run mypy $(src)
