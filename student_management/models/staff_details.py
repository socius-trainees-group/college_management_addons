from odoo import fields,models

class StaffDetails(models.Model):
    _name = 'staff.table.staff'

    name = fields.Char(string='Staff name')
    gender = fields.Char(string='Staff Gender')
    address = fields.Text(string='Address')
    phone = fields.Integer(string="phone", required=True)
