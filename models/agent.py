from odoo import models, fields, api
from datetime import datetime

class agent(models.Model):
    _name = "itsm.agent"
    _description = "this shows all agents that get mapped to tickets"
    _rec_name ="firstname"

    firstname = fields.Char(string="Firstname", required=True)
    lastname = fields.Char(string="Lastname", required=True)
    change_cad =  fields.Selection([('none','None'),('supervisor','Supervisor'),('manager','Manager')],string="Change Cad Responsibility", required=True, default="none")
    team_id = fields.Many2one('itsm.team',ondelete='cascade',string='Team')