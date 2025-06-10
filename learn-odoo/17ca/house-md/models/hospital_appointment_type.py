from odoo import models, fields

class HospitalAppointmentType(models.Model):
    _name = "hospital.appointment.type"
    _description = "Hospital Appointment Type"

    name = fields.Char()
    sequence = fields.Integer()
