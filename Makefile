.PHONY: virtual install build-requirements black isort flake8


init:
	sudo apt-get update
	sudo apt-get install python-virtualenv
	virtualenv -p /usr/bin/python3 venv

install:
	. venv/bin/activate; \
    	pip3 install -r requirements.txt; \
	pip3 install -U black; \
	pip3 install -U isort; \
	pip3 install -U flake8;
update-requirements: install
	pip3 freeze > requirements.txt
isort: venv/bin/isort # Sorts imports using isort
	venv/bin/isort *.py

flake8: venv/bin/flake8 # Lints code using flake8
	. venv/bin/activate;
	venv/bin/flake8 *.py
