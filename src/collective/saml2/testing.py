from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import applyProfile
from plone.app.testing.helpers import ploneSite
from plone.app.testing.helpers import pushGlobalRegistry
from plone.app.testing.helpers import persist_profile_upgrade_versions
from zope import site

from zope.configuration import xmlconfig
from zope.component.hooks import setHooks
from zope.component.hooks import setSite
from plone.testing import security
from Products.PluggableAuthService.interfaces.plugins import IChallengePlugin

# from zope.component import createObject


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

        # create authority
        # 1. In the ZMI Add at the Plone root a "Saml authority" object.
        # portal.manage_addProduct['dm.zope.saml2'].add_SamlAuthority("authority", "saml2 auth")
        from dm.zope.saml2.authority import SamlAuthority
        auth = SamlAuthority(title="My Auth", base_url=portal.absolute_url(), entity_id="TestIdP")
        # 2. Give it the id "saml2auth". It doesn't matter really what it's called but
        #    it will appear in the public `metadata`_ url you will give to the owners of
        #    other services
        auth.id = "saml2auth"
        portal._setObject(auth.id, auth)
        idp_metadata = portal.saml2auth.absolute_url() + "/metadata"
        # 3. Entity id. This is important. This is an id that should uniquely identify
        #    your service from other services that are part of the SSO network. For
        #    example if your and the IdP with 10 different services using you for
        #    authentication, your entity id will have to be unique.

        # Create IdP
        from dm.zope.saml2.idpsso.idpsso import SimpleIdpssoAp
        idp = SimpleIdpssoAp()
        portal._setObject('saml2idp', idp)

        # TODO: create 2nd site or 2nd acl_users which will cause login

        # For now we will use the root of zope as our IdP
        parent = portal.aq_parent
        # self.setupPlone2()
        # plone2 = parent.plone2
        sp_site = parent

        # Make root zope a site
        sm = site.LocalSiteManager(sp_site)
        sp_site.setSiteManager(sm)
        setSite(sp_site)

        auth_sp = SamlAuthority(title="My SP Auth", base_url=parent.absolute_url(), entity_id="TestSP")
        sp_site._setObject("saml2auth_sp", auth_sp)
        sp_metadata = sp_site.saml2auth_sp.absolute_url() + "/metadata"

        from dm.zope.saml2.spsso.plugin import IntegratedSimpleSpssoPlugin
        sp = IntegratedSimpleSpssoPlugin()
        zcuf = sp_site._getOb("acl_users")
        zcuf._setObject('saml2sp', sp)

        # TODO: active PAS plugins in SP. Challenge plugin. make sure its top
        plugins = zcuf._getOb('plugins')
        plugins.activatePlugin(IChallengePlugin, 'saml2sp')
        # plugins.activatePlugin( IAuthenticationPlugin, 'login' )

        # authorise the metadata connections
        from dm.zope.saml2.entity import EntityByUrl
        idp_connection = EntityByUrl(url=idp_metadata)
        idp_connection.id = "TestIdP"
        # Important: Must be the same id as entityid for our IdP
        sp_site.saml2auth_sp._setObject(idp_connection.id, idp_connection,)

        # put in the idp metadata url and activate
        sp_connection = EntityByUrl(url=sp_metadata)
        sp_connection.id = "TestSP"
        portal.saml2auth._setObject(sp_connection.id, sp_connection)

        # TODO: setup the trust connection IdP to SP

        self.showErrors(portal)

    def showErrors(self, portal):

        portal.error_log._ignored_exceptions = ()

        def raising(self, info):
            import traceback
            traceback.print_tb(info[2])
            print info[1]

        from Products.SiteErrorLog.SiteErrorLog import SiteErrorLog
        SiteErrorLog.raising = raising

    def setupPlone2(self):
        import plone.app.testing.helpers

        # HACK
        plone.app.testing.helpers.PLONE_SITE_ID = "plone2"
        with ploneSite() as portal:
            setHooks()

            # Make sure there's no local site manager while we load ZCML
            setSite(None)

            # Push a new component registry so that ZCML registations
            # and other global component registry changes are sandboxed
            pushGlobalRegistry(portal)

            # Persist GenericSetup profile upgrade versions for easy
            # rollback.
            persist_profile_upgrade_versions(portal)

            # Make sure zope.security checkers can be set up and torn down
            # reliably

            security.pushCheckers()

            from Products.PluggableAuthService.PluggableAuthService import MultiPlugins  # noqa

            # preSetupMultiPlugins = MultiPlugins[:]

            # Allow subclass to load ZCML and products
            # self.setUpZope(portal.getPhysicalRoot(), configurationContext)

            # Allow subclass to configure a persistent fixture
            setSite(portal)
            # self.setUpPloneSite(portal)
            setSite(None)
        # HACK
        plone.app.testing.helpers.PLONE_SITE_ID = "plone"


COLLECTIVE_SAML2_FIXTURE = CollectiveSAML2()
COLLECTIVE_SAML2_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(COLLECTIVE_SAML2_FIXTURE, ),
                       name="CollectiveSAML2:Integration")
