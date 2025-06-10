from odoo import http
from odoo.http import request

# This was Trial 1 for topics 'Rendering Templates'
class WebController(http.Controller):
    @http.route('/hospital/patient/registration_form',auth='public',type='http',website=True)
    def patient_registration_form(self):
        patients=request.env['hospital.patient'].search([])
        return request.render('house-md.patient_registration_form_view',{
            'patients':patients
        })
