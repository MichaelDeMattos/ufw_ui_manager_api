REVISION_MESSAGE ?= "ct"

install:
	@poetry install --no-root

lint:
	@poetry run ruff check ufw_ui_manager_api --no-cache

lint-fix:
	@poetry run ruff check ufw_ui_manager_api --no-cache --fix

db-revision-autogenerate:
	@poetry run alembic revision -m ${REVISION_MESSAGE} --autogenerate
