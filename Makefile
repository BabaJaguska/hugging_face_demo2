install:
	pip install --upgrade pip
	pip install -r requirements.txt
lint:
	flake8 --max-line-length=88 .
format:
	black .
all:
	install lint format
