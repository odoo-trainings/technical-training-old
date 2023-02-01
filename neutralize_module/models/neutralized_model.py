from odoo import models, fields, api


class neutralized_model(models.Model):
    _name = 'neutralize_module.neutralized_model'
    _description = 'neutralize_module.neutralized_model'

    name = fields.Char()
    value = fields.Integer()
