# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.
"""
Allows a user to change their password.

The workflow for a password change request is as follows:

    1. The user visits the password_change URL. If the user has not
       authenticated, they are redirected to login for authentication
       first.
    2. The user completes and successfully submits (POST to the
       password_change URL) the password change form, which contains
       the old password (once) and the new password (twice).
    3. The user is redirected to ‘post_change_redirect’ (if specified) or to
       password_change_done (the default).
"""

from django.conf.urls import patterns, url
from django.contrib.auth.views import password_change, password_change_done
from ...forms import PasswordChangeForm

urlpatterns = patterns('',
    url(r'^$',
        password_change, {
            # The full name of the template used to display the password change form
            # to the user. The template is given a RequestContext with just one
            # variable, ‘form’, which contains an instance of
            # ‘password_change_form’.
            'template_name':        'password/change.html',
            # A hard-coded redirect to be used after the password change form has
            # been successfully submitted. If None, the reverse URL lookup of
            # password_change_done is used instead.
            'post_change_redirect': None,
            # The form which is presented to the user for a password change request.
            # See the django.contrib.auth documentation for details on what specific
            # behavior is expected of this form object.
            'password_change_form': PasswordChangeForm,
        }, name='password_change'),

    # The page shown after a user has changed their password.
    url(r'^done/$',
        password_change_done, {
            # The full name of the template shown after the user has successfully
            # changed their password. The template is given a RequestContext without
            # any special context variables.
            'template_name': 'password/change_complete.html',
        }, name='password_change_done'),
)
