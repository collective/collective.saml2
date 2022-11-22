# ./_wsa.py
# -*- coding: utf-8 -*-
# PyXB bindings for NM:0ecbd27a42302a2dbf33a51269e14ce6419c0738
# Generated 2014-10-10 17:20:20.705614 by PyXB version 1.2.3
# Namespace http://www.w3.org/2005/08/addressing [xmlns:wsa]

import pyxb
import pyxb.binding
import pyxb.binding.saxer
import io
import pyxb.utils.utility
import pyxb.utils.domutils
import sys

# Unique identifier for bindings created at the same time
_GenerationUID = pyxb.utils.utility.UniqueIdentifier('urn:uuid:dbbe0922-5090-11e4-8d5b-3c77e646c78e')

# Import bindings for namespaces imported into schema
import pyxb.binding.datatypes

# NOTE: All namespace declarations are reserved within the binding
Namespace = pyxb.namespace.NamespaceForURI(u'http://www.w3.org/2005/08/addressing', create_if_missing=True)
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


# Atomic simple type: {http://www.w3.org/2005/08/addressing}RelationshipType
class RelationshipType (pyxb.binding.datatypes.anyURI, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RelationshipType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 64, 1)
    _Documentation = None
RelationshipType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RelationshipType, enum_prefix=None)
RelationshipType.httpwww_w3_org200508addressingreply = RelationshipType._CF_enumeration.addEnumeration(unicode_value=u'http://www.w3.org/2005/08/addressing/reply', tag=u'httpwww_w3_org200508addressingreply')
RelationshipType._InitializeFacetMap(RelationshipType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'RelationshipType', RelationshipType)

# Atomic simple type: {http://www.w3.org/2005/08/addressing}FaultCodesType
class FaultCodesType (pyxb.binding.datatypes.QName, pyxb.binding.basis.enumeration_mixin):

    """An atomic simple type."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FaultCodesType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 92, 1)
    _Documentation = None
FaultCodesType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FaultCodesType, enum_prefix=None)
FaultCodesType.tnsInvalidAddressingHeader = FaultCodesType._CF_enumeration.addEnumeration(unicode_value=u'tnsInvalidAddressingHeader', tag=u'tnsInvalidAddressingHeader')
FaultCodesType.tnsInvalidAddress = FaultCodesType._CF_enumeration.addEnumeration(unicode_value=u'tnsInvalidAddress', tag=u'tnsInvalidAddress')
FaultCodesType.tnsInvalidEPR = FaultCodesType._CF_enumeration.addEnumeration(unicode_value=u'tnsInvalidEPR', tag=u'tnsInvalidEPR')
FaultCodesType.tnsInvalidCardinality = FaultCodesType._CF_enumeration.addEnumeration(unicode_value=u'tnsInvalidCardinality', tag=u'tnsInvalidCardinality')
FaultCodesType.tnsMissingAddressInEPR = FaultCodesType._CF_enumeration.addEnumeration(unicode_value=u'tnsMissingAddressInEPR', tag=u'tnsMissingAddressInEPR')
FaultCodesType.tnsDuplicateMessageID = FaultCodesType._CF_enumeration.addEnumeration(unicode_value=u'tnsDuplicateMessageID', tag=u'tnsDuplicateMessageID')
FaultCodesType.tnsActionMismatch = FaultCodesType._CF_enumeration.addEnumeration(unicode_value=u'tnsActionMismatch', tag=u'tnsActionMismatch')
FaultCodesType.tnsMessageAddressingHeaderRequired = FaultCodesType._CF_enumeration.addEnumeration(unicode_value=u'tnsMessageAddressingHeaderRequired', tag=u'tnsMessageAddressingHeaderRequired')
FaultCodesType.tnsDestinationUnreachable = FaultCodesType._CF_enumeration.addEnumeration(unicode_value=u'tnsDestinationUnreachable', tag=u'tnsDestinationUnreachable')
FaultCodesType.tnsActionNotSupported = FaultCodesType._CF_enumeration.addEnumeration(unicode_value=u'tnsActionNotSupported', tag=u'tnsActionNotSupported')
FaultCodesType.tnsEndpointUnavailable = FaultCodesType._CF_enumeration.addEnumeration(unicode_value=u'tnsEndpointUnavailable', tag=u'tnsEndpointUnavailable')
FaultCodesType._InitializeFacetMap(FaultCodesType._CF_enumeration)
Namespace.addCategoryObject('typeBinding', u'FaultCodesType', FaultCodesType)

# Union simple type: {http://www.w3.org/2005/08/addressing}RelationshipTypeOpenEnum
# superclasses pyxb.binding.datatypes.anySimpleType
class RelationshipTypeOpenEnum (pyxb.binding.basis.STD_union):

    """Simple type that is a union of RelationshipType, pyxb.binding.datatypes.anyURI."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RelationshipTypeOpenEnum')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 60, 1)
    _Documentation = None

    _MemberTypes = ( RelationshipType, pyxb.binding.datatypes.anyURI, )
