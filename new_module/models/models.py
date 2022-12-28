# -*- coding: utf-8 -*-
from datetime import date
from odoo import models, fields, api


# class new_module(models.Model):
#     _name = 'new_module.new_module'
#     _description = 'new_module.new_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
class ResPartner(models.Model):
    _inherit = 'res.partner'
    birthdate = fields.Date()
    age = fields.Integer(compute="_compute_age")
    
    @api.depends('birthday')
    def _compute_age(self):
        today = date.today()
        for record in self:
            record.age = today.year - record.birthdate.year - ((today.month, today.day) < (record.birthdate.month, record.birthdate.day))
            
        