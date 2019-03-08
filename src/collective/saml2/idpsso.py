# Copyright (C) 2011-2012 by Dr. Dieter Maurer <dieter@handshake.de>
"""The Idpsso implementation."""
from datetime import datetime, timedelta
import json

from zope.interface import implements

from AccessControl import ClassSecurityInfo
from OFS.SimpleItem import SimpleItem
from ZTUtils import make_query

from Products.CMFCore.utils import getToolByName

from dm.saml2.uuid import uuid
from dm.saml2.util import compare_classes, normalize_nameid_format
from dm.zope.schema.schema import SchemaConfigured
from dm.saml2.pyxb.assertion import AssertionType

from dm.zope.saml2.interfaces import ISimpleIdpsso, IApRole, \
     INameidFormatSupport, IRelayStateStore
from dm.zope.saml2.permission import manage_saml
from dm.zope.saml2.sso import Sso
from dm.zope.saml2.role import Target
from dm.zope.saml2.attribute import SimpleAttributeProvider
from dm.zope.saml2.idpsso.idpsso import SimpleIdpsso

from zope.component.hooks import getSite
from dm.saml2.pyxb.protocol import CreateFromDocument

class CookieRelayStateStore(object):
  """ A store to override the default OOBTree store in dm.zope.saml2.
  During the login process, if a user is not logged in, the request and relay_state
  is stored temporarily while the user is asked to login. This is in the SimpleIdpsso.
  Instead of causing a transaction or the hassles of using sessions and then
  ensuring session data is replicated, we store the request back into a cookie.
  """

  implements(IRelayStateStore)

  def __init__(self, context):
      self.context = context

  def __setitem__(self, id, v):
      """store *v* under *id*."""
      portal = getSite()
      # Interface says this can be anything. We are assuming
      # (<dm.saml2.pyxb.protocol.AuthnRequestType>, string)
      reqxml = v[0].toxml().encode('base64')
      tostore = json.dumps( (reqxml, v[1]) )
      # Force the cookie to be set at the portal root
      portal.REQUEST.response.setCookie(id, tostore, path='/')

  def __getitem__(self, id):
      """retrieve value associated with *id*."""
      portal = getSite()
      v = json.loads(portal.REQUEST.get(id))
      reqxml = v[0].decode('base64')
      req = CreateFromDocument(reqxml)
      return (req, v[1])


  def __delitem__(self, id):
      """delete value under *id*."""

  def clear(self):
      """clear the complete store."""

