from odoo import models, fields

class Branch(models.Model):
    _name = "cclog.branch"
    _description = "This is a branch model"
    _rec_name ="branch_name"
    
    status = fields.Selection([('active', 'Active'),('innactive', 'Innactive')],default="active", string="Status")
    branch_name = fields.Char(string="Branch Name", required=True)
    user_id = fields.One2many('res.partner','branch_id_cclog', string="Name")
  
    
   