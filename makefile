build:
	python3 -m pkgs.core

black:
	black -l 80 pkgs/core.py

clean:
	find . -type d -name __pycache__ | xargs rm -rf

ready:
	python3 -m venv venv; \
	. venv/bin/activate; \
	pip install -U pip; \
	pip install -r requirements.txt; \
	deactivate

.phony: build black clean ready
