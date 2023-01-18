
install:
	virtualenv venv
	pip3 install -r requirements/all
	cp .env.example .env

start: 
	python3 ncr.py