## _md,  _ds and _xenc modules are not used as they are conflicting with existing bindings. 
## They are kept for the reference.

# ./ws_fed.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:d1bc8beb93ce522213ce017eabfce6bd653da8b9
# Generated 2014-10-10 17:20:20.705888 by PyXB version 1.2.3
# Namespace http://docs.oasis-open.org/wsfed/federation/200706

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:dbbe0922-5090-11e4-8d5b-3c77e646c78e')

# Version of PyXB used to generate the bindings
_PyXBVersion = '1.2.3'
# Generated bindings are not compatible across PyXB versions
if pyxb.__version__ != _PyXBVersion:
    raise pyxb.PyXBVersionError(_PyXBVersion)

# Import bindings for namespaces imported into schema
#import _md as _ImportedBinding__md
import pyxb.bundles.saml20.raw.metadata as _ImportedBinding__md
import pyxb.binding.datatypes
#import _ds as _ImportedBinding__ds
import pyxb.bundles.wssplat.raw.ds as _ImportedBinding__ds
import _sp as _ImportedBinding__sp
import _wsu as _ImportedBinding__wsu
import _auth as _ImportedBinding__auth
import _wsa as _ImportedBinding__wsa

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://docs.oasis-open.org/wsfed/federation/200706', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_wsa = _ImportedBinding__wsa.Namespace
_Namespace_wsa.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_auth = _ImportedBinding__auth.Namespace
_Namespace_auth.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_wsu = _ImportedBinding__wsu.Namespace
_Namespace_wsu.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_ds = _ImportedBinding__ds.Namespace
_Namespace_ds.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_md = _ImportedBinding__md.Namespace
_Namespace_md.configureCategories(['typeBinding', 'elementBinding'])

def CreateFromDocument (xml_text, default_namespace=None, location_base=None):
    """Parse the given XML and use the document element to create a
    Python instance.

    @param xml_text An XML document.  This should be data (Python 2
    str or Python 3 bytes), or a text (Python 2 unicode or Python 3
    str) in the L{pyxb._InputEncoding} encoding.

    @keyword default_namespace The L{pyxb.Namespace} instance to use as the
    default namespace where there is no default namespace in scope.
    If unspecified or C{None}, the namespace of the module containing
    this function will be used.

    @keyword location_base: An object to be recorded as the base of all
    L{pyxb.utils.utility.Location} instances associated with events and
    objects handled by the parser.  You might pass the URI from which
    the document was obtained.
    """

    if pyxb.XMLStyle_saxer != pyxb._XMLStyle:
        dom = pyxb.utils.domutils.StringToDOM(xml_text)
        return CreateFromDOM(dom.documentElement)
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    saxer = pyxb.binding.saxer.make_parser(fallback_namespace=default_namespace, location_base=location_base)
    handler = saxer.getContentHandler()
    xmld = xml_text
    if isinstance(xmld, unicode):
        xmld = xmld.encode(pyxb._InputEncoding)
    saxer.parse(io.BytesIO(xmld))
    instance = handler.rootObject()
    return instance

def CreateFromDOM (node, default_namespace=None):
    """Create a Python instance from the given DOM node.
    The node tag must correspond to an element declaration in this module.

    @deprecated: Forcing use of DOM interface is unnecessary; use L{CreateFromDocument}."""
    if default_namespace is None:
        default_namespace = Namespace.fallbackNamespace()
    return pyxb.binding.basis.element.AnyCreateFromDOM(node, default_namespace)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}FederationMetadataType with content type ELEMENT_ONLY
class FederationMetadataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}FederationMetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FederationMetadataType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 54, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'FederationMetadataType', FederationMetadataType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}FederationType with content type ELEMENT_ONLY
class FederationType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}FederationType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FederationType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 66, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute FederationID uses Python identifier FederationID
    __FederationID = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'FederationID'), 'FederationID', '__httpdocs_oasis_open_orgwsfedfederation200706_FederationType_FederationID', pyxb.binding.datatypes.anyURI)
    __FederationID._DeclarationLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 70, 1)
    __FederationID._UseLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 70, 1)
    
    FederationID = property(__FederationID.value, __FederationID.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __FederationID.name() : __FederationID
    })
Namespace.addCategoryObject('typeBinding', u'FederationType', FederationType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}LogicalServiceNamesOfferedType with content type ELEMENT_ONLY
class LogicalServiceNamesOfferedType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}LogicalServiceNamesOfferedType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'LogicalServiceNamesOfferedType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 172, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}IssuerName uses Python identifier IssuerName
    __IssuerName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IssuerName'), 'IssuerName', '__httpdocs_oasis_open_orgwsfedfederation200706_LogicalServiceNamesOfferedType_httpdocs_oasis_open_orgwsfedfederation200706IssuerName', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 174, 3), )

    
    IssuerName = property(__IssuerName.value, __IssuerName.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _ElementMap.update({
        __IssuerName.name() : __IssuerName
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'LogicalServiceNamesOfferedType', LogicalServiceNamesOfferedType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}IssuerNameType with content type EMPTY
class IssuerNameType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}IssuerNameType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IssuerNameType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 179, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Uri uses Python identifier Uri
    __Uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Uri'), 'Uri', '__httpdocs_oasis_open_orgwsfedfederation200706_IssuerNameType_Uri', pyxb.binding.datatypes.anyURI, required=True)
    __Uri._DeclarationLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 180, 1)
    __Uri._UseLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 180, 1)
    
    Uri = property(__Uri.value, __Uri.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Uri.name() : __Uri
    })
Namespace.addCategoryObject('typeBinding', u'IssuerNameType', IssuerNameType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}EndpointType with content type ELEMENT_ONLY
class EndpointType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}EndpointType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EndpointType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 186, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/08/addressing}EndpointReference uses Python identifier EndpointReference
    __EndpointReference = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_wsa, u'EndpointReference'), 'EndpointReference', '__httpdocs_oasis_open_orgwsfedfederation200706_EndpointType_httpwww_w3_org200508addressingEndpointReference', True, pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 22, 1), )

    
    EndpointReference = property(__EndpointReference.value, __EndpointReference.set, None, None)

    _ElementMap.update({
        __EndpointReference.name() : __EndpointReference
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'EndpointType', EndpointType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}TokenTypesOfferedType with content type ELEMENT_ONLY
class TokenTypesOfferedType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}TokenTypesOfferedType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TokenTypesOfferedType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 204, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}TokenType uses Python identifier TokenType
    __TokenType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TokenType'), 'TokenType', '__httpdocs_oasis_open_orgwsfedfederation200706_TokenTypesOfferedType_httpdocs_oasis_open_orgwsfedfederation200706TokenType', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 206, 3), )

    
    TokenType = property(__TokenType.value, __TokenType.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        __TokenType.name() : __TokenType
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'TokenTypesOfferedType', TokenTypesOfferedType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}TokenType with content type ELEMENT_ONLY
class TokenType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}TokenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TokenType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 212, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Uri uses Python identifier Uri
    __Uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Uri'), 'Uri', '__httpdocs_oasis_open_orgwsfedfederation200706_TokenType_Uri', pyxb.binding.datatypes.anyURI)
    __Uri._DeclarationLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 216, 1)
    __Uri._UseLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 216, 1)
    
    Uri = property(__Uri.value, __Uri.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Uri.name() : __Uri
    })
