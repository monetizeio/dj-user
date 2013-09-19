# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.
"""
Allows a user to reset their password by generating a one-time-use link
that yields a password reset form, and sending that link to the user's
registered email address.

The workflow for a password reset request is as follows:

    1. The user visits the password_reset URL. The user does not have
       to be authenticated for this request.
    2. The user completes and successfully submits (POST to the
       password_reset URL) the password reset form presented to them,
       which contains just one field for the email address.
    3. The password reset form generates and sends an email containing a
       confirmation link for the reset operation to the email address.
    4. The user is redirected to the password_reset_done URL, which
       informs them that the password reset confirmation email has been
       sent.
    5. From their email client, the user clicks on the confirmation link,
       which loads an password_reset_confirm URL.
    6. The password_reset_confirm URL presents the user with a form for
       setting their new password (knowledge of the old password is not
       required).
    7. Upon successful submission of the set password form, the user is
       redirected to the password_reset_complete URL, which informs
       them that the process is complete.
"""

from django.conf.urls import patterns, url
from django.contrib.auth.views import (password_reset, password_reset_done,
    password_reset_confirm, password_reset_complete)
from django.contrib.auth.tokens import default_token_generator
from ...forms import PasswordResetForm, SetPasswordForm

urlpatterns = patterns('',
    url(r'^$',
        password_reset, {
            # The full name of the template used to display the password reset form
            # to the user. The template is given a RequestContext with just one
            # variable, ‘form’, which contains an instance of ‘password_reset_form’.
            'template_name':         'password/reset.html',
            # The full name of the templates used to generate the confirmation email
            # sent to the user to authorize the password reset request. The
            # templates are given a context which includes the variables ‘email’,
            # ‘domain’, ‘site_name’, ‘uid’, ‘user’, ‘token’, and ‘protocol’ (see the
            # template file for more information).
            'subject_template_name': 'password/reset_email_subject.txt',
            'email_template_name':   'password/reset_email_body.txt',
            # The form which is presented to the user for a password reset request.
            # The default form contains just a single field for the user to specify
            # their email address (which is matched with what is on file in the user
            # account database). See the django.contrib.auth documentation for
            # details on what specific behavior is expected of this form object.
            'password_reset_form':   PasswordResetForm,
            # The token generator is an instance of an object which is capable of
            # generating and validating one-time use tokens for the purposes of a
            # password reset. The default implementation can do so in a secure
            # manner without having to store additional information in the database.
            # Read the code (it's not very complex) at django.contrib.auth.tokens
            # for more information.
            'token_generator':       default_token_generator,
            # A hard-coded redirect to be used after the password reset form has
            # been successfully submitted. If None, the reverse URL lookup of
            # password_reset_done is used instead.
            'post_reset_redirect':   None,
            # The email address to be used in the “From:” header of the confirmation
            # email. If None, the DEFAULT_FROM_EMAIL setting is used instead.
            'from_email':            None,
        }, name='password_reset'),

    # The page shown after a user has submitted a password reset request. It
    # informs the user that a confirmation email has been sent.
    url(r'^done/$',
        password_reset_done, {
            # The full name of the template shown after the user has successfully
            # submitted their password reset request. The template should inform the
            # user that a password reset confirmation email has been sent. It is
            # given a RequestContext without any special context variables.
            'template_name': 'password/reset_done.html',
        }, name='password_reset_done'),

    # Accessed from a link in the confirmation email, this view presents a form
    # for entering a new password.
    url(r'^confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, {
            # The full name of the template used to display the set password form to
            # the user. The template is given a RequestContext with two variables,
            # ‘form’ (an instance of ‘set_password_form’) and ‘validlink’. See the
            # template file for details.
            'template_name':       'password/reset_confirm.html',
            # The token generator is an instance of an object which is capable of
            # validating one-time use tokens for the purposes of a password reset.
            # See the documentatary surrounding password_reset for more
            # information.
            'token_generator':     default_token_generator,
            # The form which is presented to the user for a set password operation.
            # The default form contains just two password fields (for confirmation).
            # See the django.contrib.auth documentation for details on what specific
            # behavior is expected of this form object.
            'set_password_form':   SetPasswordForm,
            # A hard-coded redirect to be used after the set password form has been
            # successfully submitted. If None, the reverse URL lookup of
            # password_reset_complete is used instead.
            'post_reset_redirect': None,
        }, name='password_reset_confirm'),

    # Presents a view which informs the user that the password has been
    # successfully changed.
    url(r'^complete/$',
        password_reset_complete, {
            # The full name of the template shown after the password has been
            # successfully changed. The template is given a RequestContext without
            # any special context variables.
            'template_name': 'password/reset_complete.html',
        }, name='password_reset_complete'),
)
