from odoo import api, fields, models
from datetime import datetime

class ChangeAssignTicket(models.TransientModel):
    _name = "cclog.assign_change_wizard"
    _description = "Assign Change"
    _rec_name = 'team_id'

    
    
    state =  fields.Selection([('new','New'),('validate','Validate'),('assign','Assign'),('plan','Plan'),('approve','Approve'),('reject','Reject'),('implement','Implement'),('close','close')],string="Status", required=True, default="validate")
    team_id = fields.Many2one('cclog.team', string="Team")
    agent_id = fields.Many2one('cclog.agent', string="Agent")
    supervisor_id = fields.Many2one('cclog.agent', string="Supervisor",domain = [('change_cad','=','supervisor')]  )
    manager_id = fields.Many2one('cclog.agent', string="Manager",domain = [('change_cad','=','manager')]  )
    assign_date = fields.Datetime(string='Assignment Date', default=datetime.today())
    
    @api.onchange ('team_id')
    def on_change_teamid(self):
        for rec in self:
            return {'domain': {'agent_id': [('team_id', '=', self.team_id.id)]}}


    @api.multi
    def change_assign_agent(self):
        self.write({'state': 'assign'})
        changes = self.env['cclog.change'].browse(self._context.get('active_ids'))
        for change in changes:
            change.state = self.state
            change.team_id = self.team_id
            change.agent_id = self.agent_id
            change.supervisor_id = self.supervisor_id
            change.manager_id = self.manager_id
            change.assign_date = self.assign_date
        