Namespace.addCategoryObject('typeBinding', u'TokenType', TokenType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesOfferedType with content type ELEMENT_ONLY
class ClaimTypesOfferedType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesOfferedType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesOfferedType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 223, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ClaimType uses Python identifier ClaimType
    __ClaimType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_auth, u'ClaimType'), 'ClaimType', '__httpdocs_oasis_open_orgwsfedfederation200706_ClaimTypesOfferedType_httpdocs_oasis_open_orgwsfedauthorization200706ClaimType', True, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/wsfed/authorization/v1.2/cd/ws-authorization.xsd', 53, 2), )

    
    ClaimType = property(__ClaimType.value, __ClaimType.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _ElementMap.update({
        __ClaimType.name() : __ClaimType
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ClaimTypesOfferedType', ClaimTypesOfferedType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesRequestedType with content type ELEMENT_ONLY
class ClaimTypesRequestedType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesRequestedType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesRequestedType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 233, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ClaimType uses Python identifier ClaimType
    __ClaimType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_auth, u'ClaimType'), 'ClaimType', '__httpdocs_oasis_open_orgwsfedfederation200706_ClaimTypesRequestedType_httpdocs_oasis_open_orgwsfedauthorization200706ClaimType', True, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/wsfed/authorization/v1.2/cd/ws-authorization.xsd', 53, 2), )

    
    ClaimType = property(__ClaimType.value, __ClaimType.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _ElementMap.update({
        __ClaimType.name() : __ClaimType
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ClaimTypesRequestedType', ClaimTypesRequestedType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ClaimDialectsOfferedType with content type ELEMENT_ONLY
class ClaimDialectsOfferedType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ClaimDialectsOfferedType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ClaimDialectsOfferedType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 243, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}ClaimDialect uses Python identifier ClaimDialect
    __ClaimDialect = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ClaimDialect'), 'ClaimDialect', '__httpdocs_oasis_open_orgwsfedfederation200706_ClaimDialectsOfferedType_httpdocs_oasis_open_orgwsfedfederation200706ClaimDialect', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 245, 6), )

    
    ClaimDialect = property(__ClaimDialect.value, __ClaimDialect.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _ElementMap.update({
        __ClaimDialect.name() : __ClaimDialect
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ClaimDialectsOfferedType', ClaimDialectsOfferedType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ClaimDialectType with content type ELEMENT_ONLY
class ClaimDialectType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ClaimDialectType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ClaimDialectType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 250, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Uri uses Python identifier Uri
    __Uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Uri'), 'Uri', '__httpdocs_oasis_open_orgwsfedfederation200706_ClaimDialectType_Uri', pyxb.binding.datatypes.anyURI)
    __Uri._DeclarationLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 254, 4)
    __Uri._UseLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 254, 4)
    
    Uri = property(__Uri.value, __Uri.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Uri.name() : __Uri
    })
Namespace.addCategoryObject('typeBinding', u'ClaimDialectType', ClaimDialectType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}FederationMetadataHandlerType with content type EMPTY
class FederationMetadataHandlerType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}FederationMetadataHandlerType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FederationMetadataHandlerType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 271, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'FederationMetadataHandlerType', FederationMetadataHandlerType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}SignOutType with content type ELEMENT_ONLY
class SignOutType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}SignOutType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SignOutType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 277, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}SignOutBasis uses Python identifier SignOutBasis
    __SignOutBasis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SignOutBasis'), 'SignOutBasis', '__httpdocs_oasis_open_orgwsfedfederation200706_SignOutType_httpdocs_oasis_open_orgwsfedfederation200706SignOutBasis', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 280, 3), )

    
    SignOutBasis = property(__SignOutBasis.value, __SignOutBasis.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}Realm uses Python identifier Realm
    __Realm = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Realm'), 'Realm', '__httpdocs_oasis_open_orgwsfedfederation200706_SignOutType_httpdocs_oasis_open_orgwsfedfederation200706Realm', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 295, 2), )

    
    Realm = property(__Realm.value, __Realm.set, None, None)

    
    # Attribute {http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd}Id uses Python identifier Id
    __Id = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(_Namespace_wsu, u'Id'), 'Id', '__httpdocs_oasis_open_orgwsfedfederation200706_SignOutType_httpdocs_oasis_open_orgwss200401oasis_200401_wss_wssecurity_utility_1_0_xsdId', pyxb.binding.datatypes.ID)
    __Id._DeclarationLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/wss/2004/01/oasis-200401-wss-wssecurity-utility-1.0.xsd', 28, 1)
    __Id._UseLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 283, 1)
    
    Id = property(__Id.value, __Id.set, None, u'\nThis global attribute supports annotating arbitrary elements with an ID.\n          ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        __SignOutBasis.name() : __SignOutBasis,
        __Realm.name() : __Realm
    })
    _AttributeMap.update({
        __Id.name() : __Id
    })
Namespace.addCategoryObject('typeBinding', u'SignOutType', SignOutType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}SignOutBasisType with content type ELEMENT_ONLY
class SignOutBasisType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}SignOutBasisType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SignOutBasisType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 287, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SignOutBasisType', SignOutBasisType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}FilterPseudonymsType with content type ELEMENT_ONLY
class FilterPseudonymsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}FilterPseudonymsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FilterPseudonymsType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 299, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}PseudonymBasis uses Python identifier PseudonymBasis
    __PseudonymBasis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PseudonymBasis'), 'PseudonymBasis', '__httpdocs_oasis_open_orgwsfedfederation200706_FilterPseudonymsType_httpdocs_oasis_open_orgwsfedfederation200706PseudonymBasis', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 308, 2), )

    
    PseudonymBasis = property(__PseudonymBasis.value, __PseudonymBasis.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}RelativeTo uses Python identifier RelativeTo
    __RelativeTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RelativeTo'), 'RelativeTo', '__httpdocs_oasis_open_orgwsfedfederation200706_FilterPseudonymsType_httpdocs_oasis_open_orgwsfedfederation200706RelativeTo', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 316, 2), )

    
    RelativeTo = property(__RelativeTo.value, __RelativeTo.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        __PseudonymBasis.name() : __PseudonymBasis,
        __RelativeTo.name() : __RelativeTo
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'FilterPseudonymsType', FilterPseudonymsType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}PseudonymBasisType with content type ELEMENT_ONLY
class PseudonymBasisType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}PseudonymBasisType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PseudonymBasisType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 309, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'PseudonymBasisType', PseudonymBasisType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}RelativeToType with content type ELEMENT_ONLY
class RelativeToType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}RelativeToType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RelativeToType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 317, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'RelativeToType', RelativeToType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}PseudonymType with content type ELEMENT_ONLY
class PseudonymType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}PseudonymType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PseudonymType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 327, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}PseudonymBasis uses Python identifier PseudonymBasis
    __PseudonymBasis = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PseudonymBasis'), 'PseudonymBasis', '__httpdocs_oasis_open_orgwsfedfederation200706_PseudonymType_httpdocs_oasis_open_orgwsfedfederation200706PseudonymBasis', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 308, 2), )

    
    PseudonymBasis = property(__PseudonymBasis.value, __PseudonymBasis.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}RelativeTo uses Python identifier RelativeTo
    __RelativeTo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RelativeTo'), 'RelativeTo', '__httpdocs_oasis_open_orgwsfedfederation200706_PseudonymType_httpdocs_oasis_open_orgwsfedfederation200706RelativeTo', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 316, 2), )

    
    RelativeTo = property(__RelativeTo.value, __RelativeTo.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        __PseudonymBasis.name() : __PseudonymBasis,
        __RelativeTo.name() : __RelativeTo
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'PseudonymType', PseudonymType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}SecurityTokenType with content type ELEMENT_ONLY
class SecurityTokenType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}SecurityTokenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SecurityTokenType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 347, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SecurityTokenType', SecurityTokenType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ProofTokenType with content type ELEMENT_ONLY
class ProofTokenType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ProofTokenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ProofTokenType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 355, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ProofTokenType', ProofTokenType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}RequestPseudonymType with content type ELEMENT_ONLY
class RequestPseudonymType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}RequestPseudonymType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RequestPseudonymType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 364, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute SingleUse uses Python identifier SingleUse
    __SingleUse = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'SingleUse'), 'SingleUse', '__httpdocs_oasis_open_orgwsfedfederation200706_RequestPseudonymType_SingleUse', pyxb.binding.datatypes.boolean)
    __SingleUse._DeclarationLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 368, 1)
    __SingleUse._UseLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 368, 1)
    
    SingleUse = property(__SingleUse.value, __SingleUse.set, None, None)

    
    # Attribute Lookup uses Python identifier Lookup
    __Lookup = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Lookup'), 'Lookup', '__httpdocs_oasis_open_orgwsfedfederation200706_RequestPseudonymType_Lookup', pyxb.binding.datatypes.boolean)
    __Lookup._DeclarationLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 369, 1)
    __Lookup._UseLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 369, 1)
    
    Lookup = property(__Lookup.value, __Lookup.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __SingleUse.name() : __SingleUse,
        __Lookup.name() : __Lookup
    })
