# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.
"""
The activation process is quite simple: the user clicks on a
registration_activate link from within their email client, and the mere
act of requesting the page results in the account being activated. The
user is then redirected to the registration_activation_complete and is
informed of the activation of their account.

NOTE: A full description of the registration and activation workflow, as
      well as the registration URL's can be found in the form module.
"""

from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from ...views import ActivationView

urlpatterns = patterns('',
    # NOTE: I've tried to layout the URL's in a logical ordering, but in this
    #       case registration_activation_complete must come before
    #       registration_activate (which follows) as the regular expression for
    #       the latter matches the former.

    # The page shown after the user has successfully activated their account.
    url(r'^complete/$',
        # The template to be used to inform the user that their account has been
        # successfully activated. The template is passed a RequestContext
        # without any special context variables.
        TemplateView.as_view(template_name='registration/activation_complete.html'),
        name='registration_activation_complete'),

    # The URL handler for the activation link sent via email to the new user as
    # part of the new account registration process. See urls.registration.signup
    # for more information.
    #
    # NOTE: Activation keys get matched by \w+ instead of the more specific
    #       [a-fA-F0-9]{40} because a bad activation key should still get to the
    #       view; that way it can return a sensible “invalid key” message
    #       instead of a confusing 404.
    url(r'^(?P<activation_key>\w+)/$',
        ActivationView.as_view(template_name='registration/activation_failed.html'),
        name='registration_activate'),
)
