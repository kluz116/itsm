from odoo import api, fields, models
from datetime import datetime

class IncidentAssignTicket(models.TransientModel):
    _name = "cclog.tickets_incidents_assign_wizard"
    _description = "Assign Request"
    _rec_name = 'agent'

    
    branch_id = fields.Many2one('cclog.branch',string ='Team', required=True)
    agent = fields.Many2one('res.partner','Agent',domain="[('branch_id_cclog', '=', branch_id)]")
    state = fields.Selection(
        [('N', 'New'), ('A', 'Assign'), ('RA', 'Re Assign'), ('P', 'Pending'), ('R', 'Resolved'), ('RO', 'Re Open'),
         ('C', 'Closed')], string="Status", required=True, default="N")
    assign_date = fields.Datetime(string='Assignment Date', default=datetime.today())
 
    @api.multi
    def action_assign_agent(self):
        self.write({'state': 'A'})
        incidents = self.env['cclog.request'].browse(self._context.get('active_ids'))
        for incident in incidents:
            incident.state = self.state
            incident.branch_id = self.branch_id.id
            incident.agent = self.agent.id
            incident.assign_date = self.assign_date
        
