# -*- coding: utf-8 -*-
from odoo import fields, models


class BusinessType(models.Model):
    _name = 'business.type'
    _description = 'Business Type'
    _order = 'name asc'

    name = fields.Char(string='Name', required=True)
