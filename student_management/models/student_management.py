from odoo import models, fields, api
from datetime import date
from odoo.exceptions import ValidationError


class Students(models.Model):
    _name = "students.students"
    _description = "student_management"

    name = fields.Char(string="Student Name")
    gender = fields.Selection([("male", "Male"), ("female", "Female"), ("others", "Others")],
                              string="Gender", default="male")
    age = fields.Char(string="Age", store=True, readonly=True)
    mail_id = fields.Char(string="Mail Id")
    department = fields.Char(string="Department")
    semester = fields.Char(string="Semester")
    date_of_birth = fields.Date(string="Date Of Birth", required=True)
    contact_no = fields.Char(string="Mobile number", required=True)
    address = fields.Text(string="Address")
    image_of_student = fields.Binary(string="Image", attachment=True, store=True)

    street = fields.Char(string="Street")
    street2 = fields.Char(string="Street2")
    city = fields.Char(string="City")
    state_id = fields.Char(string="State_id")
    zip = fields.Integer(string="Zip")
    country_id = fields.Char(string="Country_id")

    @api.onchange('date_of_birth')
    def set_age(self):
        for record in self:
            if record.date_of_birth:
                record.age = f"{int((date.today()-record.date_of_birth).days/365.2425)} years old"

    @api.constrains('age')
    def check_age(self):
        for record in self:
            if int(record.age[:2]) < 18:
                raise ValidationError("Only students with age more than 18 year can register")

    @api.constrains('contact_no')
    def check_contact(self):
        for record in self:
            if len(record.contact_no) < 8 or any(character.isalpha() for character in record.contact_no):
                raise ValidationError("Make Sure You Entered Mobile Number Correctly")
