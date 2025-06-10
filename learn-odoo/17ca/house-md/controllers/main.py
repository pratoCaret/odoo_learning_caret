from odoo import http

class HospitalControllerTrail(http.Controller):

    #route - done
    # @http.route("/odooDiscussion/Hospital/ControllersTrial", type='json', auth='public') # auth and type and website -done
    @http.route("/odooDiscussion/Hospital/ControllersTrial", methods=['GET'], type='http', auth='public', website=True, multilang=True)
    def display_controller_method(self,x='trial'):
        print('check__________________________________________________________________________')
        # patients=http.request.env['hospital.patient'].search([('blood_group','in',('A-','B+'))])
        patients=http.request.env['hospital.patient'].search([])
        return http.request.render('house-md.controller_website_temp_trial',{'patients':patients})
        # return "This is the return method for the controllers." #display normal text

        # return http.request.render('house-md.controller_website_temp_trial',{ #display static list from a dic
        #     'patients':['caret','tarun','saurab','captain','os']
        # })

    # Learning trial
    # @http.route('/second/trial/<string:name>',auth='public',website=True)
    # def display_name_trial(self,name):
    #     return '<h1>{}</h1>'.format(type(name).__name__)

    @http.route('/odooDiscussion/Hospital/<model("hospital.patient"):patient>/', methods=['GET'], type='http', auth='public', website=True)
    def display_model_controller_trial(self,patient):
        return http.request.render('house-md.controller_website_temp_trial_2_model',{'patient':patient})


