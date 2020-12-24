from odoo import http
from odoo.http import request

class FirstPage(http.Controller):



    @http.route('/first/page/', type='http', auth='public', website=True)
    def first_page(self):
        return request.render('student_management.first_page')#id of front_end xml
