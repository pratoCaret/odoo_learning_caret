from odoo import http
from odoo.http import request

class PatientWebMenu(http.Controller):

    @http.route('/hospital/patient_registration_form',auth='public', type='http', website=True)
    def web_menu_patient_regi_form(self):
        return request.render('house-md.web_menu_patient_registration_form')