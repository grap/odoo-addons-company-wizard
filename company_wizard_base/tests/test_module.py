# coding: utf-8
# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author Julien WESTE
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestModule(TransactionCase):
    """Tests for 'Company Wizard - Base' Module"""

    # Overload Section
    def setUp(self):
        super(TestModule, self).setUp()

        self.user_obj = self.env['res.users']
        self.company_obj = self.env['res.company']
        self.wizard_obj = self.env['res.company.create.wizard']

        self.user_erp_manager = self.env.ref(
            'company_wizard_base.user_erp_manager')

    # Test Section
    def test_01_wizard(self):
        """Create a child company via the wizard, with user ERP Manager"""
        wizard = self.wizard_obj.sudo(self.user_erp_manager).create(
            self._prepare_company_wizard())
        wizard.button_create_company()

        # Check if the company is well created
        companies = self.company_obj.search([
            ('name', '=', 'Test Company Wizard'),
        ])
        self.assertEqual(
            len(companies), 1,
            "The company creation via the wizard failed.")

        # Check if the user is well created
        users = self.user_obj.search([
            ('name', '=', 'Test User Wizard'),
            ('login', '=', 'test_user_wizard@odoo.com'),
            ('company_id', '=', companies[0].id),
        ])
        self.assertEqual(
            len(users), 1,
            "The user creation via the wizard failed.")

    def _prepare_company_wizard(self):
        return {
            'company_name': 'Test Company Wizard',
            'code': 'WIZ',
            'create_user': True,
            'user_name': 'Test User Wizard',
            'user_login': 'test_user_wizard@odoo.com',
        }
