from odoo import http
from .main import HospitalControllerTrail


class HospitalControllerTrailInherit(HospitalControllerTrail):
    @http.route("/odooDiscussion/Hospital/ControllersTrial", methods=['GET'], type='http', auth='public', website=True,
                multilang=True)
    def display_controller_method(self,x='trial'):
        res= super(HospitalControllerTrailInherit, self).display_controller_method(x)
        print("INHERITed display_controller_method from_________________________________________")
        return res

        # patients=http.request.env['hospital.patient'].search([('blood_group','in',('A-','B+'))])
        # patients = http.request.env['hospital.patient'].search([])
        # return http.request.render('house-md.controller_website_temp_trial', {'patients': patients})