# dideban

simple Attendance system written in python and django.


clone the repo 

	git clone https://github.com/foss4/dideban && cd dideban

install virtualenv package 

	python3 -m pip install virtualenv
make new virtual env and activate it:

	python3 -m virtualenv .venv && source .venv/bin/activate

install requirements:

	pip install -r requirements/local.txt


run project with:

	python3 manage.py makemigrations
	python3 manage.py migrate
	python3 manage.py runserver

for swagger open localhost:8000 in browser
