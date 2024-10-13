CONTAINER_NAME=app

up-build:
	sudo docker-compose up --build

up:
	sudo docker-compose up

up-windows:
	powershell -ExecutionPolicy Bypass -File ./run.ps1 -action up-build

down:
	sudo docker-compose down

shell:
	sudo docker-compose exec $(CONTAINER_NAME) /bin/sh

migrate:
	sudo docker-compose exec $(CONTAINER_NAME) alembic upgrade head

test:
	sudo docker-compose exec $(CONTAINER_NAME) pytest

code-convention:
	flake8
	pycodestyle