from odoo import api, fields, models
from datetime import datetime

class IncidentCloseTicket(models.TransientModel):
    _name = "itsm.tickets_incidents_close_wizard"
    _description = "Close Incident"
    _rec_name = 'rating'

    state = fields.Selection(
        [('N', 'New'), ('A', 'Assign'), ('RA', 'Re Assign'), ('P', 'Pending'), ('R', 'Resolved'), ('RO', 'Re Open'),
         ('C', 'Closed')], string="Status", required=True, default="R")
    rating = fields.Selection(
            [('very_satified', 'Very Satified'), ('satified', 'Satified'), ('disatified', 'Disatified')],
            default="satified")
    closing_date = fields.Datetime(string='Close Date', default=datetime.today())


    @api.multi
    def action_close_agent(self):
        self.write({'state': 'C'})
        incidents = self.env['itsm.incident'].browse(self._context.get('active_ids'))
        for incident in incidents:
            incident.rating = self.rating
            incident.closing_date = self.closing_date
            incident.state = self.state
    

