from odoo import models, fields

class res_user(models.Model):
    _inherit = 'res.partner'
    
    user_role = fields.Selection([('credit_supervisor', 'Credit Supervisor'),('manager', 'Branch Manager'), ('accountant', 'Branch Accountant'),('teller', 'Teller')], string="User Role")
    branch_id_cclog = fields.Many2one('cclog.branch',string ='Parent Branch')


