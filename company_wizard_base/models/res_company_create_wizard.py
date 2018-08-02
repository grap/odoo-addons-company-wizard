# coding: utf-8
# Copyright (C) 2013-Today: GRAP (http://www.grap.coop)
# @author: Julien WESTE
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import string
from random import choice

from odoo import api, fields, models


class ResCompanyCreateWizard(models.TransientModel):
    _name = 'res.company.create.wizard'

    _PASSWORD_SIZE = 8

    _STATE_SELECTION = [
        ('init', 'Start'),
        ('done', 'Done'),
    ]

    state = fields.Selection(
        selection=_STATE_SELECTION, string='State', readonly=True,
        default='init')

    company_name = fields.Char(string='Name', required=True)

    code = fields.Char(string='Code', required=True)

    parent_company_id = fields.Many2one(
        comodel_name='res.company', string='Parent Company')

    vat = fields.Char(string='Tax ID')

    company_registry = fields.Char(string='Company Registry')

    # Partner and company fields
    company_street = fields.Char(string='Street')

    company_street2 = fields.Char(string='Street complement')

    company_city = fields.Char(string='City')

    company_zip = fields.Char(string='ZIP')

    company_state_id = fields.Many2one(
        comodel_name='res.country.state', string='State')

    company_country_id = fields.Many2one(
        comodel_name='res.country', string='Country')

    company_website = fields.Char(string='Website')

    company_email = fields.Char(string='Email')

    company_phone = fields.Char(string='Phone')

    # User Fields
    create_user = fields.Boolean(string='Create User')

    user_name = fields.Char(string='Name')

    user_login = fields.Char(
        string='Login', help="Let empty to use the email as login")

    user_email = fields.Char(string='Email')

    user_password = fields.Char(
        string='Password', default=lambda s: s._default_user_password())

    # Technical hidden fields
    company_id = fields.Many2one(comodel_name='res.company')

    user_id = fields.Many2one(comodel_name='res.users')

    # Default Section
    def _default_user_password(self):
        characters = string.ascii_letters + string.digits
        return "".join(choice(characters) for x in range(self._PASSWORD_SIZE))

    # Button Section
    @api.multi
    def button_create_company(self):
        self.ensure_one()
        self._create_company()
        self.state = 'done'
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'res.company.create.wizard',
            'view_mode': 'form',
            'view_type': 'form',
            'res_id': self.id,
            'views': [(False, 'form')],
            'target': 'new',
        }

    # Overloadable Prepare Function
    @api.multi
    def _prepare_company(self):
        self.ensure_one()
        return {
            'name': self.company_name,
            'code': self.code,
            'parent_id': self.parent_company_id.id,
            'street': self.company_street,
            'street2': self.company_street2,
            'city': self.company_city,
            'state_id': self.company_state_id,
            'country_id': self.company_country_id,
            'website': self.company_website,
            'email': self.company_email,
            'phone': self.company_phone,
            'vat': self.vat,
            'company_registry': self.company_registry,
        }

    @api.multi
    def _prepare_partner(self):
        self.ensure_one()
        return {
            'customer': False,
            'supplier': False,
            'active': False,
        }

    @api.multi
    def _prepare_user(self):
        self.ensure_one()
        return {
            'customer': False,
            'name': self.user_name,
            'login': self.user_login or self.user_email,
            'email': self.user_email,
            'new_password': self.user_password,
            'company_id': self.company_id.id,
            'company_ids': [(4, self.company_id.id)],
        }

    @api.multi
    def _prepare_user_groups(self):
        """Overload this function. Should return a list of xml ids of groups"""
        self.ensure_one()
        return []

    @api.multi
    def _create_company(self):
        self.ensure_one()
        company_obj = self.env['res.company']
        user_obj = self.env['res.users']
        # Create Company
        self.company_id = company_obj.sudo().create(self._prepare_company())

        # Swith current user to the new company
        self.env.user.write({
            'company_id': self.company_id.id,
            'company_ids': [(4, self.company_id.id)],
        })
        # Clear cache, specially to reset obsoleted cached domain
        # ./odoo/tools/cache.py (_compute_domain)
        self.env.clear()

        # Manage Extra Data in associated partner
        self.company_id.partner_id.write(self._prepare_partner())

        # Create User if required
        if self.create_user:
            self.user_id = user_obj.create(self._prepare_user())
            for group in self._prepare_user_groups():
                self.env.ref(group).write({
                    'users': [(4, self.user_id.id)],
                })
