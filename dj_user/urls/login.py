# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.

from django.utils.http import urlencode
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

from django.template.response import TemplateResponse
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.views import login as auth_login

from ..forms import AuthenticationForm

# This would normally be in views.py, however since most of the code that
# follows is configuration of default parameters, it made since to place it
# here.
def login(request,
        template_name='auth/login.html',
        redirect_field_name=REDIRECT_FIELD_NAME,
        authentication_form=AuthenticationForm,
        current_app=None, extra_context=None):
    """
    template_name
        The full name of the template file used to display the login form to
        the user. The template is given a RequestContext with four extra
        variables: ‘form’, ‘next’, ‘site’, and ‘site_name’ (see the
        documentation in the template file for details).

    redirect_field_name
        The request parameter which may contain a URL to redirect to after logout.
        If this field is not set, the LOGIN_REDIRECT_URL setting is used instead.

    authentication_form
        The form which is presented to the user for authentication. It may be
        overriden in the context of alternative authentication methods. See
        the django.contrib.auth documentation for details on what specific
        behavior is expected of this form object.
    """
    response = auth_login(request,
        template_name=template_name,
        redirect_field_name=redirect_field_name,
        authentication_form=authentication_form,
        current_app=current_app,
        extra_context=extra_context)
    # Inject the hidden “next” field into the form. This is the least
    # messy option discovered so far for this particular combination of
    # django.contrib.auth and django-crispy-forms.
    if isinstance(response, TemplateResponse):
        redirect_to = response.context_data[redirect_field_name]
        helper = response.context_data['form'].helper
        if redirect_to:
            helper.form_action += ''.join((
                u'?', urlencode({redirect_field_name: redirect_to})))
            helper.layout.append(
                Hidden(redirect_field_name, redirect_to))
    return response

from django.conf.urls import patterns, url
urlpatterns = patterns('',
    # Authenticates and logs a user in.
    url(r'^$', login, name='login'),
)