Namespace.addCategoryObject('typeBinding', u'RequestPseudonymType', RequestPseudonymType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ReferenceTokenType with content type ELEMENT_ONLY
class ReferenceTokenType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ReferenceTokenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReferenceTokenType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 375, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}ReferenceEPR uses Python identifier ReferenceEPR
    __ReferenceEPR = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ReferenceEPR'), 'ReferenceEPR', '__httpdocs_oasis_open_orgwsfedfederation200706_ReferenceTokenType_httpdocs_oasis_open_orgwsfedfederation200706ReferenceEPR', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 377, 3), )

    
    ReferenceEPR = property(__ReferenceEPR.value, __ReferenceEPR.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}ReferenceDigest uses Python identifier ReferenceDigest
    __ReferenceDigest = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ReferenceDigest'), 'ReferenceDigest', '__httpdocs_oasis_open_orgwsfedfederation200706_ReferenceTokenType_httpdocs_oasis_open_orgwsfedfederation200706ReferenceDigest', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 378, 3), )

    
    ReferenceDigest = property(__ReferenceDigest.value, __ReferenceDigest.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}ReferenceType uses Python identifier ReferenceType
    __ReferenceType = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ReferenceType'), 'ReferenceType', '__httpdocs_oasis_open_orgwsfedfederation200706_ReferenceTokenType_httpdocs_oasis_open_orgwsfedfederation200706ReferenceType', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 379, 3), )

    
    ReferenceType = property(__ReferenceType.value, __ReferenceType.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}SerialNo uses Python identifier SerialNo
    __SerialNo = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SerialNo'), 'SerialNo', '__httpdocs_oasis_open_orgwsfedfederation200706_ReferenceTokenType_httpdocs_oasis_open_orgwsfedfederation200706SerialNo', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 380, 3), )

    
    SerialNo = property(__SerialNo.value, __SerialNo.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        __ReferenceEPR.name() : __ReferenceEPR,
        __ReferenceDigest.name() : __ReferenceDigest,
        __ReferenceType.name() : __ReferenceType,
        __SerialNo.name() : __SerialNo
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ReferenceTokenType', ReferenceTokenType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ReferenceDigestType with content type SIMPLE
class ReferenceDigestType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ReferenceDigestType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.base64Binary
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReferenceDigestType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 386, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.base64Binary
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ReferenceDigestType', ReferenceDigestType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}AttributeExtensibleURI with content type SIMPLE
class AttributeExtensibleURI (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}AttributeExtensibleURI with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttributeExtensibleURI')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 393, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AttributeExtensibleURI', AttributeExtensibleURI)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}RequestProofTokenType with content type ELEMENT_ONLY
class RequestProofTokenType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}RequestProofTokenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RequestProofTokenType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 406, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'RequestProofTokenType', RequestProofTokenType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ClientPseudonymType with content type ELEMENT_ONLY
class ClientPseudonymType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ClientPseudonymType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ClientPseudonymType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 415, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}PPID uses Python identifier PPID
    __PPID = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PPID'), 'PPID', '__httpdocs_oasis_open_orgwsfedfederation200706_ClientPseudonymType_httpdocs_oasis_open_orgwsfedfederation200706PPID', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 417, 3), )

    
    PPID = property(__PPID.value, __PPID.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}DisplayName uses Python identifier DisplayName
    __DisplayName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DisplayName'), 'DisplayName', '__httpdocs_oasis_open_orgwsfedfederation200706_ClientPseudonymType_httpdocs_oasis_open_orgwsfedfederation200706DisplayName', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 418, 3), )

    
    DisplayName = property(__DisplayName.value, __DisplayName.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}EMail uses Python identifier EMail
    __EMail = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EMail'), 'EMail', '__httpdocs_oasis_open_orgwsfedfederation200706_ClientPseudonymType_httpdocs_oasis_open_orgwsfedfederation200706EMail', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 419, 3), )

    
    EMail = property(__EMail.value, __EMail.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        __PPID.name() : __PPID,
        __DisplayName.name() : __DisplayName,
        __EMail.name() : __EMail
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ClientPseudonymType', ClientPseudonymType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}AttributeExtensibleString with content type SIMPLE
class AttributeExtensibleString (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}AttributeExtensibleString with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttributeExtensibleString')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 425, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AttributeExtensibleString', AttributeExtensibleString)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}Freshness with content type SIMPLE
class Freshness_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}Freshness with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.unsignedInt
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'Freshness')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 435, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.unsignedInt
    
    # Attribute AllowCache uses Python identifier AllowCache
    __AllowCache = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'AllowCache'), 'AllowCache', '__httpdocs_oasis_open_orgwsfedfederation200706_Freshness__AllowCache', pyxb.binding.datatypes.boolean)
    __AllowCache._DeclarationLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 438, 2)
    __AllowCache._UseLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 438, 2)
    
    AllowCache = property(__AllowCache.value, __AllowCache.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __AllowCache.name() : __AllowCache
    })
Namespace.addCategoryObject('typeBinding', u'Freshness', Freshness_)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}AssertionType with content type ELEMENT_ONLY
class AssertionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}AssertionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AssertionType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 448, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AssertionType', AssertionType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType with content type ELEMENT_ONLY
class WebServiceDescriptorType (_ImportedBinding__md.RoleDescriptorType):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = True
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'WebServiceDescriptorType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 75, 2)
    _ElementMap = _ImportedBinding__md.RoleDescriptorType._ElementMap.copy()
    _AttributeMap = _ImportedBinding__md.RoleDescriptorType._AttributeMap.copy()
    # Base type is _ImportedBinding__md.RoleDescriptorType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}LogicalServiceNamesOffered uses Python identifier LogicalServiceNamesOffered
    __LogicalServiceNamesOffered = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'LogicalServiceNamesOffered'), 'LogicalServiceNamesOffered', '__httpdocs_oasis_open_orgwsfedfederation200706_WebServiceDescriptorType_httpdocs_oasis_open_orgwsfedfederation200706LogicalServiceNamesOffered', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 93, 2), )

    
    LogicalServiceNamesOffered = property(__LogicalServiceNamesOffered.value, __LogicalServiceNamesOffered.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}TokenTypesOffered uses Python identifier TokenTypesOffered
    __TokenTypesOffered = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TokenTypesOffered'), 'TokenTypesOffered', '__httpdocs_oasis_open_orgwsfedfederation200706_WebServiceDescriptorType_httpdocs_oasis_open_orgwsfedfederation200706TokenTypesOffered', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 94, 2), )

    
    TokenTypesOffered = property(__TokenTypesOffered.value, __TokenTypesOffered.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}ClaimDialectsOffered uses Python identifier ClaimDialectsOffered
    __ClaimDialectsOffered = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ClaimDialectsOffered'), 'ClaimDialectsOffered', '__httpdocs_oasis_open_orgwsfedfederation200706_WebServiceDescriptorType_httpdocs_oasis_open_orgwsfedfederation200706ClaimDialectsOffered', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 95, 2), )

    
    ClaimDialectsOffered = property(__ClaimDialectsOffered.value, __ClaimDialectsOffered.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesOffered uses Python identifier ClaimTypesOffered
    __ClaimTypesOffered = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesOffered'), 'ClaimTypesOffered', '__httpdocs_oasis_open_orgwsfedfederation200706_WebServiceDescriptorType_httpdocs_oasis_open_orgwsfedfederation200706ClaimTypesOffered', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 96, 2), )

    
    ClaimTypesOffered = property(__ClaimTypesOffered.value, __ClaimTypesOffered.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesRequested uses Python identifier ClaimTypesRequested
    __ClaimTypesRequested = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesRequested'), 'ClaimTypesRequested', '__httpdocs_oasis_open_orgwsfedfederation200706_WebServiceDescriptorType_httpdocs_oasis_open_orgwsfedfederation200706ClaimTypesRequested', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 97, 2), )

    
    ClaimTypesRequested = property(__ClaimTypesRequested.value, __ClaimTypesRequested.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}AutomaticPseudonyms uses Python identifier AutomaticPseudonyms
    __AutomaticPseudonyms = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AutomaticPseudonyms'), 'AutomaticPseudonyms', '__httpdocs_oasis_open_orgwsfedfederation200706_WebServiceDescriptorType_httpdocs_oasis_open_orgwsfedfederation200706AutomaticPseudonyms', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 98, 2), )

    
    AutomaticPseudonyms = property(__AutomaticPseudonyms.value, __AutomaticPseudonyms.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}TargetScopes uses Python identifier TargetScopes
    __TargetScopes = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'TargetScopes'), 'TargetScopes', '__httpdocs_oasis_open_orgwsfedfederation200706_WebServiceDescriptorType_httpdocs_oasis_open_orgwsfedfederation200706TargetScopes', False, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 99, 2), )

    
    TargetScopes = property(__TargetScopes.value, __TargetScopes.set, None, None)

    
    # Element Signature ({http://www.w3.org/2000/09/xmldsig#}Signature) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element Extensions ({urn:oasis:names:tc:SAML:2.0:metadata}Extensions) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element Organization ({urn:oasis:names:tc:SAML:2.0:metadata}Organization) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element ContactPerson ({urn:oasis:names:tc:SAML:2.0:metadata}ContactPerson) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element KeyDescriptor ({urn:oasis:names:tc:SAML:2.0:metadata}KeyDescriptor) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute ServiceDisplayName uses Python identifier ServiceDisplayName
    __ServiceDisplayName = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ServiceDisplayName'), 'ServiceDisplayName', '__httpdocs_oasis_open_orgwsfedfederation200706_WebServiceDescriptorType_ServiceDisplayName', pyxb.binding.datatypes.string)
    __ServiceDisplayName._DeclarationLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 87, 8)
    __ServiceDisplayName._UseLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 87, 8)
    
    ServiceDisplayName = property(__ServiceDisplayName.value, __ServiceDisplayName.set, None, None)

    
    # Attribute ServiceDescription uses Python identifier ServiceDescription
    __ServiceDescription = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'ServiceDescription'), 'ServiceDescription', '__httpdocs_oasis_open_orgwsfedfederation200706_WebServiceDescriptorType_ServiceDescription', pyxb.binding.datatypes.string)
    __ServiceDescription._DeclarationLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 88, 8)
    __ServiceDescription._UseLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 88, 8)
    
    ServiceDescription = property(__ServiceDescription.value, __ServiceDescription.set, None, None)

    
    # Attribute ID inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute validUntil inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute cacheDuration inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute protocolSupportEnumeration inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute errorURL inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'urn:oasis:names:tc:SAML:2.0:metadata'))
    _ElementMap.update({
        __LogicalServiceNamesOffered.name() : __LogicalServiceNamesOffered,
        __TokenTypesOffered.name() : __TokenTypesOffered,
        __ClaimDialectsOffered.name() : __ClaimDialectsOffered,
        __ClaimTypesOffered.name() : __ClaimTypesOffered,
        __ClaimTypesRequested.name() : __ClaimTypesRequested,
        __AutomaticPseudonyms.name() : __AutomaticPseudonyms,
        __TargetScopes.name() : __TargetScopes
    })
    _AttributeMap.update({
        __ServiceDisplayName.name() : __ServiceDisplayName,
        __ServiceDescription.name() : __ServiceDescription
    })