RelationshipTypeOpenEnum._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=RelationshipTypeOpenEnum)
RelationshipTypeOpenEnum._CF_pattern = pyxb.binding.facets.CF_pattern()
RelationshipTypeOpenEnum.httpwww_w3_org200508addressingreply = u'http://www.w3.org/2005/08/addressing/reply'# originally RelationshipType.httpwww_w3_org200508addressingreply
RelationshipTypeOpenEnum._InitializeFacetMap(RelationshipTypeOpenEnum._CF_enumeration,
   RelationshipTypeOpenEnum._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'RelationshipTypeOpenEnum', RelationshipTypeOpenEnum)

# Union simple type: {http://www.w3.org/2005/08/addressing}FaultCodesOpenEnumType
# superclasses pyxb.binding.datatypes.anySimpleType
class FaultCodesOpenEnumType (pyxb.binding.basis.STD_union):

    """Simple type that is a union of FaultCodesType, pyxb.binding.datatypes.QName."""

    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'FaultCodesOpenEnumType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 88, 1)
    _Documentation = None

    _MemberTypes = ( FaultCodesType, pyxb.binding.datatypes.QName, )
FaultCodesOpenEnumType._CF_enumeration = pyxb.binding.facets.CF_enumeration(value_datatype=FaultCodesOpenEnumType)
FaultCodesOpenEnumType._CF_pattern = pyxb.binding.facets.CF_pattern()
FaultCodesOpenEnumType.tnsInvalidAddressingHeader = u'tnsInvalidAddressingHeader'# originally FaultCodesType.tnsInvalidAddressingHeader
FaultCodesOpenEnumType.tnsInvalidAddress = u'tnsInvalidAddress'# originally FaultCodesType.tnsInvalidAddress
FaultCodesOpenEnumType.tnsInvalidEPR = u'tnsInvalidEPR'# originally FaultCodesType.tnsInvalidEPR
FaultCodesOpenEnumType.tnsInvalidCardinality = u'tnsInvalidCardinality'# originally FaultCodesType.tnsInvalidCardinality
FaultCodesOpenEnumType.tnsMissingAddressInEPR = u'tnsMissingAddressInEPR'# originally FaultCodesType.tnsMissingAddressInEPR
FaultCodesOpenEnumType.tnsDuplicateMessageID = u'tnsDuplicateMessageID'# originally FaultCodesType.tnsDuplicateMessageID
FaultCodesOpenEnumType.tnsActionMismatch = u'tnsActionMismatch'# originally FaultCodesType.tnsActionMismatch
FaultCodesOpenEnumType.tnsMessageAddressingHeaderRequired = u'tnsMessageAddressingHeaderRequired'# originally FaultCodesType.tnsMessageAddressingHeaderRequired
FaultCodesOpenEnumType.tnsDestinationUnreachable = u'tnsDestinationUnreachable'# originally FaultCodesType.tnsDestinationUnreachable
FaultCodesOpenEnumType.tnsActionNotSupported = u'tnsActionNotSupported'# originally FaultCodesType.tnsActionNotSupported
FaultCodesOpenEnumType.tnsEndpointUnavailable = u'tnsEndpointUnavailable'# originally FaultCodesType.tnsEndpointUnavailable
FaultCodesOpenEnumType._InitializeFacetMap(FaultCodesOpenEnumType._CF_enumeration,
   FaultCodesOpenEnumType._CF_pattern)
Namespace.addCategoryObject('typeBinding', u'FaultCodesOpenEnumType', FaultCodesOpenEnumType)

