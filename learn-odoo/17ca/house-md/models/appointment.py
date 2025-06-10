from odoo import api, fields, models
from datetime import date,timedelta
from odoo.exceptions import ValidationError

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread']
    _description = 'Hospital Appointment'
    _rec_name='patient_id'

    doctor_id = fields.Many2one('hospital.doctor', string="Assigned Doctor", required=False, tracking=True)
    patient_id=fields.Many2one('hospital.patient',string="Patient")
    # date_appointment=fields.Date(string="Date")
    dateTime_appointment=fields.Datetime(string="Date")
    note=fields.Text(string="Note")

    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High')
    ], string="Priority Level", default='medium', help="Urgency of the appointment")

    # will be adding a many2one field.
    appointment_type = fields.Selection([('done','Done'), ('attending', 'Attending'), ('incoming', 'Incoming'), ('not_done', 'Yet to attend')],string="Follow-up", default='not_done', help="Select what type of appointment is this ")
    # is_followup = fields.Boolean(string="Follow-up", default=False, help="Check if this is a follow-up appointment")

    @api.constrains('patient_id') # age must be more than 6 months
    def _check_patient_age(self):
        for record in self:
            if record.patient_id.age < 5:
                raise ValidationError("Patient must be at least 5 years old at the time of appointment.")

    @api.constrains('date_appointment') # cannot set appointment date to any date in past
    def _check_appointment_not_in_past(self):
        for record in self:
            if record.date_appointment and record.date_appointment < fields.Date.today():
                raise ValidationError("Appointment date cannot be in the past.")

    # search_display_name = fields.Char(search="_search_display_name") # to search in the appointments section
    # def _search_display_name(self, operator, value):
    #     return [('Patient', operator, value)]