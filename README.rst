.. contents::

Introduction
============

This plugin does the following so far

- ensure the dependencies for dm.zope.saml2 are installed
- provide an example buildout to build all the dependencies standalone
- document how to configure dm.zope.saml2
- a patch to activate the encryption type
- a patch to remove the need for zope sessions

In the future we hope to also include a control panel to
- configure a Plone site as either a IdP or a SP
- managing services including manual configuration (without metadata urls)
- override the login screen to all login via IdP
- management of keys TTW

Configuration
=============

First you need to decide if you want your Plone to be an IdP or an SP.
An IdP means the users and passwords will be stored in your Plone site and other
services will be configured to redirect to Plone to be able to login into their
respective sites.
An SP means that you won't store users and passwords locally and instead your
users will be redirected to another site (the IdP) during the login process to
be authenticated. Examples of alternative IdP's might be Microsoft Active Directory
Federated services (ADFS) or Shiboleth.

Step 1. Setup your authority
----------------------------

Regardless if you are going to be an IdP or SP you will need a single authority
object. This object contains assertions about what your service can do and
what other services can do. It also provides a public url to a XML Metadata file
that contains the SAML2 assertions.

1. In the ZMI Add at the Plone root a "Saml authority" object.
2. Give it the id "saml2auth". It doesn't matter really what it's called but
   it will appear in the public metadata url you will give to the owners of
   other services
3. Entity id. This is important. This is an id that should uniquely identify
   your service from other services that are part of the SSO network. For
   example if your and the IdP with 10 different services using you for
   authentication, your entity id will have to be unique.
4. Certificate and private key. You will only need these settings if you are
   going to be an IdP. It the paths to a PER and key files on your server. That
   means you will need to find a
   way to deploy these files to your remote machines.
5. Base url. This is a zope root url, not the base url to your Plone instance.
6. Write down your own metadata url. This is found by clicking on the "metadata"
   tab inside the saml2auth object. Due to something strange with iframes you
   will likely have to open this url in a new window/tab to see the XML properly.
   The url is your the url to your saml authority object + '/metadata'

Once saved you have configured partially configured your service. Next you will
need to configure the other services that you will collaborate with. If you are
an SP these will be IdP's that the user can choose to login into your service via.
If you are an IdP these will be the SP's that are allowed to login via your site.
These remote services have to have a web accessible XML metadata file for this
to work. Periodically the saml2 authority object will download this file. The
file is then cached locally. The metadata contains the information about what
kind of service and urls are needed or offered for the interaction.

1. Obtain the metadata url and the entity id. The entity id is actually in the
metadata file that the metadata url refers to.
2. Go to ZMI plone root, then saml2auth. Click
   "Add Saml2 entity defined by metadata providing url"
3. "Id" must be equal to the entity id (which can be found in the metadata file).
4. Url goes in the url field.
5. You're done.

Step 2. Setup your IdP
----------------------

If Plone is going to be your IdP do the following

1. Go to the ZMI plone root and add a
   "Saml simple idpsso with integrated attribute provider".
2. Give the id "saml2_idp" but it doesn't really matter. This id will appear
   in the url of some of the urls used as part of the authentication process.
3. You're done.

If another service is going to the IdP you will need to consult their documentation
on how it needs to be configured. If your IdP supports the exchange of XML
metadata via url then all you will need is your Plone sites metadata url which
you wrote down in Step 1.

You might find that your IdP doesn't support the metadata standard however
as this is optional. In this case you will need to learn to read the metadata
file to get the urls and settings from it that your IdP will need.

If you don't have a direct connection between your IdP and SP you might need to
copy the metadata file to another location that is accessible. Note however
that your metadata file has an expiry date in it. You will need to periodicly
update your metadata file to ensure the expiry date is in the future.

Step 3. Setup your SP
---------------------

If your Plone is going to be your SP do the following

1. Go to ZMI Plone root and then acl_users.
2. Add a "Saml integrated simple spsso plugin (integrated spsso)" object. Call it
   "saml2_sp". Again id doesn't really matter.
3. You can use the defaults. Save.
4. Click the "activate tab".

If your Plone is the IdP and you are setting up another service as the SP you
will need to look at the documentation of your SP on how to configure it. If
it supports fetching a metadata url then all you will need is the metadata url
you wrote down in step 1. However many SP's don't support this standard. In
which case you will need to look at the metadata file contents and take the
values your SP needs from there.




