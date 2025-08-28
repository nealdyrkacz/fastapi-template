install-requirements:
	pip install -r requirements.txt
migration:
ifneq ($(name),)
	alembic revision -m $(name)
else
	@echo "make migration name=<name>"
endif

migrate:
	docker compose exec template-api bash -c 'alembic upgrade head'

migrate-down:
	docker compose exec template-api bash -c 'alembic downgrade -1'
