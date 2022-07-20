from odoo import api, fields, models
from datetime import datetime

class IncidentPendingTicket(models.TransientModel):
    _name = "cclog.tickets_incidents_pending_wizard"
    _description = "Pending Incident"
    _rec_name = 'pending_comment'

    state = fields.Selection(
        [('N', 'New'), ('A', 'Assign'), ('RA', 'Re Assign'), ('P', 'Pending'), ('R', 'Resolved'), ('RO', 'Re Open'),
         ('C', 'Closed')], string="Status", required=True, default="A")
    
    pending_comment = fields.Text(string="Pending Comment", required=True)
    pending_date = fields.Datetime(string='Pending Date Date', default=datetime.today())

    @api.multi
    def action_pending_agent(self):
        self.write({'state': 'P'})
        incidents = self.env['cclog.incident'].browse(self._context.get('active_ids'))
        for incident in incidents:
            incident.pending_comment = self.pending_comment
            incident.pending_date = self.pending_date
            incident.state = self.state
    
