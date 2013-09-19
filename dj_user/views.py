# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.

__all__ = (
    'RegistrationView',
    'ActivationView',
)

import registration.backends.default.views
class RegistrationView(registration.backends.default.views.RegistrationView):
    from .forms import RegistrationForm as form_class

    # URL to redirect to if registration is not permitted for the current
    # HttpRequest. Must be a value which can legally be passed to
    # django.shortcuts.redirect.
    disallowed_url = ('registration_closed', (), {})

    # The django-registration default is registration_complete, but
    # the alternative registration_done fits better with the naming
    # scheme of django.contrib.auth.
    def get_success_url(self, request, user):
        """
        Return the name of the URL to redirect to after successful
        user registration.
        """
        return ('registration_done', (), {})

# We don't need to make any changes to the default registration
# backend's ActivationView.
from registration.backends.default.views import ActivationView
