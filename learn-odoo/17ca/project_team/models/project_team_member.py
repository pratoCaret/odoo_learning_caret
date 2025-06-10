from odoo import api,fields,models
from odoo.exceptions import ValidationError, UserError, RedirectWarning

class ProjectTeamMember(models.Model):
    _name = "project.team.member"
    _description = "Project Team Member | This is the project task by Tejashree Ma'am"
    _rec_name = "display_name"
    _inherit = ["mail.thread", "mail.activity.mixin"]


    name = fields.Char(string="Name", required=True)

# address :
    house_no = fields.Char(string="House No.", required=True)
    street = fields.Char(string="Street", required=True)
    street2 = fields.Char(string="Street2")
    country_id = fields.Many2one(
        'res.country',
        string="Country",
        required=True
    )
    state_id = fields.Many2one(
        'res.country.state',
        string="State",
        domain="[('country_id', '=', country_id)]",
        required=True
    )
    city_id = fields.Many2one(
        'res.state.city',
        string="City",
        domain="[('state_id', '=', state_id)]",
        required=True
    )
    zip_code = fields.Char(string="ZIP Code")
#-----------------------------------------------------

    mobile = fields.Char(string="Phone No", required=True)
    user_id = fields.Many2one('res.users', string="User", required=True, domain="[('share','=','False')]", context={'search_default_employee': 1})
    email = fields.Char(related='user_id.email', string="Email", store=True, readonly=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('other', 'Other')], string="Gender")
    birth_date = fields.Date(string="DOB", required=True)
    image = fields.Image(string="Upload User Image", max_width=128, max_height=128)
    bio_data = fields.Html(string="Bio Data")
    active = fields.Boolean(default=True)
    timesheet_ids = fields.One2many('account.analytic.line', 'user_id')#, domain=[('task_id','!=',False)], string="Timesheets")
    display_name = fields.Char(compute='_compute_display_name', store=True)

    @api.onchange('city_id')
    def _onchange_city_id(self):
        if self.city_id:
            self.zip_code = self.city_id.zip_code
        else:
            self.zip_code = False

    @api.constrains('mobile')
    def _check_phone_length(self):
        for rec in self:
            if rec.mobile and len(rec.mobile) != 10:
                raise ValidationError("Phone number must be exactly 10 digits.")

    @api.depends('name', 'email')
    def _compute_display_name(self):
        for rec in self:
            rec.display_name = f"{rec.name or ''} / {rec.email or ''}"

    # @api.model
    # def create(self, vals):
    #     # user_vals =
    #     user = self.env['res.users'].create({
    #             'name': vals.get('name'),
    #             'login': vals.get('name').replace(' ', '.').lower() or '',
    #             'email': vals.get('email'),
    #         })
    #     vals['user_id'] = user.id
    #     return super().create(vals)

    def copy(self, default=None):
        raise UserError("You are not allowed to Duplicate team members.")