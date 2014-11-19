# ./_sp.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:2b8c3b7d7d7d35fdf19e565379a41c2650423cd8
# Generated 2014-10-10 17:20:20.705763 by PyXB version 1.2.3
# Namespace http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702 [xmlns:sp]

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
import pyxb.binding.datatypes
import _wsa as _ImportedBinding__wsa

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])

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


# Atomic simple type: {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IncludeTokenType
class IncludeTokenType (pyxb.binding.datatypes.anyURI, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IncludeTokenType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 110, 2)
    _Documentation = None
IncludeTokenType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IncludeTokenType, enum_prefix=None)
IncludeTokenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenNever = IncludeTokenType._CF_enumeration.addEnumeration(unicode_value=u'http://docs.oasis-open.org/ws-sx/ws-trust/200702/ws-securitypolicy/IncludeToken/Never', tag=u'httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenNever')
IncludeTokenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenOnce = IncludeTokenType._CF_enumeration.addEnumeration(unicode_value=u'http://docs.oasis-open.org/ws-sx/ws-trust/200702/ws-securitypolicy/IncludeToken/Once', tag=u'httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenOnce')
IncludeTokenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlwaysToRecipient = IncludeTokenType._CF_enumeration.addEnumeration(unicode_value=u'http://docs.oasis-open.org/ws-sx/ws-trust/200702/ws-securitypolicy/IncludeToken/AlwaysToRecipient', tag=u'httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlwaysToRecipient')
IncludeTokenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlwaysToInitiator = IncludeTokenType._CF_enumeration.addEnumeration(unicode_value=u'http://docs.oasis-open.org/ws-sx/ws-trust/200702/ws-securitypolicy/IncludeToken/AlwaysToInitiator', tag=u'httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlwaysToInitiator')
IncludeTokenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlways = IncludeTokenType._CF_enumeration.addEnumeration(unicode_value=u'http://docs.oasis-open.org/ws-sx/ws-trust/200702/ws-securitypolicy/IncludeToken/Always', tag=u'httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlways')
IncludeTokenType._InitializeFacetMap(IncludeTokenType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'IncludeTokenType', IncludeTokenType)

# Union simple type: {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IncludeTokenOpenType
# superclasses pyxb.binding.datatypes.anySimpleType
class IncludeTokenOpenType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of IncludeTokenType, pyxb.binding.datatypes.anyURI."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IncludeTokenOpenType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 107, 2)
    _Documentation = None

    _MemberTypes = ( IncludeTokenType, pyxb.binding.datatypes.anyURI, )
IncludeTokenOpenType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=IncludeTokenOpenType)
IncludeTokenOpenType._CF_pattern = pyxb.binding.facets.CF_pattern()
IncludeTokenOpenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenNever = u'http://docs.oasis-open.org/ws-sx/ws-trust/200702/ws-securitypolicy/IncludeToken/Never'# originally IncludeTokenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenNever
IncludeTokenOpenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenOnce = u'http://docs.oasis-open.org/ws-sx/ws-trust/200702/ws-securitypolicy/IncludeToken/Once'# originally IncludeTokenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenOnce
IncludeTokenOpenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlwaysToRecipient = u'http://docs.oasis-open.org/ws-sx/ws-trust/200702/ws-securitypolicy/IncludeToken/AlwaysToRecipient'# originally IncludeTokenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlwaysToRecipient
IncludeTokenOpenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlwaysToInitiator = u'http://docs.oasis-open.org/ws-sx/ws-trust/200702/ws-securitypolicy/IncludeToken/AlwaysToInitiator'# originally IncludeTokenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlwaysToInitiator
IncludeTokenOpenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlways = u'http://docs.oasis-open.org/ws-sx/ws-trust/200702/ws-securitypolicy/IncludeToken/Always'# originally IncludeTokenType.httpdocs_oasis_open_orgws_sxws_trust200702ws_securitypolicyIncludeTokenAlways
IncludeTokenOpenType._InitializeFacetMap(IncludeTokenOpenType._CF_enumeration,
   IncludeTokenOpenType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'IncludeTokenOpenType', IncludeTokenOpenType)

# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}SePartsType with content type ELEMENT_ONLY
class SePartsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}SePartsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SePartsType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 51, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}Body uses Python identifier Body
    __Body = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Body'), 'Body', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_SePartsType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702Body', False, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 53, 6), )

    
    Body = property(__Body.value, __Body.set, None, None)

    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}Header uses Python identifier Header
    __Header = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Header'), 'Header', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_SePartsType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702Header', True, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 54, 6), )

    
    Header = property(__Header.value, __Header.set, None, None)

    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}Attachments uses Python identifier Attachments
    __Attachments = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Attachments'), 'Attachments', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_SePartsType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702Attachments', False, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 55, 6), )

    
    Attachments = property(__Attachments.value, __Attachments.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        __Body.name() : __Body,
        __Header.name() : __Header,
        __Attachments.name() : __Attachments
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'SePartsType', SePartsType)


# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}EmptyType with content type EMPTY
class EmptyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}EmptyType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EmptyType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 60, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'EmptyType', EmptyType)


# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}HeaderType with content type EMPTY
class HeaderType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}HeaderType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'HeaderType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 61, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_HeaderType_Name', pyxb.binding.datatypes.QName)
    __Name._DeclarationLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 62, 4)
    __Name._UseLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 62, 4)
    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute Namespace uses Python identifier Namespace_
    __Namespace = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Namespace'), 'Namespace_', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_HeaderType_Namespace', pyxb.binding.datatypes.anyURI, required=True)
    __Namespace._DeclarationLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 63, 4)
    __Namespace._UseLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 63, 4)
    
    Namespace_ = property(__Namespace.value, __Namespace.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __Name.name() : __Name,
        __Namespace.name() : __Namespace
    })
Namespace.addCategoryObject('typeBinding', u'HeaderType', HeaderType)


# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}SerElementsType with content type ELEMENT_ONLY
class SerElementsType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}SerElementsType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SerElementsType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 88, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}XPath uses Python identifier XPath
    __XPath = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'XPath'), 'XPath', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_SerElementsType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702XPath', True, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 90, 6), )

    
    XPath = property(__XPath.value, __XPath.set, None, None)

    
    # Attribute XPathVersion uses Python identifier XPathVersion
    __XPathVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'XPathVersion'), 'XPathVersion', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_SerElementsType_XPathVersion', pyxb.binding.datatypes.anyURI)
    __XPathVersion._DeclarationLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 93, 4)
    __XPathVersion._UseLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 93, 4)
    
    XPathVersion = property(__XPathVersion.value, __XPathVersion.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        __XPath.name() : __XPath
    })
    _AttributeMap.update({
        __XPathVersion.name() : __XPathVersion
    })
Namespace.addCategoryObject('typeBinding', u'SerElementsType', SerElementsType)


# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}QNameAssertionType with content type EMPTY
class QNameAssertionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}QNameAssertionType with content type EMPTY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_EMPTY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'QNameAssertionType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 175, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'QNameAssertionType', QNameAssertionType)


# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}RequestSecurityTokenTemplateType with content type ELEMENT_ONLY
class RequestSecurityTokenTemplateType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}RequestSecurityTokenTemplateType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RequestSecurityTokenTemplateType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 202, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute TrustVersion uses Python identifier TrustVersion
    __TrustVersion = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'TrustVersion'), 'TrustVersion', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_RequestSecurityTokenTemplateType_TrustVersion', pyxb.binding.datatypes.anyURI)
    __TrustVersion._DeclarationLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 206, 4)
    __TrustVersion._UseLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 206, 4)
    
    TrustVersion = property(__TrustVersion.value, __TrustVersion.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __TrustVersion.name() : __TrustVersion
    })
Namespace.addCategoryObject('typeBinding', u'RequestSecurityTokenTemplateType', RequestSecurityTokenTemplateType)


# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}NestedPolicyType with content type ELEMENT_ONLY
class NestedPolicyType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}NestedPolicyType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'NestedPolicyType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 614, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'NestedPolicyType', NestedPolicyType)


# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}TokenAssertionType with content type ELEMENT_ONLY
class TokenAssertionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}TokenAssertionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'TokenAssertionType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 127, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}Issuer uses Python identifier Issuer
    __Issuer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Issuer'), 'Issuer', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_TokenAssertionType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702Issuer', False, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 130, 8), )

    
    Issuer = property(__Issuer.value, __Issuer.set, None, None)

    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IssuerName uses Python identifier IssuerName
    __IssuerName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IssuerName'), 'IssuerName', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_TokenAssertionType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702IssuerName', False, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 131, 8), )

    
    IssuerName = property(__IssuerName.value, __IssuerName.set, None, None)

    
    # Attribute {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IncludeToken uses Python identifier IncludeToken
    __IncludeToken = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'IncludeToken'), 'IncludeToken', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_TokenAssertionType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702IncludeToken', IncludeTokenOpenType)
    __IncludeToken._DeclarationLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 100, 2)
    __IncludeToken._UseLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 139, 4)
    
    IncludeToken = property(__IncludeToken.value, __IncludeToken.set, None, u'\n        5.1 Token Inclusion\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        __Issuer.name() : __Issuer,
        __IssuerName.name() : __IssuerName
    })
    _AttributeMap.update({
        __IncludeToken.name() : __IncludeToken
    })
Namespace.addCategoryObject('typeBinding', u'TokenAssertionType', TokenAssertionType)


# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IssuedTokenType with content type ELEMENT_ONLY
class IssuedTokenType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IssuedTokenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'IssuedTokenType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 186, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}Issuer uses Python identifier Issuer
    __Issuer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Issuer'), 'Issuer', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_IssuedTokenType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702Issuer', False, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 189, 8), )

    
    Issuer = property(__Issuer.value, __Issuer.set, None, None)

    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IssuerName uses Python identifier IssuerName
    __IssuerName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IssuerName'), 'IssuerName', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_IssuedTokenType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702IssuerName', False, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 190, 8), )

    
    IssuerName = property(__IssuerName.value, __IssuerName.set, None, None)

    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}RequestSecurityTokenTemplate uses Python identifier RequestSecurityTokenTemplate
    __RequestSecurityTokenTemplate = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'RequestSecurityTokenTemplate'), 'RequestSecurityTokenTemplate', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_IssuedTokenType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702RequestSecurityTokenTemplate', False, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 192, 6), )

    
    RequestSecurityTokenTemplate = property(__RequestSecurityTokenTemplate.value, __RequestSecurityTokenTemplate.set, None, None)

    
    # Attribute {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IncludeToken uses Python identifier IncludeToken
    __IncludeToken = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'IncludeToken'), 'IncludeToken', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_IssuedTokenType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702IncludeToken', IncludeTokenOpenType)
    __IncludeToken._DeclarationLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 100, 2)
    __IncludeToken._UseLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 199, 4)
    
    IncludeToken = property(__IncludeToken.value, __IncludeToken.set, None, u'\n        5.1 Token Inclusion\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        __Issuer.name() : __Issuer,
        __IssuerName.name() : __IssuerName,
        __RequestSecurityTokenTemplate.name() : __RequestSecurityTokenTemplate
    })
    _AttributeMap.update({
        __IncludeToken.name() : __IncludeToken
    })
Namespace.addCategoryObject('typeBinding', u'IssuedTokenType', IssuedTokenType)


# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}SpnegoContextTokenType with content type ELEMENT_ONLY
class SpnegoContextTokenType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}SpnegoContextTokenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SpnegoContextTokenType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 369, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}Issuer uses Python identifier Issuer
    __Issuer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Issuer'), 'Issuer', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_SpnegoContextTokenType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702Issuer', False, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 372, 8), )

    
    Issuer = property(__Issuer.value, __Issuer.set, None, None)

    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IssuerName uses Python identifier IssuerName
    __IssuerName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IssuerName'), 'IssuerName', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_SpnegoContextTokenType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702IssuerName', False, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 373, 8), )

    
    IssuerName = property(__IssuerName.value, __IssuerName.set, None, None)

    
    # Attribute {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IncludeToken uses Python identifier IncludeToken
    __IncludeToken = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'IncludeToken'), 'IncludeToken', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_SpnegoContextTokenType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702IncludeToken', IncludeTokenOpenType)
    __IncludeToken._DeclarationLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 100, 2)
    __IncludeToken._UseLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 381, 4)
    
    IncludeToken = property(__IncludeToken.value, __IncludeToken.set, None, u'\n        5.1 Token Inclusion\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        __Issuer.name() : __Issuer,
        __IssuerName.name() : __IssuerName
    })
    _AttributeMap.update({
        __IncludeToken.name() : __IncludeToken
    })
