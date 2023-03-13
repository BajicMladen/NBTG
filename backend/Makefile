mm:
	@python manage.py makemigrations

migrate:
	@python manage.py migrate

sm:
	@python manage.py showmigrations

smu:
	@python manage.py showmigrations | grep '\[ \]\|^[a-z]' | grep '[  ]' -B 1 || true

su:
	@python manage.py createsuperuser

cs:
	@python manage.py collectstatic

sort:
	@isort .

freeze:
	@pip freeze > requirements.txt

deps:
	@pip install -r requirements.txt

cc:
	@find . -name \*.pyc -delete
