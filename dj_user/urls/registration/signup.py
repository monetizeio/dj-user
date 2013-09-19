# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.
"""
URL patterns for new account registration, using django-registration's
default backend. This registration backend has the following workflow for
new user account registration:

  1. User visits the registration URL and fills out the new account
     registration form, which includes such information as the desired
     username, password, and email address to associate with the account.

  2. If registration is open (settings.REGISTRATION_OPEN is True), upon
     successful submission of the new account registration form the user
     is redirected to the registration_done URL which informs them that an
     activation link has been sent to the email address they specified.

     If registration is closed (settings.REGISTRATION_OPEN is False), upon
     successful submission of the new account registration form the user
     is redirected to the registration_closed URL which thanks them for
     their interest, informs that the site is currently closed for new
     users, that their email has been added to a wait-list, etc.

  3. From their email client, the user clicks on the activation link which
     takes them to a unique registration_activate URL. Their account is
     then activated, and they are redirected to
     registration_activation_complete.

  4. Registration is finished and the user may now login.

NOTE: Activation urls and their documentation can be found in the
      urls.registration.activate module.
"""

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from ...views import RegistrationView

urlpatterns = patterns('',
    # The registration view provides the workflow and logic for new user account
    # registration. The default view, which we are using, requires that the user
    # verify ownership of the email address they provide through an activation
    # email before the user account can be used. See the django-registration
    # documentation and source code (it's quite simple) for more information.
    url(r'^$',
        # The template used to show the new account registration form to the
        # user. It receives a ‘form’ variable provided by the backend as context.
        RegistrationView.as_view(template_name='registration/signup.html'),
        name='registration'),

    # If the setting REGISTRATION_OPEN is False, new user registrations are not
    # allowed and an attempt to register is redirected to a page which explains
    # the situation, the registration_closed URL.
    url(r'^closed/$',
        # The full name of the template shown after the user has successfully
        # submitted a new account registration form while registration is
        # closed. The template is given a RequestContext without any special
        # context variables.
        TemplateView.as_view(template_name='registration/closed.html'),
        name='registration_closed'),

    # The page shown after the user has completed the new account registration
    # form (if the setting REGISTRATION_OPEN is not False). In the case of the
    # default registration backend, its purpose is to tell the user that an
    # activation email has been sent to the email account they specified.
    url(r'^complete/$',
        # The full name of the template shown after the user has successfully
        # submitted a new account registration form and an activation email has
        # been sent. The template is given a RequestContext without any special
        # context variables.
        TemplateView.as_view(template_name='registration/done.html'),
        name='registration_done'),
)
