# -*- coding: utf-8 -*-
from odoo import fields, models


class BusinessUnit(models.Model):
    _name = 'business.unit'
    _description = 'Business'
    _order = 'full_name asc'

    name = fields.Char(string='Name', required=True)
    full_name = fields.Char(string='Full Name')
    short_code = fields.Char(string='Short Code')
    business_type_id = fields.Many2one(
        comodel_name='business.type',
        string='Business Type',
    )
