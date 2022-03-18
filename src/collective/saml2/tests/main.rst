
>>> from plone.testing.z2 import Browser
>>> from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, TEST_USER_PASSWORD, setRoles, login
>>> portal = layer['portal']
>>> browser = Browser(portal)
>>> portalURL = portal.absolute_url()
>>> browser.open(portalURL)

Try manual redirect url
>>> browser.open(portal.absolute_url()+'/acl_users/saml2sp/login')

Should redirect us back to the same site
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


