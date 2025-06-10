from odoo import models, fields

class ResStateCity(models.Model):
    _name = 'res.state.city'
    _description = 'City'

    name = fields.Char(string='City Name', required=True, index=True, help="Enter the name of the city.")
    state_id = fields.Many2one('res.country.state', string='State', ondelete='cascade', index=True, required=True, help="Select the state for this city.")
    zip_code = fields.Char(string="ZIP Code", help="Enter the ZIP/postal code for the city.")
