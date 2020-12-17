from odoo import fields,models

class SchoolBook(models.Model):
    _name = 'school.book'


    sname = fields.Char(string="Student Name",required=True)
    name = fields.Char(string="Book Name", required=True)
    code = fields.Integer(string="ISBN", required=True)
    email = fields.Char(string="Email", copy=False)
    phone = fields.Char("Phone", copy=False)
    genere = fields.Char(string="Genere")
    publisher = fields.Char(string="Publisher")
    pickup = fields.Datetime("Pickup Date")
    ret = fields.Datetime("Return Date")
    taken_type = fields.Selection([('pickup', 'Pickup '),
                                    ('return', 'Return ')],
                                   string="Type of Action",
                                   )