Namespace.addCategoryObject('typeBinding', u'SpnegoContextTokenType', SpnegoContextTokenType)


# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}SecureConversationTokenType with content type ELEMENT_ONLY
class SecureConversationTokenType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}SecureConversationTokenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'SecureConversationTokenType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 442, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}Issuer uses Python identifier Issuer
    __Issuer = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Issuer'), 'Issuer', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_SecureConversationTokenType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702Issuer', False, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 445, 8), )

    
    Issuer = property(__Issuer.value, __Issuer.set, None, None)

    
    # Element {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IssuerName uses Python identifier IssuerName
    __IssuerName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'IssuerName'), 'IssuerName', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_SecureConversationTokenType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702IssuerName', False, pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 446, 8), )

    
    IssuerName = property(__IssuerName.value, __IssuerName.set, None, None)

    
    # Attribute {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IncludeToken uses Python identifier IncludeToken
    __IncludeToken = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'IncludeToken'), 'IncludeToken', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_SecureConversationTokenType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702IncludeToken', IncludeTokenOpenType)
    __IncludeToken._DeclarationLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 100, 2)
    __IncludeToken._UseLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 454, 4)
    
    IncludeToken = property(__IncludeToken.value, __IncludeToken.set, None, u'\n        5.1 Token Inclusion\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        __Issuer.name() : __Issuer,
        __IssuerName.name() : __IssuerName
    })
    _AttributeMap.update({
        __IncludeToken.name() : __IncludeToken
    })
Namespace.addCategoryObject('typeBinding', u'SecureConversationTokenType', SecureConversationTokenType)


# Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}KeyValueTokenType with content type ELEMENT_ONLY
class KeyValueTokenType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}KeyValueTokenType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'KeyValueTokenType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 585, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Attribute {http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702}IncludeToken uses Python identifier IncludeToken
    __IncludeToken = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(Namespace, u'IncludeToken'), 'IncludeToken', '__httpdocs_oasis_open_orgws_sxws_securitypolicy200702_KeyValueTokenType_httpdocs_oasis_open_orgws_sxws_securitypolicy200702IncludeToken', IncludeTokenOpenType)
    __IncludeToken._DeclarationLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 100, 2)
    __IncludeToken._UseLocation = pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 593, 4)
    
    IncludeToken = property(__IncludeToken.value, __IncludeToken.set, None, u'\n        5.1 Token Inclusion\n      ')

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any)
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __IncludeToken.name() : __IncludeToken
    })
Namespace.addCategoryObject('typeBinding', u'KeyValueTokenType', KeyValueTokenType)


SignedParts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignedParts'), SePartsType, documentation=u'\n        4.1.1 SignedParts Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 37, 2))
Namespace.addCategoryObject('elementBinding', SignedParts.name().localName(), SignedParts)

EncryptedParts = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EncryptedParts'), SePartsType, documentation=u'\n        4.2.1 EncryptedParts Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 44, 2))
Namespace.addCategoryObject('elementBinding', EncryptedParts.name().localName(), EncryptedParts)

SignedElements = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignedElements'), SerElementsType, documentation=u'\n        4.1.2 SignedElements Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 67, 2))
Namespace.addCategoryObject('elementBinding', SignedElements.name().localName(), SignedElements)

EncryptedElements = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EncryptedElements'), SerElementsType, documentation=u'\n        4.2.2 EncryptedElements Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 74, 2))
Namespace.addCategoryObject('elementBinding', EncryptedElements.name().localName(), EncryptedElements)

RequiredElements = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequiredElements'), SerElementsType, documentation=u'\n        4.3.1 RequiredElements Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 81, 2))
Namespace.addCategoryObject('elementBinding', RequiredElements.name().localName(), RequiredElements)

NoPassword = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'NoPassword'), QNameAssertionType, documentation=u'\n        5.4.1 UsernameToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 143, 2))
Namespace.addCategoryObject('elementBinding', NoPassword.name().localName(), NoPassword)

HashPassword = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HashPassword'), QNameAssertionType, documentation=u'\n        5.4.1 UsernameToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 150, 2))
Namespace.addCategoryObject('elementBinding', HashPassword.name().localName(), HashPassword)

WssUsernameToken10 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssUsernameToken10'), QNameAssertionType, documentation=u'\n        5.4.1 UsernameToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 157, 2))
Namespace.addCategoryObject('elementBinding', WssUsernameToken10.name().localName(), WssUsernameToken10)

WssUsernameToken11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssUsernameToken11'), QNameAssertionType, documentation=u'\n        5.4.1 UsernameToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 164, 2))
Namespace.addCategoryObject('elementBinding', WssUsernameToken11.name().localName(), WssUsernameToken11)

RequireDerivedKeys = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireDerivedKeys'), QNameAssertionType, documentation=u'\n        5.4.2 IssuedToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 210, 2))
Namespace.addCategoryObject('elementBinding', RequireDerivedKeys.name().localName(), RequireDerivedKeys)

RequireImpliedDerivedKeys = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireImpliedDerivedKeys'), QNameAssertionType, documentation=u'\n        5.4.2 IssuedToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 217, 2))
Namespace.addCategoryObject('elementBinding', RequireImpliedDerivedKeys.name().localName(), RequireImpliedDerivedKeys)

RequireExplicitDerivedKeys = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireExplicitDerivedKeys'), QNameAssertionType, documentation=u'\n        5.4.2 IssuedToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 224, 2))
Namespace.addCategoryObject('elementBinding', RequireExplicitDerivedKeys.name().localName(), RequireExplicitDerivedKeys)

RequireExternalReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireExternalReference'), QNameAssertionType, documentation=u'\n        5.4.2 IssuedToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 231, 2))
Namespace.addCategoryObject('elementBinding', RequireExternalReference.name().localName(), RequireExternalReference)

RequireInternalReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireInternalReference'), QNameAssertionType, documentation=u'\n        5.4.2 IssuedToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 238, 2))
Namespace.addCategoryObject('elementBinding', RequireInternalReference.name().localName(), RequireInternalReference)

RequireKeyIdentifierReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireKeyIdentifierReference'), QNameAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 257, 2))
Namespace.addCategoryObject('elementBinding', RequireKeyIdentifierReference.name().localName(), RequireKeyIdentifierReference)

RequireIssuerSerialReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireIssuerSerialReference'), QNameAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 264, 2))
Namespace.addCategoryObject('elementBinding', RequireIssuerSerialReference.name().localName(), RequireIssuerSerialReference)

RequireEmbeddedTokenReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireEmbeddedTokenReference'), QNameAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 271, 2))
Namespace.addCategoryObject('elementBinding', RequireEmbeddedTokenReference.name().localName(), RequireEmbeddedTokenReference)

RequireThumbprintReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireThumbprintReference'), QNameAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 278, 2))
Namespace.addCategoryObject('elementBinding', RequireThumbprintReference.name().localName(), RequireThumbprintReference)

WssX509V3Token10 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssX509V3Token10'), QNameAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 285, 2))
Namespace.addCategoryObject('elementBinding', WssX509V3Token10.name().localName(), WssX509V3Token10)

WssX509Pkcs7Token10 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssX509Pkcs7Token10'), QNameAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 292, 2))
Namespace.addCategoryObject('elementBinding', WssX509Pkcs7Token10.name().localName(), WssX509Pkcs7Token10)

WssX509PkiPathV1Token10 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssX509PkiPathV1Token10'), QNameAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 299, 2))
Namespace.addCategoryObject('elementBinding', WssX509PkiPathV1Token10.name().localName(), WssX509PkiPathV1Token10)

WssX509V1Token11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssX509V1Token11'), QNameAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 306, 2))
Namespace.addCategoryObject('elementBinding', WssX509V1Token11.name().localName(), WssX509V1Token11)

WssX509V3Token11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssX509V3Token11'), QNameAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 313, 2))
Namespace.addCategoryObject('elementBinding', WssX509V3Token11.name().localName(), WssX509V3Token11)

WssX509Pkcs7Token11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssX509Pkcs7Token11'), QNameAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 320, 2))
Namespace.addCategoryObject('elementBinding', WssX509Pkcs7Token11.name().localName(), WssX509Pkcs7Token11)

WssX509PkiPathV1Token11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssX509PkiPathV1Token11'), QNameAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 327, 2))
Namespace.addCategoryObject('elementBinding', WssX509PkiPathV1Token11.name().localName(), WssX509PkiPathV1Token11)

WssKerberosV5ApReqToken11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssKerberosV5ApReqToken11'), QNameAssertionType, documentation=u'\n        5.4.4 KerberosToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 347, 2))
Namespace.addCategoryObject('elementBinding', WssKerberosV5ApReqToken11.name().localName(), WssKerberosV5ApReqToken11)

WssGssKerberosV5ApReqToken11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssGssKerberosV5ApReqToken11'), QNameAssertionType, documentation=u'\n        5.4.4 KerberosToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 354, 2))
Namespace.addCategoryObject('elementBinding', WssGssKerberosV5ApReqToken11.name().localName(), WssGssKerberosV5ApReqToken11)

MustNotSendCancel = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustNotSendCancel'), QNameAssertionType, documentation=u'\n        5.4.5 SpnegoContextToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 387, 2))
Namespace.addCategoryObject('elementBinding', MustNotSendCancel.name().localName(), MustNotSendCancel)

MustNotSendAmend = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustNotSendAmend'), QNameAssertionType, documentation=u'\n        5.4.5 SpnegoContextToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 394, 2))
Namespace.addCategoryObject('elementBinding', MustNotSendAmend.name().localName(), MustNotSendAmend)

MustNotSendRenew = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustNotSendRenew'), QNameAssertionType, documentation=u'\n        5.4.5 SpnegoContextToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 401, 2))
Namespace.addCategoryObject('elementBinding', MustNotSendRenew.name().localName(), MustNotSendRenew)

RequireExternalUriReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireExternalUriReference'), QNameAssertionType, documentation=u'\n        5.4.6 SecurityContextToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 420, 2))
Namespace.addCategoryObject('elementBinding', RequireExternalUriReference.name().localName(), RequireExternalUriReference)

SC13SecurityContextToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SC13SecurityContextToken'), QNameAssertionType, documentation=u'\n        5.4.6 SecurityContextToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 427, 2))
Namespace.addCategoryObject('elementBinding', SC13SecurityContextToken.name().localName(), SC13SecurityContextToken)

BootstrapPolicy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'BootstrapPolicy'), NestedPolicyType, documentation=u'\n        5.4.7 SecureConversationToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 466, 2))
Namespace.addCategoryObject('elementBinding', BootstrapPolicy.name().localName(), BootstrapPolicy)

WssSamlV11Token10 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssSamlV11Token10'), QNameAssertionType, documentation=u'\n        5.4.8 SamlToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 486, 2))
Namespace.addCategoryObject('elementBinding', WssSamlV11Token10.name().localName(), WssSamlV11Token10)

WssSamlV11Token11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssSamlV11Token11'), QNameAssertionType, documentation=u'\n        5.4.8 SamlToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 493, 2))
Namespace.addCategoryObject('elementBinding', WssSamlV11Token11.name().localName(), WssSamlV11Token11)

WssSamlV20Token11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssSamlV20Token11'), QNameAssertionType, documentation=u'\n        5.4.8 SamlToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 500, 2))
Namespace.addCategoryObject('elementBinding', WssSamlV20Token11.name().localName(), WssSamlV20Token11)

WssRelV10Token10 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssRelV10Token10'), QNameAssertionType, documentation=u'\n        5.4.9 RelToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 520, 2))
Namespace.addCategoryObject('elementBinding', WssRelV10Token10.name().localName(), WssRelV10Token10)

