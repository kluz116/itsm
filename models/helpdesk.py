from odoo import models, fields, api
from datetime import datetime


class ticketrequest(models.Model):
    _name = "cclog.request"
    _description =""
    _rec_name ='title'

    title = fields.Char(string='Title', required=True)
    description  = fields.Text(string="Description", required=True)
    branch_id = fields.Many2one('cclog.branch',string ='Team', required=True)
    agent = fields.Many2one('res.partner','Agent',domain="[('branch_id_cclog', '=', branch_id)]")
    state =  fields.Selection([('N','New'),('A','Assigned'),('RA','Re Assign'),('P','Pending'),('R','Resolved'),('RO','Re Open'),('C','Closed')],string="Status", required=True, default="A")
    start_date = fields.Datetime(string='Start Date', default=datetime.today())
    end_date = fields.Datetime(string='Start Date')
    close_date = fields.Datetime(string='Close Date')
    trx_proof = fields.Binary(string='Upload File', attachment=True)
    client_id = fields.Many2one('cclog.client',ondelete='cascade',string='Client')
    service_id = fields.Many2one('services.services',ondelete='cascade',string='Disposition')
    service_subcategory_id = fields.Many2one('services.subcategory',ondelete='cascade', string="Disposition Sub Category",domain = [('request_type','=','R')]  )
    resolution_comment = fields.Text(string="Comment")
    resolution_date = fields.Datetime(string='Resolution Date', default=datetime.today())
    pending_comment = fields.Text(string="Pending Comment")
    pending_date = fields.Datetime(string='Pending Date Date', default=datetime.today())
    rating = fields.Selection([('very_satified', 'Very Satified'), ('satified', 'Satified'), ('disatified', 'Disatified')])
    closing_date = fields.Datetime(string='Close Date', default=datetime.today())
    base_url = fields.Char('Base Url', compute='_get_url_id', store='True')


        
    @api.depends('start_date')
    def _get_url_id(self):
        for e in self:
            web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            action_id = self.env.ref('cclog.request_list_action', raise_if_not_found=False)
            e.base_url = """{}/web#id={}&view_type=form&model=cclog.request&action={}""".format(web_base_url,e.id,action_id.id)
   

    def action_reopen(self):
        for rec in self:
            rec.state = 'RO'




    