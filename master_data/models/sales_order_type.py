# -*- coding: utf-8 -*-
from odoo import fields, models


class SalesOrderType(models.Model):
    _name = 'sales.order.type'
    _description = 'Sales Order Type'
    _order = 'name asc'

    name = fields.Char(string='Name', required=True)