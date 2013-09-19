# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.

# Import the default test settings provided by django_patterns.
from django_patterns.test.project.settings import *

import dj_database_url
DATABASES = {
    'default': dj_database_url.config(
        default='sqlite://:memory:'),
}

# Use django_patterns to detect embedded Django test applications, and add
# them to our INSTALLED_APPS.
from django_patterns.test.discover import discover_test_apps
apps = discover_test_apps('dj_user')
if apps:
    for app in apps:
        INSTALLED_APPS += (app,)
