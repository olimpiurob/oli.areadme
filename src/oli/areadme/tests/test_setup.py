# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from oli.areadme.testing import OLI_AREADME_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that oli.areadme is properly installed."""

    layer = OLI_AREADME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if oli.areadme is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('oli.areadme'))

    def test_browserlayer(self):
        """Test that IOliAreadmeLayer is registered."""
        from oli.areadme.interfaces import IOliAreadmeLayer
        from plone.browserlayer import utils
        self.assertIn(IOliAreadmeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = OLI_AREADME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['oli.areadme'])

    def test_product_uninstalled(self):
        """Test if oli.areadme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('oli.areadme'))

    def test_browserlayer_removed(self):
        """Test that IOliAreadmeLayer is removed."""
        from oli.areadme.interfaces import IOliAreadmeLayer
        from plone.browserlayer import utils
        self.assertNotIn(IOliAreadmeLayer, utils.registered_layers())
