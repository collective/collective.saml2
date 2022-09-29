# -*- coding: utf-8 -*-

import dm.xmlsec.binding
from zope.i18nmessageid import MessageFactory
LVMessageFactory = MessageFactory("collective.saml2")


def initialize(context):
    """Initializer called when used as a Zope 2 product."""


import bindings  # NOQA
# init default crypto. TODO: make configurable via env var
dm.xmlsec.binding.initialize()
