from odoo import models, fields, api

class Client(models.Model):
    _name = "cclog.client"
    _description ="This is a client model"
    _rec_name = 'combination'
    
    name = fields.Char(string='Name', required=True)
    client_id = fields.Char(string='Client ID', required=True)
    account_id = fields.Char(string='Account Number', required=True)
    phone = fields.Char(string='Phone ', required=True)
    combination = fields.Char(string='Combination', compute='_compute_fields_combination')

    @api.depends('name', 'account_id')
    def _compute_fields_combination(self):
        for res in self:
            res.combination = res.name + ' : '+' ' + res.account_id

