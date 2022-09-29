
>>> from plone.testing.z2 import Browser
>>> from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, TEST_USER_PASSWORD, setRoles, login
>>> from zope.component.hooks import setSite
>>> portal = layer['portal']
>>> browser = Browser(portal)
>>> portalURL = portal.absolute_url()
>>> spURL = portal.aq_parent.absolute_url()
>>> browser.open(portalURL)

Our SP is setup in the base of the zope site and is a plain acl_users
Try manual redirect url
>>> setSite(portal.aq_parent)
>>> # browser.open(spURL + '/acl_users/saml2sp/login')
>>> browser.open(spURL + '/manage')

Should redirect us to the idp site
>>> browser.url
'http://nohost/plone/acl_users/credentials_cookie_auth/require_login?came_from=http%3A//nohost/plone/acl_users/saml2sp/login'


>>> browser.getControl(name='__ac_name').value = TEST_USER_NAME
>>> browser.getControl(name='__ac_password').value = TEST_USER_PASSWORD
>>> browser.getControl(name='submit').click()

Logged in successfully
>>> print(browser.contents)
<!...
...Log out...
...You are now logged in...
...

TODO: shouldn't be login form
>>> browser.url
'http://nohost/plone'


