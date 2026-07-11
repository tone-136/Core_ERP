from odoo import fields, models

class UnitPart(models.Model):
    _name = 'unit.part'
    _description = 'Unit or Part'
    _order = 'name asc'

    name = fields.Char(string='Name', required=True)
