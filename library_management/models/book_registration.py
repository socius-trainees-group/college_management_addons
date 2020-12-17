# -*- coding: utf-8 -*-

from odoo import models, fields

class BookRegistration(models.Model):
    _name = "book.registration"
    _description = "Book registration module"

    name = fields.Char(string="Book Name",required=True)
    number = fields.Integer(string="Book Number", required =True)
    author = fields.Char(string="Author")
    registration_date = fields.Date(string="Registration Date")
    category = fields.Char(string="Category")
    published_year = fields.Integer(string="Published Year")







