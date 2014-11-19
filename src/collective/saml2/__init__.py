# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory
LVMessageFactory = MessageFactory("collective.saml2")


def initialize(context):
    """Initializer called when used as a Zope 2 product."""

import bindings
# init default crypto. TODO: make configurable via env var
import dm.xmlsec.binding
dm.xmlsec.binding.initialize()