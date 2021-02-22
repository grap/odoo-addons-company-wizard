# Copyright (C) 2014 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).


from odoo import _, api, models


class ResCompanyCreateWizard(models.TransientModel):
    _inherit = "res.company.create.wizard"

    @api.multi
    def _create_company(self):
        self.ensure_one()
        super()._create_company()
        ProductPricelist = self.env["product.pricelist"]

        # update just created pricelist, if exist or create one
        pricelists = ProductPricelist.search([("name", "=", self.company_id.name)])
        if len(pricelists):
            pricelist = pricelists[0]
            pricelist.write(self._prepare_pricelist())
        else:
            pricelist = ProductPricelist.create(self._prepare_pricelist())

    @api.multi
    def _prepare_pricelist(self):
        self.ensure_one()
        if self.company_id.code:
            code = self.company_id.code
        else:
            code = "#%d" % self.company_id.id
        return {
            "name": _("%s - Public Pricelist") % code,
            "currency_id": self.company_id.currency_id.id,
            "company_id": self.company_id.id,
        }
