.PHONY: virtual install build-requirements black isort flake8


init:
	sudo rm -rf data/exchangerate.csv
	sudo apt-get update
	sudo apt-get -y install python-virtualenv
	virtualenv -p /usr/bin/python3 venv

install:
	. venv/bin/activate; \
    	pip3 install -r requirements.txt;
update-requirements: install
	pip3 freeze > requirements.txt
clean:
	venv/bin/black *.py; \
	venv/bin/black module/*.py;
	venv/bin/isort *.py; \
	venv/bin/isort module/*.py; \
	venv/bin/flake8 *.py; \
	venv/bin/flake8 module/*.py;
test:
	. venv/bin/activate;
	@echo "Running Unit Test"
	python3 -m unittest tests/unit_tests/unit_test.py;
	@echo "Running Integration Test"
	python3 -m unittest tests/integration_tests/integration_test.py;
run:
	. venv/bin/activate; \
	python3 main.py;
