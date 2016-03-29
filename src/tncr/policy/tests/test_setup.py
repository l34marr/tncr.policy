# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from tncr.policy.testing import TNCR_POLICY_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that tncr.policy is properly installed."""

    layer = TNCR_POLICY_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if tncr.policy is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('tncr.policy'))


class TestUninstall(unittest.TestCase):

    layer = TNCR_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['tncr.policy'])

    def test_product_uninstalled(self):
        """Test if tncr.policy is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('tncr.policy'))
