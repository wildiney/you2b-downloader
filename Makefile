.PHONY: format lint test sec


format:
	@blue . 
	@isort . 
lint:
	@blue . --check
	@isort . --check
	@prospector 
test:
	@pytest -v
sec:
	@pip-audit