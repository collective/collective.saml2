.. contents::

Introduction
============


What is SAML2 
------------------------

SAML2 is a single sign on standard. It allows for the following use cases (depending how its configured)

- A user can log into plone without entering their password
- A user could log into another website using their credentials registered in plone
- Two plone sites can be connected together such that you can log into one by having the login happen in the other Plone site (or no login at all if the user is already logged in there).

All this is done via redirects in the browser with no direct connection needed between the two web servers. This means, unlike LDAP you can have an external website be authenticated by an internal intranet SAML2 complaint identity provider (such as ADFS) without having to setup a VPN connection between the servers.

What SAML2 doesn't do
---------------------

It doesn't provide a way to search users or groups. It's not a directory service. Anything in plone that requires listing users or groups will not give you accurate information.


What does collective.saml2 do 
-----------------------------

This plugin is mainly a wrapper around `dm.zope.saml2`_ to aid in installation
for a Plone environment. All the hard work is done by Dieter Maurer's excellent
`dm.zope.saml2`_.

This plugin does the following so far

- ensure the dependencies for `dm.zope.saml2`_ are installed
- provide an `example buildout`_ to build all the dependencies standalone
- document how to configure `dm.zope.saml2`_
- a patch to activate the encryption type
- a patch to remove the need for zope sessions or transactions during login

In the future we hope to also include a control panel to

- help configure a Plone site as either a IdP or a SP
- managing services including manual configuration (without `metadata`_ urls)
- management of keys TTW
- some tests to ensure comparability with Plone

Building
========

Unfortunately `dm.zope.saml2`_ was written requiring many dependencies some of
which are c-extensions requiring some libraries.

- `dm.saml2`_
- `dm.reuse`_
- `dm.zope.schema`_
- `dm.xmlsec.binding`_
- `PyXB`_
- `xmlsec1`_
- `lxml`_
- `openssl`_ (although other encryption libraries can be used)

There is an `example buildout`_ to compile all these components from source
if you want a completely standalone solution.


Configuration
=============

First you need to decide if you want your Plone to be an IdP or an SP.

An IdP means the users and passwords will be stored in your Plone site and other
services will be configured to redirect to Plone to be able to login into their
respective sites.

