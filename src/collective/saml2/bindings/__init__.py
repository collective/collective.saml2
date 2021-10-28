# -*- coding: utf-8 -*-
#Additional bindings required by ADFS server. The list may get longer in the future.

import pyxb

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.6'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

from . import ws_fed
