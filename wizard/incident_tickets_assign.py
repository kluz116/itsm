from odoo import api, fields, models
from datetime import datetime

class IncidentAssignTicket(models.TransientModel):
    _name = "itsm.tickets_incidents_assign_wizard"
    _description = "Assign Incident"
    _rec_name = 'team_id'

    
    team_id = fields.Many2one('itsm.team', string="Team")
    state = fields.Selection(
        [('N', 'New'), ('A', 'Assign'), ('RA', 'Re Assign'), ('P', 'Pending'), ('R', 'Resolved'), ('RO', 'Re Open'),
         ('C', 'Closed')], string="Status", required=True, default="N")
    agent_id = fields.Many2one('itsm.agent', string="Agent")
    assign_date = fields.Datetime(string='Assignment Date', default=datetime.today())
    
    @api.onchange ('team_id')
    def on_change_teamid(self):
        for rec in self:
            return {'domain': {'agent_id': [('team_id', '=', self.team_id.id)]}}

    @api.multi
    def action_assign_agent(self):
        self.write({'state': 'A'})
        incidents = self.env['itsm.incident'].browse(self._context.get('active_ids'))
        for incident in incidents:
            incident.state = self.state
            incident.team_id = self.team_id
            incident.agent_id = self.agent_id
            incident.assign_date = self.assign_date
        
