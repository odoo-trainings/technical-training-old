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
    total_price = fields.Float(string="Total Price", digits='Product Price', compute='_compute_total_price', store=True, readonly=True)
    
    # Relational Fields
    session_ids = fields.One2many(comodel_name='academy.session',
                                  inverse_name='course_id', 
                                  string='Sessions')
    
    # Fields for Smart Buttons
    session_count = fields.Integer('# Sessions', compute='_compute_session_count')
    
    # --------------------------------------- Compute Methods ----------------------------------   
    # Use Computed field instead of OnChange in Odoo 16
    @api.depends('base_price', 'additional_fee')
    def _compute_total_price(self):
        for record in self:
            if record.base_price < 0.00:
                raise UserError(('Base Price cannot be set as Negative.'))
            record.total_price = record.base_price + record.additional_fee

    @api.depends('session_ids.course_id')
    def _compute_session_count(self):
        read_group_sessions = self.env['academy.session'].sudo()._read_group([('course_id', 'in', self.ids)], ['course_id'], 'course_id')
        data = dict((res['course_id'][0], res['course_id_count']) for res in read_group_sessions)
        for course in self:
            course.session_count = data.get(course.id, 0)
            
    # --------------------------------------- Constrains Methods ----------------------------------
    @api.constrains('additional_fee')
    def _check_additional_fee(self):
        for record in self:
            if record.additional_fee < 10.00:
                raise ValidationError(('Additional Fees cannot be less than 10.00. Current Value: %s' %record.additional_fee)) 
     
    # --------------------------------------- Smart Button Action ---------------------------------           
    def action_redirect_sessions(self):
        action = self.env["ir.actions.act_window"]._for_xml_id('odoo_academy.session_list_action')
        action['context'] = {
            'default_course_id': self.id
        }
        action['domain'] = [('course_id', "=", self.id)]
        return action
