#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright © 2013 by its contributors. See AUTHORS for details.
# Distributed under the MIT/X11 software license, see the accompanying
# file LICENSE or http://www.opensource.org/licenses/mit-license.php.

from distutils.core import setup
from dj_user import get_version

# Compile the list of packages available, because distutils doesn't have an
# easy way to do this.
import os
packages, data_files = [], []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

for dirpath, dirnames, filenames in os.walk('dj_user'):
    # Ignore dirnames that start with '.'
    for i, dirname in enumerate(dirnames):
        if dirname.startswith('.'): del dirnames[i]
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)
    elif filenames:
        # Strip “dj_user/” or “dj_user\”:
        prefix = dirpath[len('dj_user')+1:]
        for f in filenames:
            data_files.append(os.path.join(prefix, f))

version = get_version().replace(' ', '-')
setup(name='dj-user',
    version=version,
    description=(
        u"Provides batteries-included backends for django.contrib.auth and "
        u"django-registration."),
    author='Mark Friedenbach',
    author_email='mark@monetize.io',
    url='http://github.com/monetizeio/dj-user/',
    download_url='http://pypi.python.org/packages/source/d/dj-user/dj-user-%s.tar.gz' % version,
    package_dir={'dj_user': 'dj_user'},
    packages=packages,
    package_data={'dj_user': data_files},
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=(
        'Django>=1.5',
        'django-crispy-forms>=1.4.0',
        'django-registration>=1.0',
    ),
)
