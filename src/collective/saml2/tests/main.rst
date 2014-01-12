
>>> from plone.testing.z2 import Browser
>>> from plone.app.testing import TEST_USER_ID, TEST_USER_NAME, TEST_USER_PASSWORD, setRoles, login
>>> portal = layer['portal']
>>> browser = Browser(portal)
>>> portalURL = portal.absolute_url()
>>> browser.open(portalURL)

>>> browser.open(portal.absolute_url()+'/@@saml2_controlpanel')

>>> browser.getControl(name='__ac_name').value = TEST_USER_NAME
>>> browser.getControl(name='__ac_password').value = TEST_USER_PASSWORD
>>> browser.getControl(name='submit').click()
