fix:
	poetry run ruff check . --select I --fix
	poetry run ruff format .
	poetry run ruff check . --fix