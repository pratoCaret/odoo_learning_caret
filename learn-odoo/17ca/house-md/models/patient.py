from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HospitalPatients(models.Model):
    _name = 'hospital.patient'
    _description = 'Patient Register'
    _inherit = ['mail.thread']
    _sql_constraints = [
        ('unique_name_constrain', 'unique(name)', 'name of the patient is MUST required!'),
        ('unique_patient_email', 'UNIQUE(email)', 'Email must be unique!'),
        ('positive_age', 'CHECK(age >= 0)', 'Age must be positive!'),
    ]

    name = fields.Char(string='Name', required=True, tracking=True)  # tracking will generate the change log in the main odoo files .
    email = fields.Char(string='Email', required=True, tracking=True)
    phoneNo = fields.Char(string='Phone No', required=True, tracking=True, default='+919328551638')
    age = fields.Integer(string='Age', required=True, tracking=True, default='1')
    gender = fields.Selection([('male', 'Male'),('female', 'Female')], string="Gender", required=True, tracking=True)

    blood_group = fields.Selection([
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')
    ], string="Blood Group", help="Patient's blood group", required=True)
    address = fields.Text(string="Address", required=True, help="Permanent address of the patient")
    admit_date = fields.Date(string="Admit Date", default=fields.Date.today, readonly=True, help="Date of admission")
    is_insured = fields.Boolean(string="Is Insured?", default=False, help="Does the patient have health insurance?")
    insurance_provider = fields.Char(string="Insurance Provider", help="If insured, mention provider name")
    emergency_contact = fields.Char(string="Emergency Contact", required=True, help="In case of emergency")

    age_group = fields.Selection(
        [
            ('child', 'Child (0–18)'),
            ('adult', 'Adult (19–60)'),
            ('senior', 'Senior (60+)')
        ],
        string="Age Group",
        compute='_compute_age_group',
        store=True
    )

    @api.depends('age')
    def _compute_age_group(self):
        for rec in self:
            if rec.age <= 18:
                rec.age_group = 'child'
            elif 18 < rec.age <= 60:
                rec.age_group = 'adult'
            else:
                rec.age_group = 'senior'

    # trial_field=fields.Char(string="checking")
    # # trial_field2=fields.Char(string="checking")
    #
    # @api.constrains('trial_field')
    # def trial_method(self):
    #         print("         this is trial field python constrain 1: method 1")
    #
    # # def trial_method(self):
    # #         print("         this is trial field python constrain 1: method 2")
    #
    # @api.constrains('trial_field')
    # def trial_method(self):
    #         print("          this is trial field python constrain 2: method 1")

    # def _check_email_format(self):
    #     for record in self:
    #         print(record.email)

    @api.constrains('email')
    def _check_email_format(self):
        for record in self:
            if record.email and ('@' not in record.email or '.' not in record.email):
                raise ValidationError("Please enter a valid email address.")


    @api.constrains('phoneNo')
    def _check_phone_length(self):
        for record in self:
            if record.phoneNo and len(record.phoneNo) != 13:
                raise ValidationError("Phone number must be exactly 10 digits.")


    @api.constrains('age')
    def _check_age_limit(self):
        for record in self:
            if record.age and record.age > 120:
                raise ValidationError("Age cannot be more than 120 years.")
            if record.age < 0:
                raise ValidationError("Age cannot be negative.")

    display_name = fields.Char(compute="_compute_display_name", search="_search_display_name") # SEARCH
    def _search_display_name(self, operator, value):
        return [('name', operator, value)]
