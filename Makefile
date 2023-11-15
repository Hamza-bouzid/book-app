create_venv:
	python3.11 -m venv venv &&\
		source venv/bin/activate

install:
	pip install --upgrade pip &&\
		pip install -r src/requirements.txt &&\
		pip install -r tests/requirements.txt

format:
	black src/*.py tests/*.py
lint:
	flake8 src/*.py tests/*.py
test:
	flake8 src && pytest tests/unit -v
deploy:
	#deploy command
all: install format lint test deploy
