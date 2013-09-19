#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.

import os
import sys

try:
    from django.core.management import execute_from_command_line
except ImportError:
    sys.stderr.write(
        # The following is not transalated because in this particular error
        # condition `sys.path` is probably not setup correctly, and so we
        # cannot be sure that we'd import the translation machinery correctly.
        # It'd be better to print the correct error in English than to trigger
        # another not-so-helpful ImportError.
        u"Error: Can't find the module 'django.core.management' in the "
        u"Python path. Please execute this script from within the virtual "
        u"environment containing your project.\n")
    sys.exit(1)

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'xunit.settings')
    execute_from_command_line(sys.argv)
