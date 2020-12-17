from odoo import models,fields,api

class Students(models.Model):
    _name= "students.students"
    _description = "student_management"

    name = fields.Char(string="Student Name")
    age = fields.Integer(string="Age")
    department = fields.Char(string="Department")
    semester = fields.Char(string="semester")
    date_of_birth = fields.Date(string="Date Of Birth")
    contact_no = fields.Integer(string="mobile number")
    address = fields.Text(string="Address")