WssRelV20Token10 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssRelV20Token10'), QNameAssertionType, documentation=u'\n        5.4.9 RelToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 527, 2))
Namespace.addCategoryObject('elementBinding', WssRelV20Token10.name().localName(), WssRelV20Token10)

WssRelV10Token11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssRelV10Token11'), QNameAssertionType, documentation=u'\n        5.4.9 RelToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 534, 2))
Namespace.addCategoryObject('elementBinding', WssRelV10Token11.name().localName(), WssRelV10Token11)

WssRelV20Token11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'WssRelV20Token11'), QNameAssertionType, documentation=u'\n        5.4.9 RelToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 541, 2))
Namespace.addCategoryObject('elementBinding', WssRelV20Token11.name().localName(), WssRelV20Token11)

HttpBasicAuthentication = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HttpBasicAuthentication'), QNameAssertionType, documentation=u'\n        5.4.10 HttpsToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 556, 2))
Namespace.addCategoryObject('elementBinding', HttpBasicAuthentication.name().localName(), HttpBasicAuthentication)

HttpDigestAuthentication = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HttpDigestAuthentication'), QNameAssertionType, documentation=u'\n        5.4.10 HttpsToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 563, 2))
Namespace.addCategoryObject('elementBinding', HttpDigestAuthentication.name().localName(), HttpDigestAuthentication)

RequireClientCertificate = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireClientCertificate'), QNameAssertionType, documentation=u'\n        5.4.10 HttpsToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 570, 2))
Namespace.addCategoryObject('elementBinding', RequireClientCertificate.name().localName(), RequireClientCertificate)

RsaKeyValue = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RsaKeyValue'), QNameAssertionType, documentation=u'\n        5.4.11 KeyValueToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 596, 2))
Namespace.addCategoryObject('elementBinding', RsaKeyValue.name().localName(), RsaKeyValue)

AlgorithmSuite = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AlgorithmSuite'), NestedPolicyType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 607, 2))
Namespace.addCategoryObject('elementBinding', AlgorithmSuite.name().localName(), AlgorithmSuite)

Basic256 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic256'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 621, 2))
Namespace.addCategoryObject('elementBinding', Basic256.name().localName(), Basic256)

Basic192 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic192'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 628, 2))
Namespace.addCategoryObject('elementBinding', Basic192.name().localName(), Basic192)

Basic128 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic128'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 635, 2))
Namespace.addCategoryObject('elementBinding', Basic128.name().localName(), Basic128)

TripleDes = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TripleDes'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 642, 2))
Namespace.addCategoryObject('elementBinding', TripleDes.name().localName(), TripleDes)

Basic256Rsa15 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic256Rsa15'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 649, 2))
Namespace.addCategoryObject('elementBinding', Basic256Rsa15.name().localName(), Basic256Rsa15)

Basic192Rsa15 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic192Rsa15'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 656, 2))
Namespace.addCategoryObject('elementBinding', Basic192Rsa15.name().localName(), Basic192Rsa15)

Basic128Rsa15 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic128Rsa15'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 663, 2))
Namespace.addCategoryObject('elementBinding', Basic128Rsa15.name().localName(), Basic128Rsa15)

TripleDesRsa15 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TripleDesRsa15'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 670, 2))
Namespace.addCategoryObject('elementBinding', TripleDesRsa15.name().localName(), TripleDesRsa15)

Basic256Sha256 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic256Sha256'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 677, 2))
Namespace.addCategoryObject('elementBinding', Basic256Sha256.name().localName(), Basic256Sha256)

Basic192Sha256 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic192Sha256'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 684, 2))
Namespace.addCategoryObject('elementBinding', Basic192Sha256.name().localName(), Basic192Sha256)

Basic128Sha256 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic128Sha256'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 691, 2))
Namespace.addCategoryObject('elementBinding', Basic128Sha256.name().localName(), Basic128Sha256)

TripleDesSha256 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TripleDesSha256'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 698, 2))
Namespace.addCategoryObject('elementBinding', TripleDesSha256.name().localName(), TripleDesSha256)

Basic256Sha256Rsa15 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic256Sha256Rsa15'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 705, 2))
Namespace.addCategoryObject('elementBinding', Basic256Sha256Rsa15.name().localName(), Basic256Sha256Rsa15)

Basic192Sha256Rsa15 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic192Sha256Rsa15'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 712, 2))
Namespace.addCategoryObject('elementBinding', Basic192Sha256Rsa15.name().localName(), Basic192Sha256Rsa15)

Basic128Sha256Rsa15 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Basic128Sha256Rsa15'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 719, 2))
Namespace.addCategoryObject('elementBinding', Basic128Sha256Rsa15.name().localName(), Basic128Sha256Rsa15)

TripleDesSha256Rsa15 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TripleDesSha256Rsa15'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 726, 2))
Namespace.addCategoryObject('elementBinding', TripleDesSha256Rsa15.name().localName(), TripleDesSha256Rsa15)

InclusiveC14N = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InclusiveC14N'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 733, 2))
Namespace.addCategoryObject('elementBinding', InclusiveC14N.name().localName(), InclusiveC14N)

SOAPNormalization10 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SOAPNormalization10'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 740, 2))
Namespace.addCategoryObject('elementBinding', SOAPNormalization10.name().localName(), SOAPNormalization10)

STRTransform10 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'STRTransform10'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 747, 2))
Namespace.addCategoryObject('elementBinding', STRTransform10.name().localName(), STRTransform10)

XPath10 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XPath10'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 754, 2))
Namespace.addCategoryObject('elementBinding', XPath10.name().localName(), XPath10)

XPathFilter20 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XPathFilter20'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 761, 2))
Namespace.addCategoryObject('elementBinding', XPathFilter20.name().localName(), XPathFilter20)

AbsXPath = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AbsXPath'), QNameAssertionType, documentation=u'\n        7.1 AlgorithmSuite Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 768, 2))
Namespace.addCategoryObject('elementBinding', AbsXPath.name().localName(), AbsXPath)

Layout = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Layout'), NestedPolicyType, documentation=u'\n        7.2 Layout Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 776, 2))
Namespace.addCategoryObject('elementBinding', Layout.name().localName(), Layout)

Strict = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Strict'), QNameAssertionType, documentation=u'\n        7.2 Layout Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 784, 2))
Namespace.addCategoryObject('elementBinding', Strict.name().localName(), Strict)

Lax = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Lax'), QNameAssertionType, documentation=u'\n        7.2 Layout Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 791, 2))
Namespace.addCategoryObject('elementBinding', Lax.name().localName(), Lax)

LaxTsFirst = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LaxTsFirst'), QNameAssertionType, documentation=u'\n        7.2 Layout Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 798, 2))
Namespace.addCategoryObject('elementBinding', LaxTsFirst.name().localName(), LaxTsFirst)

LaxTsLast = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'LaxTsLast'), QNameAssertionType, documentation=u'\n        7.2 Layout Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 805, 2))
Namespace.addCategoryObject('elementBinding', LaxTsLast.name().localName(), LaxTsLast)

TransportBinding = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TransportBinding'), NestedPolicyType, documentation=u'\n        7.3 TransportBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 813, 2))
Namespace.addCategoryObject('elementBinding', TransportBinding.name().localName(), TransportBinding)

TransportToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'TransportToken'), NestedPolicyType, documentation=u'\n        7.3 TransportBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 821, 2))
Namespace.addCategoryObject('elementBinding', TransportToken.name().localName(), TransportToken)

IncludeTimestamp = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IncludeTimestamp'), QNameAssertionType, documentation=u'\n        7.3 TransportBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 831, 2))
Namespace.addCategoryObject('elementBinding', IncludeTimestamp.name().localName(), IncludeTimestamp)

SymmetricBinding = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SymmetricBinding'), NestedPolicyType, documentation=u'\n        7.4 SymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 839, 2))
Namespace.addCategoryObject('elementBinding', SymmetricBinding.name().localName(), SymmetricBinding)

EncryptionToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EncryptionToken'), NestedPolicyType, documentation=u'\n        7.4 SymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 846, 2))
Namespace.addCategoryObject('elementBinding', EncryptionToken.name().localName(), EncryptionToken)

SignatureToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignatureToken'), NestedPolicyType, documentation=u'\n        8=7.4 SymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 853, 2))
Namespace.addCategoryObject('elementBinding', SignatureToken.name().localName(), SignatureToken)

ProtectionToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtectionToken'), NestedPolicyType, documentation=u'\n        7.4 SymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 860, 2))
Namespace.addCategoryObject('elementBinding', ProtectionToken.name().localName(), ProtectionToken)

EncryptBeforeSigning = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EncryptBeforeSigning'), QNameAssertionType, documentation=u'\n        7.4 SymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 871, 2))
Namespace.addCategoryObject('elementBinding', EncryptBeforeSigning.name().localName(), EncryptBeforeSigning)

EncryptSignature = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EncryptSignature'), QNameAssertionType, documentation=u'\n        7.4 SymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 878, 2))
Namespace.addCategoryObject('elementBinding', EncryptSignature.name().localName(), EncryptSignature)

ProtectTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProtectTokens'), QNameAssertionType, documentation=u'\n        7.4 SymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 885, 2))
Namespace.addCategoryObject('elementBinding', ProtectTokens.name().localName(), ProtectTokens)

OnlySignEntireHeadersAndBody = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'OnlySignEntireHeadersAndBody'), QNameAssertionType, documentation=u'\n        7.4 SymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 892, 2))
Namespace.addCategoryObject('elementBinding', OnlySignEntireHeadersAndBody.name().localName(), OnlySignEntireHeadersAndBody)

AsymmetricBinding = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AsymmetricBinding'), NestedPolicyType, documentation=u'\n        7.5 AsymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 900, 2))
Namespace.addCategoryObject('elementBinding', AsymmetricBinding.name().localName(), AsymmetricBinding)

InitiatorToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InitiatorToken'), NestedPolicyType, documentation=u'\n        7.5 AsymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 908, 2))
Namespace.addCategoryObject('elementBinding', InitiatorToken.name().localName(), InitiatorToken)

InitiatorSignatureToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InitiatorSignatureToken'), NestedPolicyType, documentation=u'\n        7.5 AsymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 916, 2))
Namespace.addCategoryObject('elementBinding', InitiatorSignatureToken.name().localName(), InitiatorSignatureToken)

InitiatorEncryptionToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'InitiatorEncryptionToken'), NestedPolicyType, documentation=u'\n        7.5 AsymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 924, 2))
Namespace.addCategoryObject('elementBinding', InitiatorEncryptionToken.name().localName(), InitiatorEncryptionToken)

RecipientToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecipientToken'), NestedPolicyType, documentation=u'\n        7.5 AsymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 932, 2))
Namespace.addCategoryObject('elementBinding', RecipientToken.name().localName(), RecipientToken)

RecipientSignatureToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecipientSignatureToken'), NestedPolicyType, documentation=u'\n        7.5 AsymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 940, 2))
Namespace.addCategoryObject('elementBinding', RecipientSignatureToken.name().localName(), RecipientSignatureToken)

RecipientEncryptionToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RecipientEncryptionToken'), NestedPolicyType, documentation=u'\n        7.5 AsymmetricBinding Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 948, 2))
Namespace.addCategoryObject('elementBinding', RecipientEncryptionToken.name().localName(), RecipientEncryptionToken)

SupportingTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SupportingTokens'), NestedPolicyType, documentation=u'\n        8.1 SupportingTokens Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 966, 2))
Namespace.addCategoryObject('elementBinding', SupportingTokens.name().localName(), SupportingTokens)

SignedSupportingTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignedSupportingTokens'), NestedPolicyType, documentation=u'\n        8.2 SignedSupportingTokens Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 979, 2))
Namespace.addCategoryObject('elementBinding', SignedSupportingTokens.name().localName(), SignedSupportingTokens)

EndorsingSupportingTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndorsingSupportingTokens'), NestedPolicyType, documentation=u'\n        8.3 EndorsingSupportingTokens Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 992, 2))
Namespace.addCategoryObject('elementBinding', EndorsingSupportingTokens.name().localName(), EndorsingSupportingTokens)

SignedEndorsingSupportingTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignedEndorsingSupportingTokens'), NestedPolicyType, documentation=u'\n        8.4 SignedEndorsingSupportingTokens Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1005, 2))
Namespace.addCategoryObject('elementBinding', SignedEndorsingSupportingTokens.name().localName(), SignedEndorsingSupportingTokens)

SignedEncryptedSupportingTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignedEncryptedSupportingTokens'), NestedPolicyType, documentation=u'\n        8.5 SignedEncryptedSupportingTokens Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1018, 2))
Namespace.addCategoryObject('elementBinding', SignedEncryptedSupportingTokens.name().localName(), SignedEncryptedSupportingTokens)

EncryptedSupportingTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EncryptedSupportingTokens'), NestedPolicyType, documentation=u'\n        8.6 EncryptedSupportingTokens Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1031, 2))
Namespace.addCategoryObject('elementBinding', EncryptedSupportingTokens.name().localName(), EncryptedSupportingTokens)

EndorsingEncryptedSupportingTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndorsingEncryptedSupportingTokens'), NestedPolicyType, documentation=u'\n        8.7 EndorsingEncryptedSupportingTokens Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1044, 2))
Namespace.addCategoryObject('elementBinding', EndorsingEncryptedSupportingTokens.name().localName(), EndorsingEncryptedSupportingTokens)

SignedEndorsingEncryptedSupportingTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SignedEndorsingEncryptedSupportingTokens'), NestedPolicyType, documentation=u'\n        8.8 SignedEndorsingEncryptedSupportingTokens Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1057, 2))
Namespace.addCategoryObject('elementBinding', SignedEndorsingEncryptedSupportingTokens.name().localName(), SignedEndorsingEncryptedSupportingTokens)

Wss10 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wss10'), NestedPolicyType, documentation=u'\n        9.1 Wss10 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1073, 2))
Namespace.addCategoryObject('elementBinding', Wss10.name().localName(), Wss10)

MustSupportRefKeyIdentifier = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustSupportRefKeyIdentifier'), QNameAssertionType, documentation=u'\n        9.1 Wss10 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1081, 2))
Namespace.addCategoryObject('elementBinding', MustSupportRefKeyIdentifier.name().localName(), MustSupportRefKeyIdentifier)

MustSupportRefIssuerSerial = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustSupportRefIssuerSerial'), QNameAssertionType, documentation=u'\n        9.1 Wss10 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1088, 2))
Namespace.addCategoryObject('elementBinding', MustSupportRefIssuerSerial.name().localName(), MustSupportRefIssuerSerial)

MustSupportRefExternalURI = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustSupportRefExternalURI'), QNameAssertionType, documentation=u'\n        9.1 Wss10 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1095, 2))
Namespace.addCategoryObject('elementBinding', MustSupportRefExternalURI.name().localName(), MustSupportRefExternalURI)

MustSupportRefEmbeddedToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustSupportRefEmbeddedToken'), QNameAssertionType, documentation=u'\n        9.1 Wss10 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1102, 2))
Namespace.addCategoryObject('elementBinding', MustSupportRefEmbeddedToken.name().localName(), MustSupportRefEmbeddedToken)

Wss11 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Wss11'), NestedPolicyType, documentation=u'\n        9.2 Wss11 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1110, 2))
Namespace.addCategoryObject('elementBinding', Wss11.name().localName(), Wss11)

MustSupportRefThumbprint = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustSupportRefThumbprint'), QNameAssertionType, documentation=u'\n        9.2 Wss11 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1122, 2))
Namespace.addCategoryObject('elementBinding', MustSupportRefThumbprint.name().localName(), MustSupportRefThumbprint)

MustSupportRefEncryptedKey = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustSupportRefEncryptedKey'), QNameAssertionType, documentation=u'\n        9.2 Wss11 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1129, 2))
Namespace.addCategoryObject('elementBinding', MustSupportRefEncryptedKey.name().localName(), MustSupportRefEncryptedKey)

RequireSignatureConfirmation = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireSignatureConfirmation'), QNameAssertionType, documentation=u'\n        9.2 Wss11 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1136, 2))
Namespace.addCategoryObject('elementBinding', RequireSignatureConfirmation.name().localName(), RequireSignatureConfirmation)

Trust13 = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Trust13'), NestedPolicyType, documentation=u'\n        10.1 Trust13 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1147, 2))
Namespace.addCategoryObject('elementBinding', Trust13.name().localName(), Trust13)

MustSupportClientChallenge = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustSupportClientChallenge'), QNameAssertionType, documentation=u'\n        10.1 Trust13 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1155, 2))
Namespace.addCategoryObject('elementBinding', MustSupportClientChallenge.name().localName(), MustSupportClientChallenge)

MustSupportServerChallenge = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustSupportServerChallenge'), QNameAssertionType, documentation=u'\n        10.1 Trust13 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1162, 2))
Namespace.addCategoryObject('elementBinding', MustSupportServerChallenge.name().localName(), MustSupportServerChallenge)

RequireClientEntropy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireClientEntropy'), QNameAssertionType, documentation=u'\n        10.1 Trust13 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1169, 2))
Namespace.addCategoryObject('elementBinding', RequireClientEntropy.name().localName(), RequireClientEntropy)

RequireServerEntropy = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireServerEntropy'), QNameAssertionType, documentation=u'\n        10.1 Trust13 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1176, 2))
Namespace.addCategoryObject('elementBinding', RequireServerEntropy.name().localName(), RequireServerEntropy)

MustSupportIssuedTokens = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MustSupportIssuedTokens'), QNameAssertionType, documentation=u'\n        10.1 Trust13 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1183, 2))
Namespace.addCategoryObject('elementBinding', MustSupportIssuedTokens.name().localName(), MustSupportIssuedTokens)

RequireRequestSecurityTokenCollection = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireRequestSecurityTokenCollection'), QNameAssertionType, documentation=u'\n        10.1 Trust13 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1190, 2))
Namespace.addCategoryObject('elementBinding', RequireRequestSecurityTokenCollection.name().localName(), RequireRequestSecurityTokenCollection)

RequireAppiesTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequireAppiesTo'), QNameAssertionType, documentation=u'\n        10.1 Trust13 Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 1197, 2))
Namespace.addCategoryObject('elementBinding', RequireAppiesTo.name().localName(), RequireAppiesTo)

UsernameToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'UsernameToken'), TokenAssertionType, documentation=u'\n        5.4.1 UsernameToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 120, 2))
Namespace.addCategoryObject('elementBinding', UsernameToken.name().localName(), UsernameToken)

IssuedToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IssuedToken'), IssuedTokenType, documentation=u'\n        5.4.2 IssuedToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 179, 2))
Namespace.addCategoryObject('elementBinding', IssuedToken.name().localName(), IssuedToken)

X509Token = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'X509Token'), TokenAssertionType, documentation=u'\n        5.4.3 X509Token Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 246, 2))
Namespace.addCategoryObject('elementBinding', X509Token.name().localName(), X509Token)

KerberosToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'KerberosToken'), TokenAssertionType, documentation=u'\n        5.4.4 KerberosToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 335, 2))
Namespace.addCategoryObject('elementBinding', KerberosToken.name().localName(), KerberosToken)

SpnegoContextToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SpnegoContextToken'), SpnegoContextTokenType, documentation=u'\n        5.4.5 SpnegoContextToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 362, 2))
Namespace.addCategoryObject('elementBinding', SpnegoContextToken.name().localName(), SpnegoContextToken)

SecurityContextToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SecurityContextToken'), TokenAssertionType, documentation=u'\n        5.4.6 SecurityContextToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 409, 2))
Namespace.addCategoryObject('elementBinding', SecurityContextToken.name().localName(), SecurityContextToken)

SecureConversationToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SecureConversationToken'), SecureConversationTokenType, documentation=u'\n        5.4.7 SecureConversationToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 435, 2))
Namespace.addCategoryObject('elementBinding', SecureConversationToken.name().localName(), SecureConversationToken)

SamlToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SamlToken'), TokenAssertionType, documentation=u'\n        5.4.8 SamlToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 474, 2))
Namespace.addCategoryObject('elementBinding', SamlToken.name().localName(), SamlToken)

RelToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelToken'), TokenAssertionType, documentation=u'\n        5.4.9 RelToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 508, 2))
Namespace.addCategoryObject('elementBinding', RelToken.name().localName(), RelToken)

HttpsToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'HttpsToken'), TokenAssertionType, documentation=u'\n        5.4.10 HttpsToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 549, 2))
Namespace.addCategoryObject('elementBinding', HttpsToken.name().localName(), HttpsToken)

KeyValueToken = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'KeyValueToken'), KeyValueTokenType, documentation=u'\n        5.4.11 KeyValueToken Assertion\n      ', location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 578, 2))
Namespace.addCategoryObject('elementBinding', KeyValueToken.name().localName(), KeyValueToken)



SePartsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Body'), EmptyType, scope=SePartsType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 53, 6)))

SePartsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Header'), HeaderType, scope=SePartsType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 54, 6)))

SePartsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Attachments'), EmptyType, scope=SePartsType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 55, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 53, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 54, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 55, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 56, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SePartsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Body')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 53, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(SePartsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Header')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 54, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(SePartsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Attachments')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 55, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 56, 6))
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
SePartsType._Automaton = _BuildAutomaton()




SerElementsType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'XPath'), pyxb.binding.datatypes.string, scope=SerElementsType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 90, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 91, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(SerElementsType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'XPath')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 90, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 91, 6))
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
SerElementsType._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 204, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 204, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
RequestSecurityTokenTemplateType._Automaton = _BuildAutomaton_2()




def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 616, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 616, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
NestedPolicyType._Automaton = _BuildAutomaton_3()




TokenAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Issuer'), _ImportedBinding__wsa.EndpointReferenceType, scope=TokenAssertionType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 130, 8)))

TokenAssertionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IssuerName'), pyxb.binding.datatypes.anyURI, scope=TokenAssertionType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 131, 8)))

def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 129, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 137, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TokenAssertionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Issuer')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 130, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(TokenAssertionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IssuerName')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 131, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 137, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
TokenAssertionType._Automaton = _BuildAutomaton_4()




IssuedTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Issuer'), _ImportedBinding__wsa.EndpointReferenceType, scope=IssuedTokenType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 189, 8)))

IssuedTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IssuerName'), pyxb.binding.datatypes.anyURI, scope=IssuedTokenType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 190, 8)))

IssuedTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RequestSecurityTokenTemplate'), RequestSecurityTokenTemplateType, scope=IssuedTokenType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 192, 6)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 188, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 197, 6))
    counters.add(cc_1)
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IssuedTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Issuer')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 189, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(IssuedTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IssuerName')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 190, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(IssuedTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'RequestSecurityTokenTemplate')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 192, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 197, 6))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
IssuedTokenType._Automaton = _BuildAutomaton_5()




SpnegoContextTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Issuer'), _ImportedBinding__wsa.EndpointReferenceType, scope=SpnegoContextTokenType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 372, 8)))

SpnegoContextTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IssuerName'), pyxb.binding.datatypes.anyURI, scope=SpnegoContextTokenType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 373, 8)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 371, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 379, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpnegoContextTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Issuer')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 372, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SpnegoContextTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IssuerName')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 373, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 379, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SpnegoContextTokenType._Automaton = _BuildAutomaton_6()




SecureConversationTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Issuer'), _ImportedBinding__wsa.EndpointReferenceType, scope=SecureConversationTokenType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 445, 8)))

SecureConversationTokenType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'IssuerName'), pyxb.binding.datatypes.anyURI, scope=SecureConversationTokenType, location=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 446, 8)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 444, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 452, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SecureConversationTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Issuer')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 445, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(SecureConversationTokenType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'IssuerName')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 446, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 452, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_2._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
SecureConversationTokenType._Automaton = _BuildAutomaton_7()




def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 591, 6))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702')), pyxb.utils.utility.Location(u'http://docs.oasis-open.org/ws-sx/ws-securitypolicy/200702/ws-securitypolicy-1.2.xsd', 591, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
KeyValueTokenType._Automaton = _BuildAutomaton_8()

