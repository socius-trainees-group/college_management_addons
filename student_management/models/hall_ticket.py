from odoo import fields,models

class hallticket(models.Model):
    _name = 'student_management.table.hallticket'
    name = fields.Char(string='Student name')
    register_number = fields.Integer(string='Register no')
    branch = fields.Char(string='Branch')
    subject = fields.Char(string='Subject')
    subject_code = fields.Integer(string='Subject code')