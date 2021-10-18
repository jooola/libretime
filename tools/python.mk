.ONESHELL:

SHELL = bash
CPU_CORES = $(shell nproc)

# PIP_INSTALL = --editable .
# PYLINT_ARG =
# MYPY_ARG =
# PYTEST_ARG =

ifdef CI
MYPY_FORMAT = --no-color-output
# We change the msg-template because we need an absolute path instead of relative path for CI
# See .github/annotations/python.json
# See https://github.com/actions/runner/issues/659
# See https://github.com/actions/runner/issues/765
PYLINT_FORMAT = --msg-template='{abspath}:{line}:{column}: {msg_id}: {msg} ({symbol})'
else
PYLINT_FORMAT = --output-format=colorized
PYTEST_FORMAT = --color=yes
endif

SHARED_DEV_REQUIREMENTS = \
	black \
	isort \
	mypy \
	pylint \
	pytest \
	pytest-cov \
	pytest-xdist

VENV = venv
$(VENV):
	python3 -m venv $(VENV)
	source $(VENV)/bin/activate
	$(MAKE) install

install: venv
	source $(VENV)/bin/activate
	pip install --upgrade pip setuptools wheel
	pip install $(SHARED_DEV_REQUIREMENTS) $(PIP_INSTALL)

.PHONY: .format
.format: $(VENV)
	source $(VENV)/bin/activate
	black .
	isort . --profile black

.PHONY: .format-check
.format-check: $(VENV)
	source $(VENV)/bin/activate
	black . --check
	isort . --profile black --check

.PHONY: .pylint
.pylint: $(VENV)
	source $(VENV)/bin/activate
	pylint $(PYLINT_ARG) $(PYLINT_FORMAT) || true

.PHONY: .mypy
.mypy: $(VENV)
	source $(VENV)/bin/activate
	mypy $(MYPY_ARG) $(MYPY_FORMAT) || true

.PHONY: .pytest
.pytest: $(VENV)
	source venv/bin/activate
	pytest -n $(CPU_CORES) -v $(PYTEST_ARG) $(PYTEST_FORMAT)

.PHONY: .clean
.clean:
	rm -Rf $(VENV)
