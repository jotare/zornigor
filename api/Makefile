PORT := 8080

venv:
	pyenv virtualenv zornigor
	pyenv local zornigor

dist-install: venv install install-db

install:
	pip install --upgrade pip
	pip install -r requirements-test.txt
	pip install -r requirements-dev.txt
	pip install -e .

install-db:
	@python scripts/create_db.py


run-dev:
	# zornigor-dev-api
	uvicorn --port=8080 zornigor.app:app --reload


sources := zornigor
tests := zornigor/tests

lint:
	flake8 --config=setup.cfg
	isort -c --profile black $(sources) $(tests)


format:
	isort --profile black $(sources) $(tests)
	black $(sources) $(tests)


.PHONY: tests
tests:
	pytest -svv zornigor/tests/
