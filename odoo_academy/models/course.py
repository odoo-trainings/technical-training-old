from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError

class Course(models.Model):
    
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = 'academy.course'
    _description = 'Course Info'
    # --------------------------------------- Fields Declaration ----------------------------------

    # Reserved Fields
    name = fields.Char(string='Title', required=True)
    active = fields.Boolean(string='Active', default=True)
   
    # Simple Fields
    description = fields.Text(string='Description')
    level = fields.Selection(string='Level',
                            selection=[('beginner', 'Beginner'),
                                       ('intermediate', 'Intermediate'),
                                       ('advanced', 'Advanced')],
                            copy=False)
    
    # Fields for Pricing
    additional_fee = fields.Float(string="Additional Fee", digits='Product Price', default=0.00)
    base_price = fields.Float(string='Base Price', digits='Product Price', default=0.00)
    total_price = fields.Float(string="Total Price", digits='Product Price', compute='_compute_total_price', readonly=True)
    
    # --------------------------------------- Compute Methods ----------------------------------   
    # Use Computed field instead of OnChange in Odoo 16
    @api.depends('base_price', 'additional_fee')
    def _compute_total_price(self):
        for record in self:
            if record.base_price < 0.00:
                raise UserError(('Base Price cannot be set as Negative.'))
            record.total_price = record.base_price + record.additional_fee

    # --------------------------------------- Constrains Methods ----------------------------------
    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError(('Additional Fees cannot be less than 10.00. Current Value: %s' %record.additional_fee)) 