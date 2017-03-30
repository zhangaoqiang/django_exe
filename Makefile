help:
	@echo "server           run dev server"
	@echo "doc              run doc server"
	@echo "shell            open a python shell"
	@echo "mkmigrate        makemigrations"
	@echo "migrate          migrate"
	@echo "clean            clean"
	@echo "lint             run flake8 check"

server:
	@python manage_local.py runserver 0.0.0.0:8000

shell:
	@python manage_local.py shell

mkmigrate:
	@python manage_local.py makemigrations

migrate:
	@python manage_local.py migrate

clean: clean-build clean-pyc
	@rm -fr cover/

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr *.egg-info

clean-pyc:
	@find . -type f -name '*.pyc' -delete
	@find . -type f -name '*.pyo' -delete
	@find . -type f -name '*~' -delete
	@find . -type f -name '*,cover' -delete

lint:
	@flake8 . --exclude=.venv,migrations,wechat/libs/

doc:
	@mkdocs serve

.PHONY: server shell clean clean-build clean-pyc lint migrate mkmigrate