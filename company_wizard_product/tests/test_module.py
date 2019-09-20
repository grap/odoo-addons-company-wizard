# Copyright (C) 2018 - Today: GRAP (http://www.grap.coop)
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase
from odoo.addons.company_wizard_base.fix_test import fix_required_field


class TestModule(TransactionCase):
    """Tests for 'Product Fiscal Company' Module"""

    # Overload Section
    def setUp(self):
        super().setUp()
        self.ProductPricelist = self.env['product.pricelist']
        self.CreateWizard = self.env['res.company.create.wizard']
        self.user_erp_manager = self.env.ref(
            'company_wizard_base.user_erp_manager')
        fix_required_field(self, 'DROP')

    def tearDown(self):
        self.cr.rollback()
        fix_required_field(self, 'SET')
        super().tearDown()

    # Test Section
    def test_01_pricelist_creation(self):
        """[Functional Test] creating a new company via wizard,
        with user accountant, should create (or update) a pricelist"""
        wizard = self.CreateWizard.sudo(self.user_erp_manager).create({
            'company_name': 'Test Company Wizard',
            'company_code': 'WIZ',
        })
        wizard.button_create_company()
        pricelists = self.ProductPricelist.search([
            ('company_id', '=', wizard.company_id.id),
            ('name', '=', 'WIZ - Public Pricelist'),
        ])
        self.assertEqual(
            len(pricelists), 1,
            "Create a company by wizard should create a pricelist")
