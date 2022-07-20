from odoo import models, fields, api
from datetime import datetime


class ticketincident(models.Model):
    _name = "cclog.incident"
    _description = "This is the incident model"
    _rec_name = 'title'

    title = fields.Char(string='Title', required=True)
    description = fields.Text(string="Description", required=True)
    state = fields.Selection(
        [('N', 'New'), ('A', 'Assign'), ('RA', 'Re Assign'), ('P', 'Pending'), ('R', 'Resolved'), ('RO', 'Re Open'),
         ('C', 'Closed')], string="Status", required=True, default="N")
    start_date = fields.Datetime(string='Start Date', default=datetime.today())
    end_date = fields.Datetime(string='Start Date')
    close_date = fields.Datetime(string='Close Date')
    service_id = fields.Many2one('services.services', ondelete='cascade', string='Service')
    service_subcategory_id = fields.Many2one('services.subcategory',ondelete='cascade', string="Service Sub Category",domain = [('request_type','=','I')] )
    resolution_comment = fields.Text(string="Comment")
    resolution_date = fields.Datetime(string='Resolution Date', default=datetime.today())
    pending_comment = fields.Text(string="Pending Comment")
    pending_date = fields.Datetime(string='Pending Date Date', default=datetime.today())
    rating = fields.Selection(
        [('very_satified', 'Very Satified'), ('satified', 'Satified'), ('disatified', 'Disatified')])
    closing_date = fields.Datetime(string='Close Date', default=datetime.today())
    team_id = fields.Many2one('cclog.team', ondelete='cascade', string="Team", domain=[('state', '=', 'true')])
    agent_id = fields.Many2one('cclog.agent', ondelete='cascade', string="Agent")
  
    @api.onchange ('service_id')
    def on_change_service_id(self):
        for rec in self:
            return {'domain': {'service_subcategory_id': [('service_id', '=', self.service_id.id)]}}
    def action_reassign(self):
        for rec in self:
            rec.state = 'RA'


    def action_reopen(self):
        for rec in self:
            rec.state = 'RO'

