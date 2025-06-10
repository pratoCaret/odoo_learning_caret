from odoo import models, fields, api

class WizardMarkDone(models.TransientModel):
    _name = 'hospital.patient.isinsured.wizard'
    _description = 'Mark Task Done Wizard'

    confirm = fields.Boolean(string="Confirm?", default=True)
    name=fields.Char(string="Name: ")