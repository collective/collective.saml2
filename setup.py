from setuptools import setup, find_packages

version = '1.0'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTING.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='collective.saml2',
      version=version,
      description="Installation of SAML2 web single-sign-on for Plone (dm.zope.saml2)",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='Plone Python',
      author='Pretaweb',
      author_email='support@pretaweb.com',
      url='http://github.com/collective/collective.listingviews',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=['collective', ],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'dm.saml2 > 2.0.4',
          'dm.zope.saml2 > 2.0b7',
          'PyXB == 1.2.3',#maybe it is not necessary. But bindings may not be compatible between versions 
          'dm.xmlsec.binding > 1.1',
          'zope.app.component'#until import in dm.zope.saml2 is not fixed
      ],
      extras_require={'test': ['plone.app.testing']},
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
