PY ?= python3
PELICAN ?= pelican
PELICANOPTS =
VENV ?= .venv

BASEDIR = $(CURDIR)
INPUTDIR = $(BASEDIR)/content
OUTPUTDIR = $(BASEDIR)/output
CONFFILE = $(BASEDIR)/pelicanconf.py
PUBLISHCONF = $(BASEDIR)/publishconf.py

help:
	@echo 'Makefile for the portfolio site'
	@echo ''
	@echo 'Usage:'
	@echo '   make venv           create $(VENV) and install Python deps'
	@echo '   make css            build Tailwind CSS once'
	@echo '   make css-watch      rebuild Tailwind CSS on change'
	@echo '   make html           build the site with dev settings'
	@echo '   make serve          serve output/ at http://localhost:8000'
	@echo '   make devserver      build, serve, and auto-reload on change'
	@echo '   make publish        build the site with production settings'
	@echo '   make clean          remove the generated output'
	@echo ''

venv: $(VENV)/.installed

# Re-runs only when requirements.txt changes. Running venv over an existing
# directory also repairs one that is missing pip.
$(VENV)/.installed: requirements.txt
	$(PY) -m venv $(VENV)
	$(VENV)/bin/python -m pip install --upgrade pip
	$(VENV)/bin/python -m pip install -r requirements.txt
	touch $@

css:
	npm run build:css

css-watch:
	npm run watch:css

html:
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

serve:
	$(PELICAN) -l $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

devserver:
	$(PELICAN) -lr $(INPUTDIR) -o $(OUTPUTDIR) -s $(CONFFILE) $(PELICANOPTS)

publish: css
	$(PELICAN) $(INPUTDIR) -o $(OUTPUTDIR) -s $(PUBLISHCONF) $(PELICANOPTS)

clean:
	rm -rf $(OUTPUTDIR)

.PHONY: help venv css css-watch html serve devserver publish clean
