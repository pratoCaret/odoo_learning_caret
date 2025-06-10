from odoo.exceptions import ValidationError
from odoo import fields,models,api

class HospitalDecorators(models.Model):
    _name = 'hospital.decorator'
    _description = 'decorators check karva mate banavyu che'
    _inherit = ['mail.thread']
    _rec_name = 'name'

    name=fields.Char(string="Name", tracking=True)

    age = fields.Integer(string="Age")
    dob = fields.Date(string="DOB")

    def action_load_default(self):
        default_vals = self.get_default_patient_template()
        for rec in self:
            rec.name = default_vals['name']
            rec.age = default_vals['age']

    @api.model
    def get_default_patient_template(self):
        # self here is the MODEL, not a record
        return ({
            'name': 'Dummy Patient',
            'age': 6
        })

    # @api.model
    # def decorator_trial_method(self,values):
    #     self.env['hospital.decorator'].create({
    #         'name':'Dummy new Patient',
    #         'age':'9'
    #     })

    # @api.depends('dob')
    # def _compute_age(self):
    # # compute='_compute_age'  --  in the age integer field
    #     for rec in self:
    #         if rec.dob:
    #             rec.age = fields.Date.today().year - rec.dob.year

    @api.onchange('dob')
    def qo3ufwiuef(self):
    # this works before saving the changes in the form
        if self.dob:
            self.age = fields.Date.today().year - self.dob.year

    # @api.constrains('age')
    # def sjyrbvus(self):
    #     for rec in self:
    #         if rec.age < 5:
    #             raise ValidationError("User must be of 5+ age")
    #         elif rec.age < 0:
    #             raise ValidationError("Age cannot be negative.")

    # @api.model            # not yet understood
    # def create_patient_template(self):
    #     """Returns a default dictionary to pre-fill patient data."""
    #     return {
    #         'name': 'John Doe',
    #         'age': 25,
    #     }


    # @api.returns('hospital.decorator', downgrade=None)
    # def get_default_partner(self):
    #     # Returns the first available partner record
    #     return self.env['hospital.patient'].search([], limit=5)
    #
    # default_partner = self.env['custom.model'].get_default_partner()

