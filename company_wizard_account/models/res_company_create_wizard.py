# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# @author: Julien WESTE
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ResCompanyCreateWizard(models.TransientModel):
    _inherit = "res.company.create.wizard"

    chart_template_id = fields.Many2one(
        comodel_name="account.chart.template",
        string="Account Template",
        domain="[('visible', '=', True)]",
    )

    @api.multi
    def _create_company(self):
        self.ensure_one()
        super()._create_company()
        if self.chart_template_id:
            my_self = self.chart_template_id.sudo()
            # hard switch company of the user sudo, because
            # load_for_current_company is bad coded, and doesn't support
            # force_company context
            # ref /addons/account/models/chart_template.py L194
            bkp_company = my_self.env.user.company_id
            my_self.env.user.company_id = self.company_id

            my_self.load_for_current_company(0, 0)
            # Restore company for the admin user
            my_self.env.user.company_id = bkp_company
