test:
	pytest --cov=app --cov-report html

coverage: test
	@firefox htmlcov/index.html

run:
	@python main.py