# Copyright (C) 2013 - Today: GRAP (http://www.grap.coop)
# @author Julien WESTE
# @author Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo.tests.common import TransactionCase


class TestWizard(TransactionCase):
    """Tests for Account Fiscal Company Module (Wizard)"""

    # Overload Section
    def setUp(self):
        super().setUp()
        self.CreateWizard = self.env['res.company.create.wizard']
        self.user_erp_manager = self.env.ref(
            'company_wizard_base.user_erp_manager')
        self.chart_template = self.env.ref(
            'l10n_generic_coa.configurable_chart_template')

    # Test Section
    def test_01_chart_of_account_creation(self):
        """[Functional Test] creating a new company via wizard
        should generate a Chart of Account"""
        wizard = self.CreateWizard.sudo(self.user_erp_manager).create({
            'company_name': 'Test Company Wizard',
            'company_code': 'WIZ',
            'chart_template_id': self.chart_template.id,
        })
        wizard.button_create_company()
