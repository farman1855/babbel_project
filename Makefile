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
clean:
	venv/bin/black *.py; \
	venv/bin/black module/*.py;
	venv/bin/isort *.py; \
	venv/bin/isort module/*.py; \
	venv/bin/flake8 *.py; \
	venv/bin/flake8 module/*.py;
run:
	. venv/bin/activate; \
	python3 main.py;
