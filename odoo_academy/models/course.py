from odoo import models, fields, api

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

    
