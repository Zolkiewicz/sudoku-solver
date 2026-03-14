PYTHON_PATH := src/python_gui
C_PATH := src/c_logic
VENV := $(PYTHON_PATH)/venv
PIP := $(VENV)/bin/pip

.PHONY: venv
venv:
	python3 -m venv $(VENV)

.PHONY: install
install: venv
	$(PIP) install -r $(PYTHON_PATH)/requirements.txt

.PHONY: clib
clib:
	$(MAKE) -C $(C_PATH)

.PHONY: clean
clean:
	$(MAKE) -C $(C_PATH) clean
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete