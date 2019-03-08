# ./_auth.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:99e26faa7115afe236fd70b28dddaf1784b16d87
# Generated 2014-10-10 17:20:20.705469 by PyXB version 1.2.3
# Namespace http://docs.oasis-open.org/wsfed/authorization/200706 [xmlns:auth]

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
#import _xenc as _ImportedBinding__xenc
import pyxb.bundles.wssplat.raw.xenc as _ImportedBinding__xenc 

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://docs.oasis-open.org/wsfed/authorization/200706', create_if_missing=True)
Namespace.configureCategories(['typeBinding', 'elementBinding'])
_Namespace_xenc = _ImportedBinding__xenc.Namespace
_Namespace_xenc.configureCategories(['typeBinding', 'elementBinding'])

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


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}AdditionalContextType with content type ELEMENT_ONLY
class AdditionalContextType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}AdditionalContextType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AdditionalContextType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 34, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ContextItem uses Python identifier ContextItem
    __ContextItem = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ContextItem'), 'ContextItem', '__httpdocs_oasis_open_orgwsfedauthorization200706_AdditionalContextType_httpdocs_oasis_open_orgwsfedauthorization200706ContextItem', True, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 36, 6), )

    
    ContextItem = property(__ContextItem.value, __ContextItem.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        __ContextItem.name() : __ContextItem
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AdditionalContextType', AdditionalContextType)


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ContextItemType with content type ELEMENT_ONLY
class ContextItemType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ContextItemType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ContextItemType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 42, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpdocs_oasis_open_orgwsfedauthorization200706_ContextItemType_httpdocs_oasis_open_orgwsfedauthorization200706Value', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 44, 6), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Attribute Name uses Python identifier Name
    __Name = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Name'), 'Name', '__httpdocs_oasis_open_orgwsfedauthorization200706_ContextItemType_Name', pyxb.binding.datatypes.anyURI, required=True)
    __Name._DeclarationLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 47, 4)
    __Name._UseLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 47, 4)
    
    Name = property(__Name.value, __Name.set, None, None)

    
    # Attribute Scope uses Python identifier Scope
    __Scope = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Scope'), 'Scope', '__httpdocs_oasis_open_orgwsfedauthorization200706_ContextItemType_Scope', pyxb.binding.datatypes.anyURI)
    __Scope._DeclarationLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 48, 1)
    __Scope._UseLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 48, 1)
    
    Scope = property(__Scope.value, __Scope.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        __Value.name() : __Value
    })
    _AttributeMap.update({
        __Name.name() : __Name,
        __Scope.name() : __Scope
    })
Namespace.addCategoryObject('typeBinding', u'ContextItemType', ContextItemType)


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ClaimType with content type ELEMENT_ONLY
class ClaimType_ (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ClaimType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ClaimType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 54, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}DisplayName uses Python identifier DisplayName
    __DisplayName = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DisplayName'), 'DisplayName', '__httpdocs_oasis_open_orgwsfedauthorization200706_ClaimType__httpdocs_oasis_open_orgwsfedauthorization200706DisplayName', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 56, 6), )

    
    DisplayName = property(__DisplayName.value, __DisplayName.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}Description uses Python identifier Description
    __Description = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Description'), 'Description', '__httpdocs_oasis_open_orgwsfedauthorization200706_ClaimType__httpdocs_oasis_open_orgwsfedauthorization200706Description', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 57, 6), )

    
    Description = property(__Description.value, __Description.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}DisplayValue uses Python identifier DisplayValue
    __DisplayValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'DisplayValue'), 'DisplayValue', '__httpdocs_oasis_open_orgwsfedauthorization200706_ClaimType__httpdocs_oasis_open_orgwsfedauthorization200706DisplayValue', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 58, 6), )

    
    DisplayValue = property(__DisplayValue.value, __DisplayValue.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpdocs_oasis_open_orgwsfedauthorization200706_ClaimType__httpdocs_oasis_open_orgwsfedauthorization200706Value', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 60, 7), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}EncryptedValue uses Python identifier EncryptedValue
    __EncryptedValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'EncryptedValue'), 'EncryptedValue', '__httpdocs_oasis_open_orgwsfedauthorization200706_ClaimType__httpdocs_oasis_open_orgwsfedauthorization200706EncryptedValue', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 61, 8), )

    
    EncryptedValue = property(__EncryptedValue.value, __EncryptedValue.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}StructuredValue uses Python identifier StructuredValue
    __StructuredValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StructuredValue'), 'StructuredValue', '__httpdocs_oasis_open_orgwsfedauthorization200706_ClaimType__httpdocs_oasis_open_orgwsfedauthorization200706StructuredValue', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 62, 8), )

    
    StructuredValue = property(__StructuredValue.value, __StructuredValue.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ConstrainedValue uses Python identifier ConstrainedValue
    __ConstrainedValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ConstrainedValue'), 'ConstrainedValue', '__httpdocs_oasis_open_orgwsfedauthorization200706_ClaimType__httpdocs_oasis_open_orgwsfedauthorization200706ConstrainedValue', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 63, 8), )

    
    ConstrainedValue = property(__ConstrainedValue.value, __ConstrainedValue.set, None, None)

    
    # Attribute Uri uses Python identifier Uri
    __Uri = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Uri'), 'Uri', '__httpdocs_oasis_open_orgwsfedauthorization200706_ClaimType__Uri', pyxb.binding.datatypes.anyURI, required=True)
    __Uri._DeclarationLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 67, 1)
    __Uri._UseLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 67, 1)
    
    Uri = property(__Uri.value, __Uri.set, None, None)

    
    # Attribute Optional uses Python identifier Optional
    __Optional = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'Optional'), 'Optional', '__httpdocs_oasis_open_orgwsfedauthorization200706_ClaimType__Optional', pyxb.binding.datatypes.boolean)
    __Optional._DeclarationLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 68, 1)
    __Optional._UseLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 68, 1)
    
    Optional = property(__Optional.value, __Optional.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        __DisplayName.name() : __DisplayName,
        __Description.name() : __Description,
        __DisplayValue.name() : __DisplayValue,
        __Value.name() : __Value,
        __EncryptedValue.name() : __EncryptedValue,
        __StructuredValue.name() : __StructuredValue,
        __ConstrainedValue.name() : __ConstrainedValue
    })
    _AttributeMap.update({
        __Uri.name() : __Uri,
        __Optional.name() : __Optional
    })