Namespace.addCategoryObject('typeBinding', u'WebServiceDescriptorType', WebServiceDescriptorType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}SecurityTokenServiceType with content type ELEMENT_ONLY
class SecurityTokenServiceType (WebServiceDescriptorType):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}SecurityTokenServiceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SecurityTokenServiceType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 102, 2)
    _ElementMap = WebServiceDescriptorType._ElementMap.copy()
    _AttributeMap = WebServiceDescriptorType._AttributeMap.copy()
    # Base type is WebServiceDescriptorType
    
    # Element LogicalServiceNamesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}LogicalServiceNamesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element TokenTypesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}TokenTypesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimDialectsOffered ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimDialectsOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimTypesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimTypesRequested ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesRequested) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element AutomaticPseudonyms ({http://docs.oasis-open.org/wsfed/federation/200706}AutomaticPseudonyms) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element TargetScopes ({http://docs.oasis-open.org/wsfed/federation/200706}TargetScopes) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}SecurityTokenServiceEndpoint uses Python identifier SecurityTokenServiceEndpoint
    __SecurityTokenServiceEndpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SecurityTokenServiceEndpoint'), 'SecurityTokenServiceEndpoint', '__httpdocs_oasis_open_orgwsfedfederation200706_SecurityTokenServiceType_httpdocs_oasis_open_orgwsfedfederation200706SecurityTokenServiceEndpoint', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 114, 2), )

    
    SecurityTokenServiceEndpoint = property(__SecurityTokenServiceEndpoint.value, __SecurityTokenServiceEndpoint.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}SingleSignOutSubscriptionEndpoint uses Python identifier SingleSignOutSubscriptionEndpoint
    __SingleSignOutSubscriptionEndpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutSubscriptionEndpoint'), 'SingleSignOutSubscriptionEndpoint', '__httpdocs_oasis_open_orgwsfedfederation200706_SecurityTokenServiceType_httpdocs_oasis_open_orgwsfedfederation200706SingleSignOutSubscriptionEndpoint', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 115, 2), )

    
    SingleSignOutSubscriptionEndpoint = property(__SingleSignOutSubscriptionEndpoint.value, __SingleSignOutSubscriptionEndpoint.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}SingleSignOutNotificationEndpoint uses Python identifier SingleSignOutNotificationEndpoint
    __SingleSignOutNotificationEndpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint'), 'SingleSignOutNotificationEndpoint', '__httpdocs_oasis_open_orgwsfedfederation200706_SecurityTokenServiceType_httpdocs_oasis_open_orgwsfedfederation200706SingleSignOutNotificationEndpoint', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 116, 2), )

    
    SingleSignOutNotificationEndpoint = property(__SingleSignOutNotificationEndpoint.value, __SingleSignOutNotificationEndpoint.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}PassiveRequestorEndpoint uses Python identifier PassiveRequestorEndpoint
    __PassiveRequestorEndpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PassiveRequestorEndpoint'), 'PassiveRequestorEndpoint', '__httpdocs_oasis_open_orgwsfedfederation200706_SecurityTokenServiceType_httpdocs_oasis_open_orgwsfedfederation200706PassiveRequestorEndpoint', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 117, 2), )

    
    PassiveRequestorEndpoint = property(__PassiveRequestorEndpoint.value, __PassiveRequestorEndpoint.set, None, None)

    
    # Element Signature ({http://www.w3.org/2000/09/xmldsig#}Signature) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element Extensions ({urn:oasis:names:tc:SAML:2.0:metadata}Extensions) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element Organization ({urn:oasis:names:tc:SAML:2.0:metadata}Organization) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element ContactPerson ({urn:oasis:names:tc:SAML:2.0:metadata}ContactPerson) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element KeyDescriptor ({urn:oasis:names:tc:SAML:2.0:metadata}KeyDescriptor) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute ServiceDisplayName inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Attribute ServiceDescription inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Attribute ID inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute validUntil inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute cacheDuration inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute protocolSupportEnumeration inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute errorURL inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'urn:oasis:names:tc:SAML:2.0:metadata'))
    _ElementMap.update({
        __SecurityTokenServiceEndpoint.name() : __SecurityTokenServiceEndpoint,
        __SingleSignOutSubscriptionEndpoint.name() : __SingleSignOutSubscriptionEndpoint,
        __SingleSignOutNotificationEndpoint.name() : __SingleSignOutNotificationEndpoint,
        __PassiveRequestorEndpoint.name() : __PassiveRequestorEndpoint
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SecurityTokenServiceType', SecurityTokenServiceType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}PseudonymServiceType with content type ELEMENT_ONLY
class PseudonymServiceType (WebServiceDescriptorType):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}PseudonymServiceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'PseudonymServiceType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 120, 2)
    _ElementMap = WebServiceDescriptorType._ElementMap.copy()
    _AttributeMap = WebServiceDescriptorType._AttributeMap.copy()
    # Base type is WebServiceDescriptorType
    
    # Element LogicalServiceNamesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}LogicalServiceNamesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element TokenTypesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}TokenTypesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimDialectsOffered ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimDialectsOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimTypesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimTypesRequested ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesRequested) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element AutomaticPseudonyms ({http://docs.oasis-open.org/wsfed/federation/200706}AutomaticPseudonyms) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element TargetScopes ({http://docs.oasis-open.org/wsfed/federation/200706}TargetScopes) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}SingleSignOutNotificationEndpoint uses Python identifier SingleSignOutNotificationEndpoint
    __SingleSignOutNotificationEndpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint'), 'SingleSignOutNotificationEndpoint', '__httpdocs_oasis_open_orgwsfedfederation200706_PseudonymServiceType_httpdocs_oasis_open_orgwsfedfederation200706SingleSignOutNotificationEndpoint', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 116, 2), )

    
    SingleSignOutNotificationEndpoint = property(__SingleSignOutNotificationEndpoint.value, __SingleSignOutNotificationEndpoint.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}PseudonymServiceEndpoint uses Python identifier PseudonymServiceEndpoint
    __PseudonymServiceEndpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PseudonymServiceEndpoint'), 'PseudonymServiceEndpoint', '__httpdocs_oasis_open_orgwsfedfederation200706_PseudonymServiceType_httpdocs_oasis_open_orgwsfedfederation200706PseudonymServiceEndpoint', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 131, 2), )

    
    PseudonymServiceEndpoint = property(__PseudonymServiceEndpoint.value, __PseudonymServiceEndpoint.set, None, None)

    
    # Element Signature ({http://www.w3.org/2000/09/xmldsig#}Signature) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element Extensions ({urn:oasis:names:tc:SAML:2.0:metadata}Extensions) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element Organization ({urn:oasis:names:tc:SAML:2.0:metadata}Organization) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element ContactPerson ({urn:oasis:names:tc:SAML:2.0:metadata}ContactPerson) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element KeyDescriptor ({urn:oasis:names:tc:SAML:2.0:metadata}KeyDescriptor) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute ServiceDisplayName inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Attribute ServiceDescription inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Attribute ID inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute validUntil inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute cacheDuration inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute protocolSupportEnumeration inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute errorURL inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'urn:oasis:names:tc:SAML:2.0:metadata'))
    _ElementMap.update({
        __SingleSignOutNotificationEndpoint.name() : __SingleSignOutNotificationEndpoint,
        __PseudonymServiceEndpoint.name() : __PseudonymServiceEndpoint
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'PseudonymServiceType', PseudonymServiceType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}AttributeServiceType with content type ELEMENT_ONLY
class AttributeServiceType (WebServiceDescriptorType):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}AttributeServiceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttributeServiceType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 136, 2)
    _ElementMap = WebServiceDescriptorType._ElementMap.copy()
    _AttributeMap = WebServiceDescriptorType._AttributeMap.copy()
    # Base type is WebServiceDescriptorType
    
    # Element LogicalServiceNamesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}LogicalServiceNamesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element TokenTypesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}TokenTypesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimDialectsOffered ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimDialectsOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimTypesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimTypesRequested ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesRequested) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element AutomaticPseudonyms ({http://docs.oasis-open.org/wsfed/federation/200706}AutomaticPseudonyms) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element TargetScopes ({http://docs.oasis-open.org/wsfed/federation/200706}TargetScopes) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}SingleSignOutNotificationEndpoint uses Python identifier SingleSignOutNotificationEndpoint
    __SingleSignOutNotificationEndpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint'), 'SingleSignOutNotificationEndpoint', '__httpdocs_oasis_open_orgwsfedfederation200706_AttributeServiceType_httpdocs_oasis_open_orgwsfedfederation200706SingleSignOutNotificationEndpoint', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 116, 2), )

    
    SingleSignOutNotificationEndpoint = property(__SingleSignOutNotificationEndpoint.value, __SingleSignOutNotificationEndpoint.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}AttributeServiceEndpoint uses Python identifier AttributeServiceEndpoint
    __AttributeServiceEndpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'AttributeServiceEndpoint'), 'AttributeServiceEndpoint', '__httpdocs_oasis_open_orgwsfedfederation200706_AttributeServiceType_httpdocs_oasis_open_orgwsfedfederation200706AttributeServiceEndpoint', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 146, 2), )

    
    AttributeServiceEndpoint = property(__AttributeServiceEndpoint.value, __AttributeServiceEndpoint.set, None, None)

    
    # Element Signature ({http://www.w3.org/2000/09/xmldsig#}Signature) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element Extensions ({urn:oasis:names:tc:SAML:2.0:metadata}Extensions) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element Organization ({urn:oasis:names:tc:SAML:2.0:metadata}Organization) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element ContactPerson ({urn:oasis:names:tc:SAML:2.0:metadata}ContactPerson) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element KeyDescriptor ({urn:oasis:names:tc:SAML:2.0:metadata}KeyDescriptor) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute ServiceDisplayName inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Attribute ServiceDescription inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Attribute ID inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute validUntil inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute cacheDuration inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute protocolSupportEnumeration inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute errorURL inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'urn:oasis:names:tc:SAML:2.0:metadata'))
    _ElementMap.update({
        __SingleSignOutNotificationEndpoint.name() : __SingleSignOutNotificationEndpoint,
        __AttributeServiceEndpoint.name() : __AttributeServiceEndpoint
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AttributeServiceType', AttributeServiceType)


# Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ApplicationServiceType with content type ELEMENT_ONLY
class ApplicationServiceType (WebServiceDescriptorType):
    """Complex type {http://docs.oasis-open.org/wsfed/federation/200706}ApplicationServiceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ApplicationServiceType')
    _XSDLocation = pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 151, 2)
    _ElementMap = WebServiceDescriptorType._ElementMap.copy()
    _AttributeMap = WebServiceDescriptorType._AttributeMap.copy()
    # Base type is WebServiceDescriptorType
    
    # Element LogicalServiceNamesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}LogicalServiceNamesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element TokenTypesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}TokenTypesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimDialectsOffered ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimDialectsOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimTypesOffered ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesOffered) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element ClaimTypesRequested ({http://docs.oasis-open.org/wsfed/federation/200706}ClaimTypesRequested) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element AutomaticPseudonyms ({http://docs.oasis-open.org/wsfed/federation/200706}AutomaticPseudonyms) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element TargetScopes ({http://docs.oasis-open.org/wsfed/federation/200706}TargetScopes) inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}SingleSignOutNotificationEndpoint uses Python identifier SingleSignOutNotificationEndpoint
    __SingleSignOutNotificationEndpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint'), 'SingleSignOutNotificationEndpoint', '__httpdocs_oasis_open_orgwsfedfederation200706_ApplicationServiceType_httpdocs_oasis_open_orgwsfedfederation200706SingleSignOutNotificationEndpoint', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 116, 2), )

    
    SingleSignOutNotificationEndpoint = property(__SingleSignOutNotificationEndpoint.value, __SingleSignOutNotificationEndpoint.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}PassiveRequestorEndpoint uses Python identifier PassiveRequestorEndpoint
    __PassiveRequestorEndpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'PassiveRequestorEndpoint'), 'PassiveRequestorEndpoint', '__httpdocs_oasis_open_orgwsfedfederation200706_ApplicationServiceType_httpdocs_oasis_open_orgwsfedfederation200706PassiveRequestorEndpoint', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 117, 2), )

    
    PassiveRequestorEndpoint = property(__PassiveRequestorEndpoint.value, __PassiveRequestorEndpoint.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/federation/200706}ApplicationServiceEndpoint uses Python identifier ApplicationServiceEndpoint
    __ApplicationServiceEndpoint = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ApplicationServiceEndpoint'), 'ApplicationServiceEndpoint', '__httpdocs_oasis_open_orgwsfedfederation200706_ApplicationServiceType_httpdocs_oasis_open_orgwsfedfederation200706ApplicationServiceEndpoint', True, pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 162, 2), )

    
    ApplicationServiceEndpoint = property(__ApplicationServiceEndpoint.value, __ApplicationServiceEndpoint.set, None, None)

    
    # Element Signature ({http://www.w3.org/2000/09/xmldsig#}Signature) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element Extensions ({urn:oasis:names:tc:SAML:2.0:metadata}Extensions) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element Organization ({urn:oasis:names:tc:SAML:2.0:metadata}Organization) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element ContactPerson ({urn:oasis:names:tc:SAML:2.0:metadata}ContactPerson) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Element KeyDescriptor ({urn:oasis:names:tc:SAML:2.0:metadata}KeyDescriptor) inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute ServiceDisplayName inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Attribute ServiceDescription inherited from {http://docs.oasis-open.org/wsfed/federation/200706}WebServiceDescriptorType
    
    # Attribute ID inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute validUntil inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute cacheDuration inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute protocolSupportEnumeration inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    
    # Attribute errorURL inherited from {urn:oasis:names:tc:SAML:2.0:metadata}RoleDescriptorType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'urn:oasis:names:tc:SAML:2.0:metadata'))
    _ElementMap.update({
        __SingleSignOutNotificationEndpoint.name() : __SingleSignOutNotificationEndpoint,
        __PassiveRequestorEndpoint.name() : __PassiveRequestorEndpoint,
        __ApplicationServiceEndpoint.name() : __ApplicationServiceEndpoint
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ApplicationServiceType', ApplicationServiceType)


AutomaticPseudonyms = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AutomaticPseudonyms'), pyxb.binding.datatypes.boolean, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 98, 2))
Namespace.addCategoryObject('elementBinding', AutomaticPseudonyms.name().localName(), AutomaticPseudonyms)

Realm = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Realm'), pyxb.binding.datatypes.anyURI, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 295, 2))
Namespace.addCategoryObject('elementBinding', Realm.name().localName(), Realm)

FederationMetadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FederationMetadata'), FederationMetadataType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 52, 2))
Namespace.addCategoryObject('elementBinding', FederationMetadata.name().localName(), FederationMetadata)

LogicalServiceNamesOffered = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LogicalServiceNamesOffered'), LogicalServiceNamesOfferedType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 93, 2))
Namespace.addCategoryObject('elementBinding', LogicalServiceNamesOffered.name().localName(), LogicalServiceNamesOffered)

TokenTypesOffered = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TokenTypesOffered'), TokenTypesOfferedType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 94, 2))
Namespace.addCategoryObject('elementBinding', TokenTypesOffered.name().localName(), TokenTypesOffered)

ClaimDialectsOffered = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClaimDialectsOffered'), ClaimDialectsOfferedType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 95, 2))
Namespace.addCategoryObject('elementBinding', ClaimDialectsOffered.name().localName(), ClaimDialectsOffered)

ClaimTypesOffered = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesOffered'), ClaimTypesOfferedType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 96, 2))
Namespace.addCategoryObject('elementBinding', ClaimTypesOffered.name().localName(), ClaimTypesOffered)

ClaimTypesRequested = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesRequested'), ClaimTypesRequestedType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 97, 2))
Namespace.addCategoryObject('elementBinding', ClaimTypesRequested.name().localName(), ClaimTypesRequested)

TargetScopes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TargetScopes'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 99, 2))
Namespace.addCategoryObject('elementBinding', TargetScopes.name().localName(), TargetScopes)

SecurityTokenServiceEndpoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SecurityTokenServiceEndpoint'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 114, 2))
Namespace.addCategoryObject('elementBinding', SecurityTokenServiceEndpoint.name().localName(), SecurityTokenServiceEndpoint)

SingleSignOutSubscriptionEndpoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutSubscriptionEndpoint'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 115, 2))
Namespace.addCategoryObject('elementBinding', SingleSignOutSubscriptionEndpoint.name().localName(), SingleSignOutSubscriptionEndpoint)

SingleSignOutNotificationEndpoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 116, 2))
Namespace.addCategoryObject('elementBinding', SingleSignOutNotificationEndpoint.name().localName(), SingleSignOutNotificationEndpoint)

PassiveRequestorEndpoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PassiveRequestorEndpoint'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 117, 2))
Namespace.addCategoryObject('elementBinding', PassiveRequestorEndpoint.name().localName(), PassiveRequestorEndpoint)

PseudonymServiceEndpoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PseudonymServiceEndpoint'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 131, 2))
Namespace.addCategoryObject('elementBinding', PseudonymServiceEndpoint.name().localName(), PseudonymServiceEndpoint)

AttributeServiceEndpoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AttributeServiceEndpoint'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 146, 2))
Namespace.addCategoryObject('elementBinding', AttributeServiceEndpoint.name().localName(), AttributeServiceEndpoint)

ApplicationServiceEndpoint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ApplicationServiceEndpoint'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 162, 2))
Namespace.addCategoryObject('elementBinding', ApplicationServiceEndpoint.name().localName(), ApplicationServiceEndpoint)

PsuedonymServiceEndpoints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PsuedonymServiceEndpoints'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 185, 2))
Namespace.addCategoryObject('elementBinding', PsuedonymServiceEndpoints.name().localName(), PsuedonymServiceEndpoints)

AttributeServiceEndpoints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AttributeServiceEndpoints'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 193, 2))
Namespace.addCategoryObject('elementBinding', AttributeServiceEndpoints.name().localName(), AttributeServiceEndpoints)

SingleSignOutSubscriptionEndpoints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutSubscriptionEndpoints'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 196, 2))
Namespace.addCategoryObject('elementBinding', SingleSignOutSubscriptionEndpoints.name().localName(), SingleSignOutSubscriptionEndpoints)

SingleSignOutNotificationEndpoints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoints'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 199, 2))
Namespace.addCategoryObject('elementBinding', SingleSignOutNotificationEndpoints.name().localName(), SingleSignOutNotificationEndpoints)

PassiveRequestorEnpoints = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PassiveRequestorEnpoints'), EndpointType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 263, 2))
Namespace.addCategoryObject('elementBinding', PassiveRequestorEnpoints.name().localName(), PassiveRequestorEnpoints)

FederationMetadataHandler = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FederationMetadataHandler'), FederationMetadataHandlerType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 270, 2))
Namespace.addCategoryObject('elementBinding', FederationMetadataHandler.name().localName(), FederationMetadataHandler)

SignOut = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignOut'), SignOutType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 276, 2))
Namespace.addCategoryObject('elementBinding', SignOut.name().localName(), SignOut)

FilterPseudonyms = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FilterPseudonyms'), FilterPseudonymsType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 298, 2))
Namespace.addCategoryObject('elementBinding', FilterPseudonyms.name().localName(), FilterPseudonyms)

PseudonymBasis = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PseudonymBasis'), PseudonymBasisType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 308, 2))
Namespace.addCategoryObject('elementBinding', PseudonymBasis.name().localName(), PseudonymBasis)

RelativeTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelativeTo'), RelativeToType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 316, 2))
Namespace.addCategoryObject('elementBinding', RelativeTo.name().localName(), RelativeTo)

Pseudonym = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Pseudonym'), PseudonymType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 325, 2))
Namespace.addCategoryObject('elementBinding', Pseudonym.name().localName(), Pseudonym)

SecurityToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SecurityToken'), SecurityTokenType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 346, 2))
Namespace.addCategoryObject('elementBinding', SecurityToken.name().localName(), SecurityToken)

ProofToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProofToken'), ProofTokenType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 354, 2))
Namespace.addCategoryObject('elementBinding', ProofToken.name().localName(), ProofToken)

RequestPseudonym = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequestPseudonym'), RequestPseudonymType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 363, 2))
Namespace.addCategoryObject('elementBinding', RequestPseudonym.name().localName(), RequestPseudonym)

ReferenceToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceToken'), ReferenceTokenType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 374, 2))
Namespace.addCategoryObject('elementBinding', ReferenceToken.name().localName(), ReferenceToken)

FederationID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FederationID'), AttributeExtensibleURI, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 402, 2))
Namespace.addCategoryObject('elementBinding', FederationID.name().localName(), FederationID)

RequestProofToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequestProofToken'), RequestProofTokenType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 405, 2))
Namespace.addCategoryObject('elementBinding', RequestProofToken.name().localName(), RequestProofToken)

ClientPseudonym = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClientPseudonym'), ClientPseudonymType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 414, 2))
Namespace.addCategoryObject('elementBinding', ClientPseudonym.name().localName(), ClientPseudonym)

Freshness = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Freshness'), Freshness_, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 434, 2))
Namespace.addCategoryObject('elementBinding', Freshness.name().localName(), Freshness)

ReferenceToken11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceToken11'), AssertionType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 446, 2))
Namespace.addCategoryObject('elementBinding', ReferenceToken11.name().localName(), ReferenceToken11)

WebBinding = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WebBinding'), _ImportedBinding__sp.NestedPolicyType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 456, 2))
Namespace.addCategoryObject('elementBinding', WebBinding.name().localName(), WebBinding)

AuthenticationToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AuthenticationToken'), _ImportedBinding__sp.NestedPolicyType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 457, 2))
Namespace.addCategoryObject('elementBinding', AuthenticationToken.name().localName(), AuthenticationToken)

RequireSignedTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireSignedTokens'), AssertionType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 459, 2))
Namespace.addCategoryObject('elementBinding', RequireSignedTokens.name().localName(), RequireSignedTokens)

RequireBearerTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireBearerTokens'), AssertionType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 460, 2))
Namespace.addCategoryObject('elementBinding', RequireBearerTokens.name().localName(), RequireBearerTokens)

RequireSharedCookies = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireSharedCookies'), AssertionType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 461, 2))
Namespace.addCategoryObject('elementBinding', RequireSharedCookies.name().localName(), RequireSharedCookies)

RequiresGenericClaimDialect = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequiresGenericClaimDialect'), AssertionType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 465, 2))
Namespace.addCategoryObject('elementBinding', RequiresGenericClaimDialect.name().localName(), RequiresGenericClaimDialect)

IssuesSpecificPolicyFault = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IssuesSpecificPolicyFault'), AssertionType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 466, 2))
Namespace.addCategoryObject('elementBinding', IssuesSpecificPolicyFault.name().localName(), IssuesSpecificPolicyFault)

AdditionalContextProcessed = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalContextProcessed'), AssertionType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 467, 2))
Namespace.addCategoryObject('elementBinding', AdditionalContextProcessed.name().localName(), AdditionalContextProcessed)

RequireReferenceToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireReferenceToken'), _ImportedBinding__sp.TokenAssertionType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 445, 2))
Namespace.addCategoryObject('elementBinding', RequireReferenceToken.name().localName(), RequireReferenceToken)



def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 61, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 61, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FederationMetadataType._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 68, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 68, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FederationType._Automaton = _BuildAutomaton_()




LogicalServiceNamesOfferedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IssuerName'), IssuerNameType, scope=LogicalServiceNamesOfferedType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 174, 3)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(LogicalServiceNamesOfferedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IssuerName')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 174, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
LogicalServiceNamesOfferedType._Automaton = _BuildAutomaton_2()




EndpointType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_wsa, u'EndpointReference'), _ImportedBinding__wsa.EndpointReferenceType, scope=EndpointType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 22, 1)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EndpointType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_wsa, u'EndpointReference')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 188, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EndpointType._Automaton = _BuildAutomaton_3()




TokenTypesOfferedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TokenType'), TokenType, scope=TokenTypesOfferedType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 206, 3)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 207, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(TokenTypesOfferedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TokenType')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 206, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 207, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
TokenTypesOfferedType._Automaton = _BuildAutomaton_4()




def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 214, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 214, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TokenType._Automaton = _BuildAutomaton_5()




ClaimTypesOfferedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_auth, u'ClaimType'), _ImportedBinding__auth.ClaimType_, scope=ClaimTypesOfferedType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/wsfed/authorization/v1.2/cd/ws-authorization.xsd', 53, 2)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClaimTypesOfferedType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_auth, u'ClaimType')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 225, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ClaimTypesOfferedType._Automaton = _BuildAutomaton_6()




ClaimTypesRequestedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_auth, u'ClaimType'), _ImportedBinding__auth.ClaimType_, scope=ClaimTypesRequestedType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/wsfed/authorization/v1.2/cd/ws-authorization.xsd', 53, 2)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClaimTypesRequestedType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_auth, u'ClaimType')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 235, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ClaimTypesRequestedType._Automaton = _BuildAutomaton_7()




ClaimDialectsOfferedType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClaimDialect'), ClaimDialectType, scope=ClaimDialectsOfferedType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 245, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ClaimDialectsOfferedType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimDialect')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 245, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ClaimDialectsOfferedType._Automaton = _BuildAutomaton_8()




def _BuildAutomaton_9 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_9
    del _BuildAutomaton_9
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 252, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 252, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ClaimDialectType._Automaton = _BuildAutomaton_9()




SignOutType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignOutBasis'), SignOutBasisType, scope=SignOutType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 280, 3)))

SignOutType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Realm'), pyxb.binding.datatypes.anyURI, scope=SignOutType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 295, 2)))

def _BuildAutomaton_10 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_10
    del _BuildAutomaton_10
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 279, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 281, 3))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SignOutType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Realm')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 279, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SignOutType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SignOutBasis')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 280, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 281, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SignOutType._Automaton = _BuildAutomaton_10()




def _BuildAutomaton_11 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_11
    del _BuildAutomaton_11
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 289, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SignOutBasisType._Automaton = _BuildAutomaton_11()




FilterPseudonymsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PseudonymBasis'), PseudonymBasisType, scope=FilterPseudonymsType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 308, 2)))

FilterPseudonymsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelativeTo'), RelativeToType, scope=FilterPseudonymsType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 316, 2)))

def _BuildAutomaton_12 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_12
    del _BuildAutomaton_12
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 301, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 302, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 303, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(FilterPseudonymsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PseudonymBasis')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 301, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(FilterPseudonymsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RelativeTo')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 302, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_strict, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 303, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
FilterPseudonymsType._Automaton = _BuildAutomaton_12()




def _BuildAutomaton_13 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_13
    del _BuildAutomaton_13
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 311, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PseudonymBasisType._Automaton = _BuildAutomaton_13()




def _BuildAutomaton_14 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_14
    del _BuildAutomaton_14
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 319, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 319, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RelativeToType._Automaton = _BuildAutomaton_14()




PseudonymType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PseudonymBasis'), PseudonymBasisType, scope=PseudonymType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 308, 2)))

PseudonymType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelativeTo'), RelativeToType, scope=PseudonymType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 316, 2)))

def _BuildAutomaton_15 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_15
    del _BuildAutomaton_15
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 341, 3))
    counters.add(cc_0)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PseudonymBasis')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 339, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PseudonymType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RelativeTo')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 340, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 341, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PseudonymType._Automaton = _BuildAutomaton_15()




def _BuildAutomaton_16 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_16
    del _BuildAutomaton_16
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 349, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SecurityTokenType._Automaton = _BuildAutomaton_16()




def _BuildAutomaton_17 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_17
    del _BuildAutomaton_17
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 357, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ProofTokenType._Automaton = _BuildAutomaton_17()




def _BuildAutomaton_18 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_18
    del _BuildAutomaton_18
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 366, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 366, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RequestPseudonymType._Automaton = _BuildAutomaton_18()




ReferenceTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceEPR'), _ImportedBinding__wsa.EndpointReferenceType, scope=ReferenceTokenType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 377, 3)))

ReferenceTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceDigest'), ReferenceDigestType, scope=ReferenceTokenType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 378, 3)))

ReferenceTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceType'), AttributeExtensibleURI, scope=ReferenceTokenType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 379, 3)))

ReferenceTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SerialNo'), AttributeExtensibleURI, scope=ReferenceTokenType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 380, 3)))

def _BuildAutomaton_19 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_19
    del _BuildAutomaton_19
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 378, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 379, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 380, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 381, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ReferenceTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceEPR')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 377, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceDigest')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 378, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceType')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 379, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ReferenceTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SerialNo')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 380, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 381, 3))
    st_4 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    transitions.append(fac.Transition(st_4, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ReferenceTokenType._Automaton = _BuildAutomaton_19()




def _BuildAutomaton_20 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_20
    del _BuildAutomaton_20
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 408, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 408, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RequestProofTokenType._Automaton = _BuildAutomaton_20()




ClientPseudonymType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PPID'), AttributeExtensibleString, scope=ClientPseudonymType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 417, 3)))

ClientPseudonymType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DisplayName'), AttributeExtensibleString, scope=ClientPseudonymType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 418, 3)))

ClientPseudonymType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EMail'), AttributeExtensibleString, scope=ClientPseudonymType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 419, 3)))

def _BuildAutomaton_21 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_21
    del _BuildAutomaton_21
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 417, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 418, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 419, 3))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 420, 3))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClientPseudonymType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PPID')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 417, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClientPseudonymType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DisplayName')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 418, 3))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClientPseudonymType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EMail')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 419, 3))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/federation/200706')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 420, 3))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ClientPseudonymType._Automaton = _BuildAutomaton_21()




def _BuildAutomaton_22 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_22
    del _BuildAutomaton_22
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 450, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 450, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AssertionType._Automaton = _BuildAutomaton_22()




WebServiceDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LogicalServiceNamesOffered'), LogicalServiceNamesOfferedType, scope=WebServiceDescriptorType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 93, 2)))

WebServiceDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TokenTypesOffered'), TokenTypesOfferedType, scope=WebServiceDescriptorType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 94, 2)))

WebServiceDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClaimDialectsOffered'), ClaimDialectsOfferedType, scope=WebServiceDescriptorType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 95, 2)))

WebServiceDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesOffered'), ClaimTypesOfferedType, scope=WebServiceDescriptorType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 96, 2)))

WebServiceDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesRequested'), ClaimTypesRequestedType, scope=WebServiceDescriptorType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 97, 2)))

WebServiceDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AutomaticPseudonyms'), pyxb.binding.datatypes.boolean, scope=WebServiceDescriptorType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 98, 2)))

WebServiceDescriptorType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TargetScopes'), EndpointType, scope=WebServiceDescriptorType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 99, 2)))

def _BuildAutomaton_23 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_23
    del _BuildAutomaton_23
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 173, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 174, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 175, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 176, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 177, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 79, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 80, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 81, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 82, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 83, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 84, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 85, 10))
    counters.add(cc_11)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 173, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'Extensions')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 174, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'KeyDescriptor')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 175, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'Organization')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 176, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_4, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'ContactPerson')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 177, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_5, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LogicalServiceNamesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 79, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_6, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TokenTypesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 80, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_7, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimDialectsOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 81, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_8, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 82, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_9, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesRequested')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 83, 10))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_10, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AutomaticPseudonyms')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 84, 10))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_11, False))
    symbol = pyxb.binding.content.ElementUse(WebServiceDescriptorType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TargetScopes')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 85, 10))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    st_11._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
WebServiceDescriptorType._Automaton = _BuildAutomaton_23()




SecurityTokenServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SecurityTokenServiceEndpoint'), EndpointType, scope=SecurityTokenServiceType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 114, 2)))

SecurityTokenServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutSubscriptionEndpoint'), EndpointType, scope=SecurityTokenServiceType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 115, 2)))

SecurityTokenServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint'), EndpointType, scope=SecurityTokenServiceType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 116, 2)))

SecurityTokenServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PassiveRequestorEndpoint'), EndpointType, scope=SecurityTokenServiceType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 117, 2)))

def _BuildAutomaton_24 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_24
    del _BuildAutomaton_24
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 173, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 174, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 175, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 176, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 177, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 79, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 80, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 81, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 82, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 83, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 84, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 85, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 107, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 108, 10))
    counters.add(cc_13)
    cc_14 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 109, 10))
    counters.add(cc_14)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 173, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'Extensions')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 174, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'KeyDescriptor')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 175, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'Organization')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 176, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'ContactPerson')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 177, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LogicalServiceNamesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 79, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TokenTypesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 80, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimDialectsOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 81, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 82, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesRequested')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 83, 10))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AutomaticPseudonyms')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 84, 10))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TargetScopes')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 85, 10))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SecurityTokenServiceEndpoint')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 106, 10))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutSubscriptionEndpoint')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 107, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 108, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_14, False))
    symbol = pyxb.binding.content.ElementUse(SecurityTokenServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PassiveRequestorEndpoint')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 109, 10))
    st_15 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_15)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    transitions.append(fac.Transition(st_15, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_13, False) ]))
    st_14._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_15, [
        fac.UpdateInstruction(cc_14, True) ]))
    st_15._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
SecurityTokenServiceType._Automaton = _BuildAutomaton_24()




PseudonymServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint'), EndpointType, scope=PseudonymServiceType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 116, 2)))

PseudonymServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PseudonymServiceEndpoint'), EndpointType, scope=PseudonymServiceType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 131, 2)))

def _BuildAutomaton_25 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_25
    del _BuildAutomaton_25
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 173, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 174, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 175, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 176, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 177, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 79, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 80, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 81, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 82, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 83, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 84, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 85, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 125, 10))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 173, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'Extensions')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 174, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'KeyDescriptor')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 175, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'Organization')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 176, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'ContactPerson')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 177, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LogicalServiceNamesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 79, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TokenTypesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 80, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimDialectsOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 81, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 82, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesRequested')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 83, 10))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AutomaticPseudonyms')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 84, 10))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TargetScopes')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 85, 10))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PseudonymServiceEndpoint')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 124, 10))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(PseudonymServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 125, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
PseudonymServiceType._Automaton = _BuildAutomaton_25()




AttributeServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint'), EndpointType, scope=AttributeServiceType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 116, 2)))

AttributeServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AttributeServiceEndpoint'), EndpointType, scope=AttributeServiceType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 146, 2)))

def _BuildAutomaton_26 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_26
    del _BuildAutomaton_26
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 173, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 174, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 175, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 176, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 177, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 79, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 80, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 81, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 82, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 83, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 84, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 85, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 141, 10))
    counters.add(cc_12)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 173, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'Extensions')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 174, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'KeyDescriptor')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 175, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'Organization')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 176, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'ContactPerson')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 177, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LogicalServiceNamesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 79, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TokenTypesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 80, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimDialectsOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 81, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 82, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesRequested')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 83, 10))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AutomaticPseudonyms')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 84, 10))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TargetScopes')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 85, 10))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AttributeServiceEndpoint')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 140, 10))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(AttributeServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 141, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    st_13._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
AttributeServiceType._Automaton = _BuildAutomaton_26()




ApplicationServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint'), EndpointType, scope=ApplicationServiceType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 116, 2)))

ApplicationServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'PassiveRequestorEndpoint'), EndpointType, scope=ApplicationServiceType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 117, 2)))

ApplicationServiceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ApplicationServiceEndpoint'), EndpointType, scope=ApplicationServiceType, location=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 162, 2)))

def _BuildAutomaton_27 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_27
    del _BuildAutomaton_27
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 173, 12))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 174, 12))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 175, 12))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 176, 12))
    counters.add(cc_3)
    cc_4 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 177, 12))
    counters.add(cc_4)
    cc_5 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 79, 10))
    counters.add(cc_5)
    cc_6 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 80, 10))
    counters.add(cc_6)
    cc_7 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 81, 10))
    counters.add(cc_7)
    cc_8 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 82, 10))
    counters.add(cc_8)
    cc_9 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 83, 10))
    counters.add(cc_9)
    cc_10 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 84, 10))
    counters.add(cc_10)
    cc_11 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 85, 10))
    counters.add(cc_11)
    cc_12 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 156, 10))
    counters.add(cc_12)
    cc_13 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 157, 10))
    counters.add(cc_13)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_ds, u'Signature')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 173, 12))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'Extensions')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 174, 12))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'KeyDescriptor')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 175, 12))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'Organization')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 176, 12))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_md, u'ContactPerson')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/security/saml/v2.0/saml-schema-metadata-2.0.xsd', 177, 12))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'LogicalServiceNamesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 79, 10))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TokenTypesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 80, 10))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimDialectsOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 81, 10))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesOffered')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 82, 10))
    st_8 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_8)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ClaimTypesRequested')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 83, 10))
    st_9 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_9)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'AutomaticPseudonyms')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 84, 10))
    st_10 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_10)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'TargetScopes')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 85, 10))
    st_11 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_11)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ApplicationServiceEndpoint')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 155, 10))
    st_12 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_12)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_12, False))
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SingleSignOutNotificationEndpoint')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 156, 10))
    st_13 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_13)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_13, False))
    symbol = pyxb.binding.content.ElementUse(ApplicationServiceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'PassiveRequestorEndpoint')), pyxb.utils.utility.Location('http://docs.oasis-open.org/wsfed/federation/v1.2/os/ws-federation.xsd', 157, 10))
    st_14 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_14)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_1, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_2, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_2, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_2, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_3, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_3, False) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_4, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_4, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_4, False) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_5, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_5, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_5, False) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_6, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_6, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_6, False) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_7, True) ]))
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_7, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_7, False) ]))
    st_7._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_8, [
        fac.UpdateInstruction(cc_8, True) ]))
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_8, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_8, False) ]))
    st_8._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_9, [
        fac.UpdateInstruction(cc_9, True) ]))
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_9, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_9, False) ]))
    st_9._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_10, [
        fac.UpdateInstruction(cc_10, True) ]))
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_10, False) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_10, False) ]))
    st_10._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_11, [
        fac.UpdateInstruction(cc_11, True) ]))
    transitions.append(fac.Transition(st_12, [
        fac.UpdateInstruction(cc_11, False) ]))
    st_11._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_12, [
         ]))
    transitions.append(fac.Transition(st_13, [
         ]))
    transitions.append(fac.Transition(st_14, [
         ]))
    st_12._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_13, [
        fac.UpdateInstruction(cc_12, True) ]))
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_12, False) ]))
    st_13._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_14, [
        fac.UpdateInstruction(cc_13, True) ]))
    st_14._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ApplicationServiceType._Automaton = _BuildAutomaton_27()

