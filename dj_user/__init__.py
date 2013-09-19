# -*- coding: utf-8 -*-
# This file is part of dj-user. dj-user is copyright © 2012-2013, Monetize.io
# Inc. and contributors and released under the terms of the GNU Lesser General
# Public License, version 3 or later. See AUTHORS and LICENSE for more details.

VERSION = (0,1,0, 'final', 0)

def get_version():
    version = '%s.%s' % (VERSION[0], VERSION[1])
    if VERSION[2]:
        version = '%s.%s' % (version, VERSION[2])
    if VERSION[3:] == ('alpha', 0):
        version = '%spre-alpha' % version
    else:
        if VERSION[3] != 'final':
            version = "%s%s" % (version, VERSION[3])
            if VERSION[4] != 0:
                version = '%s%s' % (version, VERSION[4])
    return version
