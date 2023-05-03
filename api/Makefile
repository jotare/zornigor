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
	alembic upgrade head


run-dev:
	# zornigor-dev-api
	uvicorn --port=$(PORT) zornigor.app:app --reload


sources := zornigor scripts
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
