.PHONY: install upload ci

VIRTUALENV = $(shell which virtualenv)

ifeq ($(strip $(VIRTUALENV)),)
  VIRTUALENV = /usr/local/python/bin/virtualenv
endif

nopyc:
	find . -name '*.pyc' | xargs rm -f || true
	find . -name __pycache__ | xargs rm -rf || true

clean:
	rm -rf build cover coverage.xml league-oracle.egg-info venv

install: venv
	. venv/bin/activate; pip install --editable .

venv:
	$(VIRTUALENV) venv
