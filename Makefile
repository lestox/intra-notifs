# Installer les dépendances Python
install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

# Lancer le script principal
run:
	python run.py

# Exécuter les tests
test:
	pytest

# Lint avec ruff
lint:
	ruff check .

# Appliquer les corrections de style avec ruff
fix:
	ruff check . --fix

# Formatage avec black
format:
	black .
