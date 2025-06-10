from odoo import models, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    def action_create_doctor(self):
        # Find the external ID of the doctor group
        doctor_group = self.env.ref('house-md.group_hospital_doctor')
        if doctor_group:
            self.groups_id= [(4, doctor_group.id)]  # Add to doctor group