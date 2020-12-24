# -*- coding: utf-8 -*-

from odoo import models, fields


class BookRegistration(models.Model):
    _name = "book.registration"
    _description = "Book registration module"

    name = fields.Char(string="Book Name", required=True)
    number = fields.Integer(string="Book Number", required=True)
    author_id = fields.Many2one('res.partner', string="Author", domain="[('author','=','True')]")
    image = fields.Binary(string="Image")
    registration_date = fields.Date(string="Registration Date")
    category_id = fields.Many2one('book.category', string="Category")
    published_year = fields.Integer(string="Published Year")
    shelf_id = fields.Many2one('book.shelf', string="Book Shelf")


class BookCategory(models.Model):
    _name = "book.category"
    _description = "Categories of book"
    name = fields.Char(string="Book Category")


class BookAuthor(models.Model):
    _inherit = 'res.partner'
    author = fields.Boolean(string="Book Author")


class BookShelf(models.Model):
    _name = "book.shelf"
    name = fields.Char(string="Shelf ID")
    book_ids = fields.One2many('book.registration', 'shelf_id',  string="Book")
