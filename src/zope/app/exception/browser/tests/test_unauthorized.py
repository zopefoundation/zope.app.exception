##############################################################################
#
# Copyright (c) 2001-2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Test Unauthorized Exception Views"""

import unittest
from zope import component, interface
import zope.browserpage.namedtemplate
from zope.publisher.browser import TestRequest
from zope.authentication.interfaces import IAuthentication
from zope.security.interfaces import IPrincipal

from zope.app.exception.browser.unauthorized import Unauthorized
from zope.component.testing import PlacelessSetup


@interface.implementer(IPrincipal)  # this is a lie
class DummyPrincipal(object):

    def __init__(self, id):
        self.id = id

    def getId(self):  # pragma: no cover
        return self.id


@interface.implementer(IAuthentication)  # this is a lie
class DummyAuthUtility(object):

    status = None

    def unauthorized(self, principal_id, request):
        self.principal_id = principal_id
        self.request = request
        if self.status is not None:
            self.request.response.setStatus(self.status)


@component.adapter(Unauthorized)
@interface.implementer(zope.browserpage.namedtemplate.INamedTemplate)
class DummyTemplate(object):

    def __init__(self, context):
        self.context = context

    def __call__(self):
        return 'You are not authorized'


class Test(PlacelessSetup, unittest.TestCase):

    def setUp(self):
        super(Test, self).setUp()
        self.auth = DummyAuthUtility()
        component.provideUtility(self.auth, IAuthentication)

    def tearDown(self):
        super(Test, self).tearDown()

    def testUnauthorized(self):
        component.provideAdapter(DummyTemplate, name="default")
        exception = Exception()
        try:
            raise exception
        except:  # noqa: E722 do not use bare 'except'
            pass
        request = TestRequest()
        request.setPrincipal(DummyPrincipal(23))
        u = Unauthorized(exception, request)
        res = u()

        # Make sure that we rendered the expected template
        self.assertEqual("You are not authorized", res)

        # Make sure the response status was set
        self.assertEqual(request.response.getStatus(), 403)

        # check headers that work around squid "negative_ttl"
        self.assertEqual(request.response.getHeader('Expires'),
                         'Mon, 26 Jul 1997 05:00:00 GMT')
        self.assertEqual(request.response.getHeader('Pragma'),
                         'no-cache')
        self.assertEqual(request.response.getHeader('Cache-Control'),
                         'no-store, no-cache, must-revalidate')

        # Make sure the auth utility was called
        self.assertIs(self.auth.request, request)
        self.assertEqual(self.auth.principal_id, 23)

    def testRedirect(self):
        exception = Exception()
        try:
            raise exception
        except:  # noqa: E722 do not use bare 'except'
            pass
        request = TestRequest()
        request.setPrincipal(DummyPrincipal(23))
        u = Unauthorized(exception, request)

        self.auth.status = 303

        res = u()

        # Make sure that the template was not rendered
        self.assertIsNone(res)

        # Make sure the auth's redirect is honored
        self.assertEqual(request.response.getStatus(), 303)

        # Make sure the auth utility was called
        self.assertIs(self.auth.request, request)
        self.assertEqual(self.auth.principal_id, 23)


def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)
