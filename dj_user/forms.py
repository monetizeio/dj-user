# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.

from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse

from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from crispy_forms.bootstrap import *

import django.contrib.auth.forms

class AuthenticationForm(django.contrib.auth.forms.AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form-login'
        self.helper.form_action = reverse('login')
        self.helper.layout = Layout()
        self.helper.layout.extend((
            HTML(u"".join((u"<h2>", _(u"Login"), u"</h2>"))),
            HTML(u"".join((u"<p>", _(u"<a href=\"%(password_reset_url)s\">"
                u"Forgot</a> your password? <a href=\"%(registration_url)s\">"
                u"Need an account</a>?") % {
                    'password_reset_url': reverse('password_reset'),
                    'registration_url':   reverse('registration'),
                }, u"</p>"))),
            'username',
            'password',
            FormActions(
                Submit('login', _(u"Authenticate")),
            ),
        ))

class PasswordChangeForm(django.contrib.auth.forms.PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form-password-change'
        self.helper.form_action = reverse('password_change')
        self.helper.layout = Layout()
        self.helper.layout.extend((
            HTML(u"".join((u"<h2>", _(u"Change password"), u"</h2>"))),
            HTML(u"".join((u"<p>", _(u"Enter your old password, and your new "
                u"password twice (for verification) in the form below."),
                u"</p>"))),
            'old_password',
            'new_password1',
            'new_password2',
            FormActions(
                Submit('password-change', _("Change password")),
            ),
        ))

class PasswordResetForm(django.contrib.auth.forms.PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form-password-reset'
        self.helper.form_action = reverse('password_reset')
        self.helper.layout = Layout()
        self.helper.layout.extend((
            HTML(u"".join((u"<h2>", _(u"Reset password"), u"</h2>"))),
            HTML(u"".join((u"<p>", _(u"Forgot your password? Enter your "
                u"email in the form below and we'll send you instructions on "
                u"how to create a new one."), u"</p>"))),
            'email',
            FormActions(
                Submit('password-reset', _(u"Send reset token")),
            ),
        ))

class SetPasswordForm(django.contrib.auth.forms.SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(SetPasswordForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form-set-password'
        self.helper.layout = Layout()
        self.helper.layout.extend((
            HTML(u"".join((u"<h2>", _(u"Set password"), u"</h2>"))),
            HTML(u"".join((u"<p>", _(u"Enter your new password below to "
                u"reset your password."), u"</p>"))),
            'new_password1',
            'new_password2',
            FormActions(
                Submit('set-password', _(u"Set password")),
            ),
        ))

import registration.forms

class RegistrationForm(registration.forms.RegistrationFormTermsOfService,
                       registration.forms.RegistrationFormUniqueEmail):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'form-registration'
        self.helper.form_action = reverse('registration')
        self.helper.layout = Layout()
        self.helper.layout.extend((
            HTML(u"".join((u"<h2>", _(u"Signup"), u"</h2>"))),
            HTML(u"".join((u"<p>", _(u"Please provide a username, password, "
                u"and email address. An activation link will be sent to the "
                u"email address provided."), u"</p>"))),
            'username',
            'email',
            'password1',
            'password2',
            'tos',
            FormActions(
                Submit('registration', _(u"Send activation email")),
            ),
        ))
