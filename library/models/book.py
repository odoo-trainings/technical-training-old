from odoo import models, fields, api

class Book(models.Model):
    
    # ---------------------------------------- Private Attributes ---------------------------------
    _name = 'library.book'
    _description = 'Book Info'
    # --------------------------------------- Fields Declaration ----------------------------------

    # Reserved Fields
    name = fields.Char(string='Title', required=True)
    active = fields.Boolean(string='Active', default=True)
   
    # Simple Fields
    isbn = fields.Char(string='ISBN')
    summary = fields.Text(string='Summary')
    author = fields.Char(string='Author')
    format = fields.Selection(string='Level',
                            selection=[('paperback', 'Paperback'),
                                       ('hardcover', 'Hardcover'),
                                       ('audiobook', 'Audiobook'),
                                       ('ebook', 'E-Book')],
                            copy=False)
    language = fields.Selection(string='Language',
                            selection=[('en', 'English'),
                                       ('es', 'Spanish'),
                                       ('fr', 'French'),
                                       ('de', 'German')],
                            copy=False)
    edition = fields.Integer(string='Edition')
    publisher = fields.Char(string='Publisher')
    publish_date = fields.Date(string='Publish Date')
    price = fields.Monetary(string='Price')
    currency_id = fields.Many2one('res.currency')