from odoo import models, fields, api
from datetime import datetime

class Change(models.Model):
    _name = "itsm.change"
    _description ="This is a change managment model"
    _rec_name ='title'
    
    title = fields.Char(string='Title', required=True)
    description  = fields.Text(string="Description", required=True)
    start_date = fields.Datetime(string='Start Date', default=datetime.today())  
    state =  fields.Selection([('new','New'),('validate','Validate'),('assign','Assign'),('plan','Plan'),('approve','Approve'),('reject','Reject'),('implement','Implement'),('close','close')],string="Status", required=True, default="new")
    team_id = fields.Many2one('itsm.team', string="Team")
    agent_id = fields.Many2one('itsm.agent', string="Agent")
    team_id_supervisor = fields.Many2one('itsm.team', string="Supervisor Team")
    agent_id_supervisor = fields.Many2one('itsm.change_supervisor', string="Supervisor")
    team_id_manager = fields.Many2one('itsm.team', string="Manager Team")
    agent_id_manager = fields.Many2one('itsm.change_manager', string="Manager Team")
    assign_date = fields.Datetime(string='Assignment Date', default=datetime.today())
    validate_comment = fields.Text(string="Comment")
    validate_date =  fields.Datetime(string='Validate Date', default=datetime.today())
    fallback_plan = fields.Text(string="Fallback Plan")
    from_date =  fields.Datetime(string='From ', default=datetime.today())
    to_date =  fields.Datetime(string='To', default=datetime.today())
    rating = fields.Selection([('very_satified','Very Satified'),('satified','Satified'),('disatified','Disatified')])
    closing_date =  fields.Datetime(string='Close Date', default=datetime.today())

    @api.multi
    def action_implement(self):
        for rec in self:
            rec.state = 'implement'