# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.

ROOT=$(shell pwd)
CACHE_ROOT=${ROOT}/.cache
PYENV=${ROOT}/.pyenv
CONF=${ROOT}/conf
APP_NAME=dj-user
PACKAGE_NAME=dj_user

-include Makefile.local

.PHONY: all
all: python

.PHONY: python
python: ${PYENV}/.stamp-h

.PHONY: check
check: all
	mkdir -p "${ROOT}"/build/report
	"${PYENV}"/bin/python -Wall "${ROOT}"/manage.py test \
	  --settings=xunit.settings \
	  --with-xunit \
	  --xunit-file="${ROOT}"/build/report/xunit.xml \
	  --with-xcoverage \
	  --xcoverage-file="${ROOT}"/build/report/coverage.xml \
	  --cover-package=${PACKAGE_NAME} \
	  --cover-erase \
	  --cover-tests \
	  --cover-inclusive \
	  ${PACKAGE_NAME}

.PHONY: shell
shell: all
	"${PYENV}"/bin/python "${ROOT}"/manage.py shell_plusplus \
	  --settings=tests.settings \
	  --print-sql \
	  --ipython

.PHONY: mostlyclean
mostlyclean:
	-rm -rf dist
	-rm -rf build
	-rm -rf .coverage

.PHONY: clean
clean: mostlyclean
	-rm -rf "${PYENV}"

.PHONY: distclean
distclean: clean
	-rm -rf "${CACHE_ROOT}"
	-rm -rf Makefile.local

.PHONY: maintainer-clean
maintainer-clean: distclean
	@echo 'This command is intended for maintainers to use; it'
	@echo 'deletes files that may need special tools to rebuild.'

# ===--------------------------------------------------------------------===

.PHONY: dist
dist:
	"${PYENV}"/bin/python setup.py sdist

# ===--------------------------------------------------------------------===

${CACHE_ROOT}/virtualenv/virtualenv-1.10.1.tar.gz:
	mkdir -p "${CACHE_ROOT}"/virtualenv
	curl -L 'https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.10.1.tar.gz' >'$@'

${PYENV}/.stamp-h: ${ROOT}/requirements.txt ${CONF}/requirements*.txt ${CACHE_ROOT}/virtualenv/virtualenv-1.10.1.tar.gz
	# Because build and run-time dependencies are not thoroughly tracked,
	# it is entirely possible that rebuilding the development environment
	# on top of an existing one could result in a broken build. For the
	# sake of consistency and preventing unnecessary, difficult-to-debug
	# problems, the entire development environment is rebuilt from scratch
	# everytime this make target is selected.
	rm -rf ${PYENV}
	
	# The ${PYENV} directory, if it exists, was removed above. The
	# PyPI cache is nonexistant if this is a freshly checked-out
	# repository, or if the `distclean` target has been run.  This
	# might cause problems with build scripts executed later which
	# assume their existence, so they are created now if they don't
	# already exist.
	mkdir -p "${PYENV}"
	mkdir -p "${CACHE_ROOT}"/pypi
	
	# `virtualenv` is used to create a separate Python installation for
	# this project in `${PYENV}`.
	tar \
	    -C "${CACHE_ROOT}"/virtualenv --gzip \
	    -xf "${CACHE_ROOT}"/virtualenv/virtualenv-1.10.1.tar.gz
	python "${CACHE_ROOT}"/virtualenv/virtualenv-1.10.1/virtualenv.py \
	    --clear \
	    --distribute \
	    --never-download \
	    --prompt="(${APP_NAME}) " \
	    "${PYENV}"
	-rm -rf "${CACHE_ROOT}"/virtualenv/virtualenv-1.10.1
	
	# readline is installed here to get around a bug on Mac OS X
	# which is causing readline to not build properly if installed
	# from pip, and the fact that a different package must be used
	# to support it on Windows/Cygwin.
	if [ "x`uname -o`" == "xCygwin" ]; then \
	    "${PYENV}"/bin/pip install pyreadline; \
	else \
	    "${PYENV}"/bin/easy_install readline; \
	fi
	
	# pip is used to install Python dependencies for this project.
	for reqfile in "${ROOT}"/requirements.txt \
	               "${CONF}"/requirements*.txt; do \
	    CFLAGS=-I/opt/local/include LDFLAGS=-L/opt/local/lib \
	    "${PYENV}"/bin/python "${PYENV}"/bin/pip install \
	        --download-cache="${CACHE_ROOT}"/pypi \
	        -r "$$reqfile"; \
	done
	
	# All done!
	touch "${PYENV}"/.stamp-h
