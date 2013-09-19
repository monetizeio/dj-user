# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.

# Import the default test urls provided by django_patterns.
from django_patterns.test.project.urls import *

from django.conf.urls import patterns, include, url

urlpatterns += patterns(
    url(r'^login/',                   include('dj_user.urls.login')),
    url(r'^logout/',                  include('dj_user.urls.logout')),
    url(r'^signup/',                  include('dj_user.urls.registration.signup')),
    url(r'^account/activate/',        include('dj_user.urls.registration.activate')),
    url(r'^account/password/change/', include('dj_user.urls.password.change')),
    url(r'^account/password/reset/',  include('dj_user.urls.password.reset')),
)
