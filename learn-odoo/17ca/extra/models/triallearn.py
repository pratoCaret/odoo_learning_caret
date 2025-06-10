from odoo import fields,models,api

class HospitalTrialLearn(models.Model):
    _name = "hospital.triallearn"
    _description = "trial for the things I learn"
    _inherit = ['mail.thread']
    _rec_name = 'name'

    # is_company=fields.Boolean(string="default")
    name=fields.Char(string="name", tracking=True, index=True)
    # surname=fields.Char(string="surname")

    # tryBool=fields.Boolean(string="trying Boolean :", default=False)
    # file_data = fields.Binary(string="Upload File", store=True) # not happening with store true or false nor with attachment
    # notes = fields.Text(string="Notes")

    # Currency field is mandatory for monetary field to work
    # currency_id = fields.Many2one(
    #     'res.currency',
    #     string="Currency",
    #     required=True,
    #     # default=lambda self: self.env.company.currency_id.id
    # )
    # consultation_fee = fields.Monetary(
    #     string="Consultation Fee",
    #     currency_field='currency_id'
    # )

    # tag_m2m_ids=fields.Many2many( 'hospital.doctor','rel_triallearn_doctor','triallearn_id','doctor_id',string='m2m:', context={'default_is_company':'1'})
    # tag_o2m_ids=fields.One2many('hospital.doctor', string='m2o')

    # computed_value = fields.Integer(compute='_compute_value') # COMPUTE # will return a value after computation # performs computation on any fields mentioned.
    # @api.depends('name')
    # def _compute_value(self):
    #     for record in self:
    #         record.computed_value = len(record.name)

    # full_name = fields.Char(compute="_compute_full_name", inverse="_inverse_full_name", string="full name", default=" ") # INVERSE
    # def _compute_full_name(self):
    #     for record in self:
    #         record.full_name = f"{record.name or ' '} {record.surname or ' '}"
    #         print("--------->>>>>>>>>>>>>>>>>"+record.full_name)
    #
    # def _inverse_full_name(self):
    #     for record in self:
    #         names = record.full_name.split(' ',1)
    #         record.name = names[0]
    #         record.surname = names[-1]


    # display_name = fields.Char(compute="_compute_display_name", search="_search_display_name") # searching
    # def _search_display_name(self, operator, value):
    #     return [('name', operator, value)]

    # related_name = fields.Char(related='name', readonly=1)

    # tag_m2o=fields.Many2one('hospital.doctor', string='many2one')
    # user_m2o = fields.Many2one('hospital.patient', ondelete='cascade')

    # description = fields.Text(string="descriptoin", translate=True, default="this is a translation trial")

    # state = fields.Selection([
    #     ('draft', 'Draft'),
    #     ('confirmed', 'Confirmed'),
    #     ('done', 'Done'),
    #     ('cancelled', 'Cancelled'),
    # ], string="Status", default='draft', tracking=True)
    # notes = fields.Text(string="Doctor Notes", states={'done': {'readonly': True}})