An SP means that you won't store users and passwords locally and instead your
users will be redirected to another site (the IdP) during the login process to
be authenticated. Examples of alternative IdP's might be `Microsoft Active Directory
Federated services`_ (`ADFS`_) or `Shibboleth`_, or another Plone site configured
as an IdP.


Step 1. Setup your authority
----------------------------

Regardless if you are going to be an IdP or SP you will need a single authority
object. This object contains assertions about what your service can do and
what other services can do. It also provides a public url to a XML `Metadata`_ file
that contains the SAML2 assertions.

1. In the ZMI Add at the Plone root a "Saml authority" object.
2. Give it the id "saml2auth". It doesn't matter really what it's called but
   it will appear in the public `metadata`_ url you will give to the owners of
   other services
3. Entity id. This is important. This is an id that should uniquely identify
   your service from other services that are part of the SSO network. For
   example if your and the IdP with 10 different services using you for
   authentication, your entity id will have to be unique.
4. Certificate and private key. You will only need these settings if you are
   going to be an IdP. It the paths to a .per and .key files on your server. That
   means you will need to find a
   way to deploy these files to your remote machines.
   The .der file can be created from .key file. The path is relative to $CLIENT_HOME
   (not the buildout-dir as you might expect)
   This is normally something like 'var/instance' with buildout.
   So a relative url starting with '../../' gets you to buildout dir.
5. Base URL. This is a zope root URL. It needs to be in the same domain as your
   Plone site (However, you can use your Plone site URL here - since by acquisition
   it behaves as the zope root URL).


Next you will
need to configure the other services that you will collaborate with. If you are
an SP these will be IdP's that the user can choose to login into your service via.
If you are an IdP these will be the SP's that are allowed to login via your site.


Step 2. Setup your IdP
----------------------

If Plone is going to be your IdP do the following

1. Go to the ZMI plone root and add a
   "Saml simple idpsso with integrated attribute provider".
2. Give the id `saml2idp` but it doesn't really matter. This id will appear
   in the url of some of the urls used as part of the authentication process.
3. You're done.

If your IdP isn't a Plone site you will need to consult their documentation
on how it needs to be configured.


Step 3. Setup your SP
---------------------

If your Plone is going to be your SP do the following

1. Go to ZMI Plone root and then acl_users.
2. Add a "Saml integrated simple spsso plugin (integrated spsso)" object. Call it
   `saml2sp`. Again id doesn't really matter.
3. You can use the defaults. Save.
4. Click the "activate tab" and activate each PAS plugin.
5. Click 'Challenge' in the Activate tab and ensure `saml2sp` is the top plugin.
   This means that if an UnAuthorized exception is thrown in Plone
   the saml2 plugin will be used and the user will be directed to select a IdP
   to login via. If this isn't done Plone's normal login page will display
   and the only way to instigate a SAML login sequence is via the explicit
   login url. The explicit login url in this case would be
   'acl_users/saml2sp/login'.
6. (optional) Create a new login link. Plone's default login link
   in personal tools goes direct to the cookie based authentication form
   /login. Instead create a page in the base of your site called /loggedin.
   Make it private it and in the sharing tab make it visible to logged in users.
   In ZMI '/portal_actions/user/login' set the URL to
   'string:${globals_view/navigationRootUrl}/loggedin'.

If your Plone is the IdP and you are setting up another service as the SP you
will need to look at the documentation of your SP on how to configure it.


Step 4. Authorise
-----------------

Now that you have a working IdP and SP you will need to authorise them so they
will work together. The SAML2 protocol is such that a IdP needs to know about the
SP and visa versa for the authentication requests to work.

Providers can be configured to authorise each other in different ways however
`dm.zope.saml2`_ ONLY supports the `metadata`_ method. Your Plone site has
a web accessible url to a `metadata`_ file that contains all the information
the other providers need to authorise the Plone site. Likewise your other providers
will need to provide a url to a `metadata`_ file that your Plone site can access.
Periodically your Plone site will download this file. The
file is then cached locally. The `metadata`_ contains the information about what
kind of service and urls are needed or offered for the interaction.

Note that the actual SAML2 authentication exchange doesn't require the SP and IdP
to be directly connected, just that the end users browser be able to access both.
However the `metadata`_ exchange does require direct connectivity between the services.
If you don't have direct connectivity this can be
worked around by moving your metadata files on a different webserver. Note however
that your `metadata`_ file generated by Plone has an expiry date in it.
You will need to periodically update your `metadata`_ file to ensure the expiry date
is in the future.

To configure another provider (SP or IdP) to authorise your Plone site

1. Go to your SAML2 Authority object /saml2auth.
2. Write down your own `metadata`_ url. This is found by clicking on the "`metadata`_"
   tab inside the saml2auth object. Due to something strange with iframes you
   will likely have to open this url in a new window/tab to see the XML properly.
   The url is the url to your saml authority object + '/metadata'.
   Note that you will get an error like "DOMGenerationError: Binding value inconsistent with content model"
   if you try to access this url before you have done step 2 or 3.
3. Configure this url in the appropriate way in your provider. Ensure it can
   download and parse the metadata file.

You might find that your provider doesn't support the `metadata`_ standard
as this is optional. Many implementations that claim to be SAML2 compliant
but have retained the old way of doing configuration.
In this case you will need to learn to read the `metadata`_
file to get the urls and settings from it that your IdP will need.


To configure your Plone site to authorize another provider (SP or IdP)

1. Obtain the metadata url and the entity id from your other provider. The entity
   id is actually in the metadata file that the metadata url refers to.
2. Go to ZMI plone root, then saml2auth. Click
   "Add Saml2 entity defined by metadata providing url"
3. "Id" must be equal to the entity id (which can be found in the metadata file).
4. Url goes in the url field.
5. Click on the object with the entity id. Click the metadata tab and ensure to
   ensure the file cached and able to be parsed. You may need to open the url in a new
   tab or window for the xml to appear properly.

If your provider doesn't support the `metadata`_ standard you will need to
manually generate a metadata file and place it in a web accessible location.
Once you've done that, follow the above steps. For example here is documentation
on creating `metadata files for shibboleth`_


Step 5. Test
------------

To test an IdP you will need a SP. You can use another Plone site (same one
won't work) or another SAML2 SP. To test an SP you will need a IdP.
You can use another Plone site or another SAML2 SP.

It's possible to create two Plone sites in the same instance and authorise
one to authenticate via the other.

Step 5. Member Attributes
-------------------------

If you set your Plone site up as an IdP then you make member attributes
or arbritrary data available to the SP's.

1. If you setup your IdP using these instructions you would have created an
   object in your Plone root called `saml2idp` of type
   'Saml simple idpsso with integrated attribute provider'. Open this.
2. Click 'Add Saml provided attribute.
3. If the data is an attribute of your member object such as provided by LDAP
   plugin or another PAS plugin then just enter the attribute name as the id.
   Otherwise pick an id and use the 'Evaluator' field togeather with a
   PythonScript or a view to determine the information to send.
4. External attribute name will be what the your SP uses to request this data.
5. After configuring your attributes you metadata file will have changed to
   reflect this additional service. You may need to ensure your SP obtains
   the update metadata file.
6. Configure your SP to request the attributes.nNote that the attributes will
   not automatically be sent with the authentication response but rather are
   sent in response to a `SAML Attribute Query`_.

TODO

Patches
=======

c.saml2 overrides the IRelayStateStore implementation for the idpsso so as to
store the original SAML request during the login process. Instead of storing
it in the database incurring a transaction for each login attempt, it stores
it back in the users browsers in a cookie.

c.saml2 also makes the call to 'dm.xmlsec.binding.initialize()' on zope startup
refered to in the `dm.zope.saml2` implementation. This means that currently
c.saml2 is hard-coded to use openssl. In future this might be made configurable
via an environment variable, otherwise try setting this yourself as per
`dm.xmlsec.binding`_ documentation.

Compatibility
=============

Some SAML2 SP's expect to see both key and signature passed back in the authentication response.
The key is compared against one store locally on the SP to ensure its the correct one.
`dm.zope.saml2`_ doesn't support this, instead expecting the key to be shared
and updated via the metadata url.

`dm.zope.saml2`_ doesn't support SAML 2.0 Single Logout.

If you get 'DOMGenerationError: Binding value inconsistent with content model'
exception when viewing your own metadata url. Ensure your ipdsso or spsso
objects are created first.

If you get a 'ComponentLookupError: (<InterfaceClass dm.zope.saml2.interfaces.ISamlAuthority>, '')'
when trying to remove a site with saml installed then remove your each of the
saml related objects from the site first before deleting the whole site.

You may also get a
'ComponentLookupError: (<InterfaceClass dm.zope.saml2.interfaces.ISamlAuthority>, '')'
during a zexp import of a SamlAuthority object. There are also problems when
 using zexp import for the Idpsso object as well.

Notice to CentOS users
----------------------

You may experience errors compiling and/or running the software on CentOS.
These GitHub issues mention some errors you might expect to encounter, and pointers how to solve them:

- https://github.com/onelogin/python-saml/issues/30
- https://github.com/onelogin/python-saml/issues/177

Most of it is to do with the `dm.xmlsec.binding` package.

Thanks
======

`Dieter Maurer`_ for the excellent dm.zope.saml2 which does all the work.

Work on collective.saml2 is so far sponsored by `PretaGov`_.



.. _example buildout: https://github.com/collective/collective.saml2/blob/master/buildout.cfg
.. _dm.zope.saml2: https://pypi.python.org/pypi/dm.zope.saml2
.. _dm.reuse: https://pypi.python.org/pypi/dm.reuse
.. _dm.saml2: https://pypi.python.org/pypi/dm.saml2
.. _dm.xmlsec.binding: https://pypi.python.org/pypi/dm.xmlsec.binding
.. _dm.zope.schema: https://pypi.python.org/pypi/dm.zope.schema
.. _PyXB: https://pypi.python.org/pypi/PyXB
.. _lxml: https://pypi.python.org/pypi/lxml
.. _xmlsec1: http://www.aleksey.com/xmlsec/
.. _openssl: http://www.openssl.org/
.. _PretaGov: http://www.pretagov.com.au
.. _Dieter Maurer:http://www.dieter.handshake.de/
.. _Shibboleth: http://shibboleth.net/
.. _ADFS: http://en.wikipedia.org/wiki/Active_Directory_Federation_Services
.. _Microsoft Active Directory Federated services: http://en.wikipedia.org/wiki/Active_Directory_Federation_Services
.. _metadata: http://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Metadata
.. _Metadata: http://en.wikipedia.org/wiki/SAML_2.0#SAML_2.0_Metadata
.. _metadata files for shibboleth: https://wiki.shibboleth.net/confluence/display/SHIB2/MetadataForSP
.. _SAML Attribute Query: http://en.wikipedia.org/wiki/SAML_2.0#SAML_Attribute_Query