# Complex type {http://www.w3.org/2005/08/addressing}EndpointReferenceType with content type ELEMENT_ONLY
class EndpointReferenceType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/08/addressing}EndpointReferenceType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'EndpointReferenceType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 23, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/08/addressing}Address uses Python identifier Address
    __Address = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Address'), 'Address', '__httpwww_w3_org200508addressing_EndpointReferenceType_httpwww_w3_org200508addressingAddress', False, pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 25, 3), )

    
    Address = property(__Address.value, __Address.set, None, None)

    
    # Element {http://www.w3.org/2005/08/addressing}ReferenceParameters uses Python identifier ReferenceParameters
    __ReferenceParameters = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'ReferenceParameters'), 'ReferenceParameters', '__httpwww_w3_org200508addressing_EndpointReferenceType_httpwww_w3_org200508addressingReferenceParameters', False, pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 33, 1), )

    
    ReferenceParameters = property(__ReferenceParameters.value, __ReferenceParameters.set, None, None)

    
    # Element {http://www.w3.org/2005/08/addressing}Metadata uses Python identifier Metadata
    __Metadata = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), 'Metadata', '__httpwww_w3_org200508addressing_EndpointReferenceType_httpwww_w3_org200508addressingMetadata', False, pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 41, 1), )

    
    Metadata = property(__Metadata.value, __Metadata.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/08/addressing'))
    _HasWildcardElement = True
    _ElementMap.update({
        __Address.name() : __Address,
        __ReferenceParameters.name() : __ReferenceParameters,
        __Metadata.name() : __Metadata
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'EndpointReferenceType', EndpointReferenceType)


# Complex type {http://www.w3.org/2005/08/addressing}ReferenceParametersType with content type ELEMENT_ONLY
class ReferenceParametersType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/08/addressing}ReferenceParametersType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ReferenceParametersType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 34, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/08/addressing'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ReferenceParametersType', ReferenceParametersType)


# Complex type {http://www.w3.org/2005/08/addressing}MetadataType with content type ELEMENT_ONLY
class MetadataType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/08/addressing}MetadataType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'MetadataType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 42, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/08/addressing'))
    _HasWildcardElement = True
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'MetadataType', MetadataType)


# Complex type {http://www.w3.org/2005/08/addressing}AttributedURIType with content type SIMPLE
class AttributedURIType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/08/addressing}AttributedURIType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttributedURIType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 76, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/08/addressing'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AttributedURIType', AttributedURIType)


# Complex type {http://www.w3.org/2005/08/addressing}AttributedUnsignedLongType with content type SIMPLE
class AttributedUnsignedLongType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/08/addressing}AttributedUnsignedLongType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.unsignedLong
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttributedUnsignedLongType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 109, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.unsignedLong
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/08/addressing'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AttributedUnsignedLongType', AttributedUnsignedLongType)


# Complex type {http://www.w3.org/2005/08/addressing}AttributedQNameType with content type SIMPLE
class AttributedQNameType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/08/addressing}AttributedQNameType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.QName
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'AttributedQNameType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 118, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.QName
    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/08/addressing'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'AttributedQNameType', AttributedQNameType)


