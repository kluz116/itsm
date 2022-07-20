from odoo import api, fields, models
from datetime import datetime

class IncidentResolveTicket(models.TransientModel):
    _name = "cclog.tickets_incidents_resolve_wizard"
    _description = "Resolve Incident"
    _rec_name = 'resolution_comment'

    state = fields.Selection(
        [('N', 'New'), ('A', 'Assign'), ('RA', 'Re Assign'), ('P', 'Pending'), ('R', 'Resolved'), ('RO', 'Re Open'),
         ('C', 'Closed')], string="Status", required=True, default="A")
    resolution_comment = fields.Text(string="Comment", required=True)
    resolution_date = fields.Datetime(string='Resolution Date', default=datetime.today())

    @api.multi
    def action_resolve_agent(self):
        self.write({'state': 'R'})
        incidents = self.env['cclog.incident'].browse(self._context.get('active_ids'))
        for incident in incidents:
            incident.resolution_comment = self.resolution_comment
            incident.resolution_date = self.resolution_date
            incident.state = self.state
    