Namespace.addCategoryObject('typeBinding', u'ClaimType', ClaimType_)


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}DisplayNameType with content type SIMPLE
class DisplayNameType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}DisplayNameType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DisplayNameType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 72, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'DisplayNameType', DisplayNameType)


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}DescriptionType with content type SIMPLE
class DescriptionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}DescriptionType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DescriptionType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 79, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'DescriptionType', DescriptionType)


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}DisplayValueType with content type SIMPLE
class DisplayValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}DisplayValueType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.string
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'DisplayValueType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 86, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.string
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'DisplayValueType', DisplayValueType)


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}EncryptedValueType with content type ELEMENT_ONLY
class EncryptedValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}EncryptedValueType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EncryptedValueType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 94, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2001/04/xmlenc#}EncryptedData uses Python identifier EncryptedData
    __EncryptedData = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(_Namespace_xenc, u'EncryptedData'), 'EncryptedData', '__httpdocs_oasis_open_orgwsfedauthorization200706_EncryptedValueType_httpwww_w3_org200104xmlencEncryptedData', False, pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmlenc-core-20021210/xenc-schema.xsd', 72, 2), )

    
    EncryptedData = property(__EncryptedData.value, __EncryptedData.set, None, None)

    
    # Attribute DecryptionCondition uses Python identifier DecryptionCondition
    __DecryptionCondition = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'DecryptionCondition'), 'DecryptionCondition', '__httpdocs_oasis_open_orgwsfedauthorization200706_EncryptedValueType_DecryptionCondition', pyxb.binding.datatypes.anyURI)
    __DecryptionCondition._DeclarationLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 98, 4)
    __DecryptionCondition._UseLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 98, 4)
    
    DecryptionCondition = property(__DecryptionCondition.value, __DecryptionCondition.set, None, None)

    _ElementMap.update({
        __EncryptedData.name() : __EncryptedData
    })
    _AttributeMap.update({
        __DecryptionCondition.name() : __DecryptionCondition
    })
