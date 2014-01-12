import unittest2 as unittest
import doctest
from collective.saml2.testing import\
    COLLECTIVE_SAML2_INTEGRATION_TESTING



OPTIONFLAGS = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE


def test_suite():
    suite = unittest.TestSuite()
#    seltest = doctest.DocFileSuite('selenium.rst', optionflags=OPTIONFLAGS)
    # Run selenium tests on level 2, as it requires a correctly configured
    # Firefox browser
#    seltest.level = 2
    layer = COLLECTIVE_SAML2_INTEGRATION_TESTING
    suite.addTests([
        doctest.DocFileSuite('tests/main.rst', optionflags=OPTIONFLAGS, globs=dict(layer=layer)),
    ])
    suite.layer = COLLECTIVE_SAML2_INTEGRATION_TESTING
    return suite