# Complex type {http://www.w3.org/2005/08/addressing}ProblemActionType with content type ELEMENT_ONLY
class ProblemActionType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/08/addressing}ProblemActionType with content type ELEMENT_ONLY"""
    _TypeDefinition = None
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_ELEMENT_ONLY
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'ProblemActionType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 129, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyType
    
    # Element {http://www.w3.org/2005/08/addressing}Action uses Python identifier Action
    __Action = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'Action'), 'Action', '__httpwww_w3_org200508addressing_ProblemActionType_httpwww_w3_org200508addressingAction', False, pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 74, 1), )

    
    Action = property(__Action.value, __Action.set, None, None)

    
    # Element {http://www.w3.org/2005/08/addressing}SoapAction uses Python identifier SoapAction
    __SoapAction = pyxb.binding.content.ElementDeclaration(pyxb.namespace.ExpandedName(Namespace, u'SoapAction'), 'SoapAction', '__httpwww_w3_org200508addressing_ProblemActionType_httpwww_w3_org200508addressingSoapAction', False, pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 132, 3), )

    
    SoapAction = property(__SoapAction.value, __SoapAction.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/08/addressing'))
    _ElementMap.update({
        __Action.name() : __Action,
        __SoapAction.name() : __SoapAction
    })
    _AttributeMap.update({
        
    })
Namespace.addCategoryObject('typeBinding', u'ProblemActionType', ProblemActionType)


# Complex type {http://www.w3.org/2005/08/addressing}RelatesToType with content type SIMPLE
class RelatesToType (pyxb.binding.basis.complexTypeDefinition):
    """Complex type {http://www.w3.org/2005/08/addressing}RelatesToType with content type SIMPLE"""
    _TypeDefinition = pyxb.binding.datatypes.anyURI
    _ContentTypeTag = pyxb.binding.basis.complexTypeDefinition._CT_SIMPLE
    _Abstract = False
    _ExpandedName = pyxb.namespace.ExpandedName(Namespace, u'RelatesToType')
    _XSDLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 51, 1)
    _ElementMap = {}
    _AttributeMap = {}
    # Base type is pyxb.binding.datatypes.anyURI
    
    # Attribute RelationshipType uses Python identifier RelationshipType
    __RelationshipType = pyxb.binding.content.AttributeUse(pyxb.namespace.ExpandedName(None, u'RelationshipType'), 'RelationshipType', '__httpwww_w3_org200508addressing_RelatesToType_RelationshipType', RelationshipTypeOpenEnum, unicode_default=u'http://www.w3.org/2005/08/addressing/reply')
    __RelationshipType._DeclarationLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 54, 4)
    __RelationshipType._UseLocation = pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 54, 4)
    
    RelationshipType = property(__RelationshipType.value, __RelationshipType.set, None, None)

    _AttributeWildcard = pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/08/addressing'))
    _ElementMap.update({
        
    })
    _AttributeMap.update({
        __RelationshipType.name() : __RelationshipType
    })
Namespace.addCategoryObject('typeBinding', u'RelatesToType', RelatesToType)


EndpointReference = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'EndpointReference'), EndpointReferenceType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 22, 1))
Namespace.addCategoryObject('elementBinding', EndpointReference.name().localName(), EndpointReference)

ReferenceParameters = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceParameters'), ReferenceParametersType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 33, 1))
Namespace.addCategoryObject('elementBinding', ReferenceParameters.name().localName(), ReferenceParameters)

Metadata = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), MetadataType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 41, 1))
Namespace.addCategoryObject('elementBinding', Metadata.name().localName(), Metadata)

MessageID = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'MessageID'), AttributedURIType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 49, 1))
Namespace.addCategoryObject('elementBinding', MessageID.name().localName(), MessageID)

ReplyTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReplyTo'), EndpointReferenceType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 70, 1))
Namespace.addCategoryObject('elementBinding', ReplyTo.name().localName(), ReplyTo)

From = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'From'), EndpointReferenceType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 71, 1))
Namespace.addCategoryObject('elementBinding', From.name().localName(), From)

FaultTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'FaultTo'), EndpointReferenceType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 72, 1))
Namespace.addCategoryObject('elementBinding', FaultTo.name().localName(), FaultTo)

To = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'To'), AttributedURIType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 73, 1))
Namespace.addCategoryObject('elementBinding', To.name().localName(), To)

Action = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Action'), AttributedURIType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 74, 1))
Namespace.addCategoryObject('elementBinding', Action.name().localName(), Action)

RetryAfter = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RetryAfter'), AttributedUnsignedLongType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 108, 1))
Namespace.addCategoryObject('elementBinding', RetryAfter.name().localName(), RetryAfter)

ProblemHeaderQName = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProblemHeaderQName'), AttributedQNameType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 117, 1))
Namespace.addCategoryObject('elementBinding', ProblemHeaderQName.name().localName(), ProblemHeaderQName)

ProblemIRI = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProblemIRI'), AttributedURIType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 126, 1))
Namespace.addCategoryObject('elementBinding', ProblemIRI.name().localName(), ProblemIRI)

ProblemAction = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ProblemAction'), ProblemActionType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 128, 1))
Namespace.addCategoryObject('elementBinding', ProblemAction.name().localName(), ProblemAction)

RelatesTo = pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'RelatesTo'), RelatesToType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 50, 1))
Namespace.addCategoryObject('elementBinding', RelatesTo.name().localName(), RelatesTo)



EndpointReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Address'), AttributedURIType, scope=EndpointReferenceType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 25, 3)))

EndpointReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'ReferenceParameters'), ReferenceParametersType, scope=EndpointReferenceType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 33, 1)))

EndpointReferenceType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Metadata'), MetadataType, scope=EndpointReferenceType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 41, 1)))

def _BuildAutomaton ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton
    del _BuildAutomaton
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 26, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 27, 3))
    counters.add(cc_1)
    cc_2 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 28, 3))
    counters.add(cc_2)
    states = []
    final_update = set()
    symbol = pyxb.binding.content.ElementUse(EndpointReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Address')), pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 25, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(EndpointReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'ReferenceParameters')), pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 26, 3))
    st_1 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_1)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(EndpointReferenceType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Metadata')), pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 27, 3))
    st_2 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_2)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_2, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=(pyxb.binding.content.Wildcard.NC_not, u'http://www.w3.org/2005/08/addressing')), pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 28, 3))
    st_3 = fac.State(symbol, is_initial=False, final_update=final_update, is_unordered_catenation=False)
    states.append(st_3)
    transitions = []
    transitions.append(fac.Transition(st_1, [
         ]))
    transitions.append(fac.Transition(st_2, [
         ]))
    transitions.append(fac.Transition(st_3, [
         ]))
    st_0._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_1, [
        fac.UpdateInstruction(cc_0, True) ]))
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_0, False) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_0, False) ]))
    st_1._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_2, [
        fac.UpdateInstruction(cc_1, True) ]))
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_1, False) ]))
    st_2._set_transitionSet(transitions)
    transitions = []
    transitions.append(fac.Transition(st_3, [
        fac.UpdateInstruction(cc_2, True) ]))
    st_3._set_transitionSet(transitions)
    return fac.Automaton(states, counters, False, containing_state=None)
EndpointReferenceType._Automaton = _BuildAutomaton()




def _BuildAutomaton_ ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_
    del _BuildAutomaton_
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 36, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 36, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
ReferenceParametersType._Automaton = _BuildAutomaton_()




def _BuildAutomaton_2 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_2
    del _BuildAutomaton_2
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=None, metadata=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 44, 3))
    counters.add(cc_0)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.WildcardUse(pyxb.binding.content.Wildcard(process_contents=pyxb.binding.content.Wildcard.PC_lax, namespace_constraint=pyxb.binding.content.Wildcard.NC_any), pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 44, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    transitions = []
    transitions.append(fac.Transition(st_0, [
        fac.UpdateInstruction(cc_0, True) ]))
    st_0._set_transitionSet(transitions)
    return fac.Automaton(states, counters, True, containing_state=None)
MetadataType._Automaton = _BuildAutomaton_2()




ProblemActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'Action'), AttributedURIType, scope=ProblemActionType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 74, 1)))

ProblemActionType._AddElement(pyxb.binding.basis.element(pyxb.namespace.ExpandedName(Namespace, u'SoapAction'), pyxb.binding.datatypes.anyURI, scope=ProblemActionType, location=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 132, 3)))

def _BuildAutomaton_3 ():
    # Remove this helper function from the namespace after it is invoked
    global _BuildAutomaton_3
    del _BuildAutomaton_3
    import pyxb.utils.fac as fac

    counters = set()
    cc_0 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 131, 3))
    counters.add(cc_0)
    cc_1 = fac.CounterCondition(min=0, max=1, metadata=pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 132, 3))
    counters.add(cc_1)
    states = []
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_0, False))
    symbol = pyxb.binding.content.ElementUse(ProblemActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'Action')), pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 131, 3))
    st_0 = fac.State(symbol, is_initial=True, final_update=final_update, is_unordered_catenation=False)
    states.append(st_0)
    final_update = set()
    final_update.add(fac.UpdateInstruction(cc_1, False))
    symbol = pyxb.binding.content.ElementUse(ProblemActionType._UseForTag(pyxb.namespace.ExpandedName(Namespace, u'SoapAction')), pyxb.utils.utility.Location(u'http://www.w3.org/2006/03/addressing/ws-addr.xsd', 132, 3))
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
ProblemActionType._Automaton = _BuildAutomaton_3()

