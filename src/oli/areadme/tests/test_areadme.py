# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from oli.areadme.testing import OLI_AREADME_INTEGRATION_TESTING  # noqa
from oli.areadme.interfaces import IAReadme

import unittest2 as unittest


class AReadmeIntegrationTest(unittest.TestCase):

    layer = OLI_AREADME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='AReadme')
        schema = fti.lookupSchema()
        self.assertEqual(IAReadme, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='AReadme')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='AReadme')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(IAReadme.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('AReadme', 'AReadme')
        self.assertTrue(
            IAReadme.providedBy(self.portal['AReadme'])
        )