Namespace.addCategoryObject('typeBinding', u'EncryptedValueType', EncryptedValueType)


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}StructuredValueType with content type ELEMENT_ONLY
class StructuredValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}StructuredValueType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'StructuredValueType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 101, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'StructuredValueType', StructuredValueType)


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ConstrainedValueType with content type ELEMENT_ONLY
class ConstrainedValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ConstrainedValueType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ConstrainedValueType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 110, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ValueLessThan uses Python identifier ValueLessThan
    __ValueLessThan = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ValueLessThan'), 'ValueLessThan', '__httpdocs_oasis_open_orgwsfedauthorization200706_ConstrainedValueType_httpdocs_oasis_open_orgwsfedauthorization200706ValueLessThan', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 113, 8), )

    
    ValueLessThan = property(__ValueLessThan.value, __ValueLessThan.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ValueLessThanOrEqual uses Python identifier ValueLessThanOrEqual
    __ValueLessThanOrEqual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ValueLessThanOrEqual'), 'ValueLessThanOrEqual', '__httpdocs_oasis_open_orgwsfedauthorization200706_ConstrainedValueType_httpdocs_oasis_open_orgwsfedauthorization200706ValueLessThanOrEqual', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 114, 8), )

    
    ValueLessThanOrEqual = property(__ValueLessThanOrEqual.value, __ValueLessThanOrEqual.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ValueGreaterThan uses Python identifier ValueGreaterThan
    __ValueGreaterThan = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ValueGreaterThan'), 'ValueGreaterThan', '__httpdocs_oasis_open_orgwsfedauthorization200706_ConstrainedValueType_httpdocs_oasis_open_orgwsfedauthorization200706ValueGreaterThan', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 115, 8), )

    
    ValueGreaterThan = property(__ValueGreaterThan.value, __ValueGreaterThan.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ValueGreaterThanOrEqual uses Python identifier ValueGreaterThanOrEqual
    __ValueGreaterThanOrEqual = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ValueGreaterThanOrEqual'), 'ValueGreaterThanOrEqual', '__httpdocs_oasis_open_orgwsfedauthorization200706_ConstrainedValueType_httpdocs_oasis_open_orgwsfedauthorization200706ValueGreaterThanOrEqual', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 116, 8), )

    
    ValueGreaterThanOrEqual = property(__ValueGreaterThanOrEqual.value, __ValueGreaterThanOrEqual.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ValueInRangen uses Python identifier ValueInRangen
    __ValueInRangen = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ValueInRangen'), 'ValueInRangen', '__httpdocs_oasis_open_orgwsfedauthorization200706_ConstrainedValueType_httpdocs_oasis_open_orgwsfedauthorization200706ValueInRangen', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 117, 8), )

    
    ValueInRangen = property(__ValueInRangen.value, __ValueInRangen.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ValueOneOf uses Python identifier ValueOneOf
    __ValueOneOf = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ValueOneOf'), 'ValueOneOf', '__httpdocs_oasis_open_orgwsfedauthorization200706_ConstrainedValueType_httpdocs_oasis_open_orgwsfedauthorization200706ValueOneOf', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 118, 8), )

    
    ValueOneOf = property(__ValueOneOf.value, __ValueOneOf.set, None, None)

    
    # Attribute AssertConstraint uses Python identifier AssertConstraint
    __AssertConstraint = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'AssertConstraint'), 'AssertConstraint', '__httpdocs_oasis_open_orgwsfedauthorization200706_ConstrainedValueType_AssertConstraint', pyxb.binding.datatypes.boolean)
    __AssertConstraint._DeclarationLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 122, 4)
    __AssertConstraint._UseLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 122, 4)
    
    AssertConstraint = property(__AssertConstraint.value, __AssertConstraint.set, None, None)

    _HasWildcardElement = True
    _ElementMap.update({
        __ValueLessThan.name() : __ValueLessThan,
        __ValueLessThanOrEqual.name() : __ValueLessThanOrEqual,
        __ValueGreaterThan.name() : __ValueGreaterThan,
        __ValueGreaterThanOrEqual.name() : __ValueGreaterThanOrEqual,
        __ValueInRangen.name() : __ValueInRangen,
        __ValueOneOf.name() : __ValueOneOf
    })
    _AttributeMap.update({
        __AssertConstraint.name() : __AssertConstraint
    })
Namespace.addCategoryObject('typeBinding', u'ConstrainedValueType', ConstrainedValueType)


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ValueInRangeType with content type ELEMENT_ONLY
class ValueInRangeType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ValueInRangeType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ValueInRangeType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 124, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ValueUpperBound uses Python identifier ValueUpperBound
    __ValueUpperBound = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ValueUpperBound'), 'ValueUpperBound', '__httpdocs_oasis_open_orgwsfedauthorization200706_ValueInRangeType_httpdocs_oasis_open_orgwsfedauthorization200706ValueUpperBound', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 126, 6), )

    
    ValueUpperBound = property(__ValueUpperBound.value, __ValueUpperBound.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}ValueLowerBound uses Python identifier ValueLowerBound
    __ValueLowerBound = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ValueLowerBound'), 'ValueLowerBound', '__httpdocs_oasis_open_orgwsfedauthorization200706_ValueInRangeType_httpdocs_oasis_open_orgwsfedauthorization200706ValueLowerBound', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 127, 6), )

    
    ValueLowerBound = property(__ValueLowerBound.value, __ValueLowerBound.set, None, None)

    _ElementMap.update({
        __ValueUpperBound.name() : __ValueUpperBound,
        __ValueLowerBound.name() : __ValueLowerBound
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ValueInRangeType', ValueInRangeType)


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ConstrainedSingleValueType with content type ELEMENT_ONLY
class ConstrainedSingleValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ConstrainedSingleValueType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ConstrainedSingleValueType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 131, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpdocs_oasis_open_orgwsfedauthorization200706_ConstrainedSingleValueType_httpdocs_oasis_open_orgwsfedauthorization200706Value', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 133, 6), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}StructuredValue uses Python identifier StructuredValue
    __StructuredValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StructuredValue'), 'StructuredValue', '__httpdocs_oasis_open_orgwsfedauthorization200706_ConstrainedSingleValueType_httpdocs_oasis_open_orgwsfedauthorization200706StructuredValue', False, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 134, 6), )

    
    StructuredValue = property(__StructuredValue.value, __StructuredValue.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value,
        __StructuredValue.name() : __StructuredValue
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ConstrainedSingleValueType', ConstrainedSingleValueType)


# Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ConstrainedManyValueType with content type ELEMENT_ONLY
class ConstrainedManyValueType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://docs.oasis-open.org/wsfed/authorization/200706}ConstrainedManyValueType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ConstrainedManyValueType')
    _XSDLocation = pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 138, 2)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}Value uses Python identifier Value
    __Value = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Value'), 'Value', '__httpdocs_oasis_open_orgwsfedauthorization200706_ConstrainedManyValueType_httpdocs_oasis_open_orgwsfedauthorization200706Value', True, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 140, 6), )

    
    Value = property(__Value.value, __Value.set, None, None)

    
    # Element {http://docs.oasis-open.org/wsfed/authorization/200706}StructuredValue uses Python identifier StructuredValue
    __StructuredValue = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'StructuredValue'), 'StructuredValue', '__httpdocs_oasis_open_orgwsfedauthorization200706_ConstrainedManyValueType_httpdocs_oasis_open_orgwsfedauthorization200706StructuredValue', True, pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 141, 6), )

    
    StructuredValue = property(__StructuredValue.value, __StructuredValue.set, None, None)

    _ElementMap.update({
        __Value.name() : __Value,
        __StructuredValue.name() : __StructuredValue
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ConstrainedManyValueType', ConstrainedManyValueType)


AdditionalContext = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'AdditionalContext'), AdditionalContextType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 33, 2))
Namespace.addCategoryObject('elementBinding', AdditionalContext.name().localName(), AdditionalContext)

