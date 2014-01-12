from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import applyProfile
from zope.configuration import xmlconfig


class CollectiveSAML2(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import collective.saml2
        xmlconfig.file('configure.zcml',
                       collective.saml2,
                       context=configurationContext)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'collective.saml2:default')

COLLECTIVE_SAML2_FIXTURE = CollectiveSAML2()
COLLECTIVE_SAML2_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_SAML2_FIXTURE, ),
                       name="CollectiveSAML2:Integration")
