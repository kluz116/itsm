from odoo import models, fields

class Branch(models.Model):
    _name = "cclog.branch"
    _description = "This is a team model"
    _rec_name ="team_name"
    
    status = fields.Selection([('active', 'Active'),('innactive', 'Innactive')],default="active", string="Status")
    team_name = fields.Char(string="Name", required=True)
    team_email = fields.Char(string="email", required=True)
    user_id = fields.One2many('res.partner','branch_id_cclog', string="Name")
  
    
   