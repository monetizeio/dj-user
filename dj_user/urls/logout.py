# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.

from django.conf.urls import patterns, url
from django.contrib.auth.views import logout

urlpatterns = patterns('',
    # Logs the user out.
    url(r'^$',
        logout, {
            # The full name of the template used after logging the user out if
            # neither a run-time nor a hard-coded redirect is requested (see above).
            # The template receives a RequestContext with three additional
            # variables: ‘site’, ‘site_name’, and ‘title’ (see the documentation in
            # the template file for details).
            'template_name':       'auth/logout.html',
            # The GET field which may contain a URL to redirect to after logout. If
            # this field is not set, the hard-coded ‘next_page’ parameter used
            # instead. If ‘next_page’ is None, the template specified by the
            # ‘template_name’ parameter is rendered and returned.
            'redirect_field_name': 'next',
            # The hard-coded URL to redirect to after a successful logout, assuming
            # the ‘redirect_field_name’ is empty or not specified (see above).
            'next_page':           None,
        }, name='logout'),
)
