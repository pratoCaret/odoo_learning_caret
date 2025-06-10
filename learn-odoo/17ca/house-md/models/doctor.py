from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Details'
    _inherit = ['mail.thread']
    _rec_name = 'name'

    name = fields.Char(string='Name', required=True, tracking=True)
    doctor_user_id=fields.Many2one('res.users', string="UserID", tracking=True, required=True)
    specialization = fields.Char(string='Specialization', tracking=True)
    phone = fields.Char(string='Phone Number', tracking=True)
    email = fields.Char(string='Email', tracking=True)

    patient_ids = fields.One2many('hospital.appointment', 'doctor_id', string='Patients Assigned') # COUNTING ASSIGNED PATIENTS
    @api.depends('patient_ids')
    def _compute_patient_count(self):
        for record in self:
            record.patient_count = len(record.patient_ids)
    patient_count = fields.Integer(string="Total Assigned Patients", compute="_compute_patient_count")

    display_name = fields.Char(compute="_compute_display_name", search="_search_display_name") # SEARCH
    def _search_display_name(self, operator, value):
        return [('name', operator, value)]