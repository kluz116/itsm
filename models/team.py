from odoo import models, fields, api
from datetime import datetime


class team(models.Model):
    _name = 'itsm.team'
    _description ='This describles individual teams'
    _rec_name = "team_name"

    team_name = fields.Char(string='Team Name', required=True)
    state = fields.Selection([('true','Yes'),('false','No')], default='false', string="Delivery Status")
    agent_id = fields.One2many('itsm.agent','team_id', string="Agent")
