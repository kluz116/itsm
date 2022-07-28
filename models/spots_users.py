from odoo import models, fields

class res_user(models.Model):
    _inherit = 'res.partner'
    

    branch_id_cclog = fields.Many2one('cclog.branch',string ='Parent Branch')