ClaimType = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ClaimType'), ClaimType_, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 53, 2))
Namespace.addCategoryObject('elementBinding', ClaimType.name().localName(), ClaimType)



AdditionalContextType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ContextItem'), ContextItemType, scope=AdditionalContextType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 36, 6)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 36, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=None, metadata=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 37, 6))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(AdditionalContextType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ContextItem')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 36, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 37, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_1, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
AdditionalContextType._Automaton = _BuildAutomaton()




ContextItemType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.string, scope=ContextItemType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 44, 6)))

def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 43, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ContextItemType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 44, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 45, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ContextItemType._Automaton = _BuildAutomaton_()




ClaimType_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DisplayName'), DisplayNameType, scope=ClaimType_, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 56, 6)))

ClaimType_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Description'), DescriptionType, scope=ClaimType_, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 57, 6)))

ClaimType_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'DisplayValue'), DisplayValueType, scope=ClaimType_, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 58, 6)))

ClaimType_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.string, scope=ClaimType_, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 60, 7)))

ClaimType_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EncryptedValue'), EncryptedValueType, scope=ClaimType_, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 61, 8)))

ClaimType_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StructuredValue'), StructuredValueType, scope=ClaimType_, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 62, 8)))

ClaimType_._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ConstrainedValue'), ConstrainedValueType, scope=ClaimType_, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 63, 8)))

def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 56, 6))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 57, 6))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0L, max=1L, metadata=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 58, 6))
    counters.add(cc_2)
    cc_3 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 59, 6))
    counters.add(cc_3)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ClaimType_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DisplayName')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 56, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ClaimType_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Description')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 57, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.ElementUse(ClaimType_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'DisplayValue')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 58, 6))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClaimType_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 60, 7))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClaimType_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'EncryptedValue')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 61, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClaimType_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StructuredValue')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 62, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.ElementUse(ClaimType_._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ConstrainedValue')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 63, 8))
    st_6 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_3, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 64, 8))
    st_7 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_7)
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
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_6._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_4, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_5, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_6, [
        fac.UpdateInstruction(cc_3, True) ]))
    transitions.append(fac.Transition(st_7, [
        fac.UpdateInstruction(cc_3, True) ]))
    st_7._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ClaimType_._Automaton = _BuildAutomaton_2()




EncryptedValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(_Namespace_xenc, u'EncryptedData'), _ImportedBinding__xenc.EncryptedDataType, scope=EncryptedValueType, location=pyxb.utils.utility.Location(u'http://www.w3.org/TR/2002/REC-xmlenc-core-20021210/xenc-schema.xsd', 72, 2)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EncryptedValueType._UseForTag(pyxb.namespace.ExpandedName(_Namespace_xenc, u'EncryptedData')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 96, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EncryptedValueType._Automaton = _BuildAutomaton_3()




def _BuildAutomaton_4 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_4
    del _BuildAutomaton_4
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 103, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
StructuredValueType._Automaton = _BuildAutomaton_4()




ConstrainedValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueLessThan'), ConstrainedSingleValueType, scope=ConstrainedValueType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 113, 8)))

ConstrainedValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueLessThanOrEqual'), ConstrainedSingleValueType, scope=ConstrainedValueType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 114, 8)))

ConstrainedValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueGreaterThan'), ConstrainedSingleValueType, scope=ConstrainedValueType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 115, 8)))

ConstrainedValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueGreaterThanOrEqual'), ConstrainedSingleValueType, scope=ConstrainedValueType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 116, 8)))

ConstrainedValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueInRangen'), ValueInRangeType, scope=ConstrainedValueType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 117, 8)))

ConstrainedValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueOneOf'), ConstrainedManyValueType, scope=ConstrainedValueType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 118, 8)))

def _BuildAutomaton_5 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_5
    del _BuildAutomaton_5
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstrainedValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValueLessThan')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 113, 8))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstrainedValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValueLessThanOrEqual')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 114, 8))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstrainedValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValueGreaterThan')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 115, 8))
    st_2 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstrainedValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValueGreaterThanOrEqual')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 116, 8))
    st_3 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstrainedValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValueInRangen')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 117, 8))
    st_4 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_4)
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ConstrainedValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValueOneOf')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 118, 8))
    st_5 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_5)
    final_update = set()
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://docs.oasis-open.org/wsfed/authorization/200706')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 120, 6))
    st_6 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_6)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_3._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_4._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_5._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_6, [
         ]))
    st_6._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ConstrainedValueType._Automaton = _BuildAutomaton_5()




ValueInRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueUpperBound'), ConstrainedSingleValueType, scope=ValueInRangeType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 126, 6)))

ValueInRangeType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ValueLowerBound'), ConstrainedSingleValueType, scope=ValueInRangeType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 127, 6)))

def _BuildAutomaton_6 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_6
    del _BuildAutomaton_6
    import pyxb.utils.fac as fac

    counters = set()
    states = []
    final_update = None
    symbol = pyxb.binding.content.ElementUse(ValueInRangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValueUpperBound')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 126, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(ValueInRangeType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ValueLowerBound')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 127, 6))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
ValueInRangeType._Automaton = _BuildAutomaton_6()




ConstrainedSingleValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.string, scope=ConstrainedSingleValueType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 133, 6)))

ConstrainedSingleValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StructuredValue'), StructuredValueType, scope=ConstrainedSingleValueType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 134, 6)))

def _BuildAutomaton_7 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_7
    del _BuildAutomaton_7
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 132, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConstrainedSingleValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 133, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConstrainedSingleValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StructuredValue')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 134, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ConstrainedSingleValueType._Automaton = _BuildAutomaton_7()




ConstrainedManyValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Value'), pyxb.binding.datatypes.string, scope=ConstrainedManyValueType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 140, 6)))

ConstrainedManyValueType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'StructuredValue'), StructuredValueType, scope=ConstrainedManyValueType, location=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 141, 6)))

def _BuildAutomaton_8 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_8
    del _BuildAutomaton_8
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0L, max=1, metadata=pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 139, 4))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConstrainedManyValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Value')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 140, 6))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ConstrainedManyValueType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'StructuredValue')), pyxb.utils.utility.Location(u'/data/federation/ws-authorization.xsd', 141, 6))
    st_1 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    transitions = []
    transitions.append(fac.Transition(st_0, [
         ]))
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_1._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ConstrainedManyValueType._Automaton = _BuildAutomaton_8()

