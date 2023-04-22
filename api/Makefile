PORT := 8080

venv:
	pyenv virtualenv zornigor
	pyenv local zornigor

install:
	pip install --upgrade pip
	pip install -e .

run-dev:
	# zornigor-dev-api
	uvicorn --port=8080 zornigor.app:app --reload
