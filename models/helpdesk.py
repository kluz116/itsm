from odoo import models, fields, api
from datetime import datetime, timedelta
from pytz import timezone 



class ticketrequest(models.Model):
    _name = "cclog.request"
    _description =""
    _rec_name ='title'

    title = fields.Char(string='Title', required=True)
    description  = fields.Text(string="Description", required=True)
    branch_id = fields.Many2one('cclog.branch',string ='Team')
    agent = fields.Many2one('res.partner','Agent',domain="[('branch_id_cclog', '=', branch_id)]")
    state =  fields.Selection([('N','New'),('A','Assigned'),('RA','Re Assign'),('P','Pending'),('R','Resolved'),('RO','Re Open'),('C','Closed'),('E','Escalated')],string="Status", required=True, default="N")
    client_state =  fields.Selection([('yes','Yes'),('no','No')],string="Is Existing Client", required=True, default="yes")
    prospect_client = fields.Char(string='Propect Client')
    start_date = fields.Datetime(string='Start Date', default=lambda self: fields.datetime.now())
    end_date = fields.Datetime(string='Start Date')
    close_date = fields.Datetime(string='Close Date')
    trx_proof = fields.Binary(string='Upload File', attachment=True)
    client_id = fields.Many2one('cclog.client',ondelete='cascade',string='Client')
    service_id = fields.Many2one('cclog.services',ondelete='cascade',string='Disposition')
    service_subcategory_id = fields.Many2one('cclog.subcategory',string="Disposition Sub Category",domain = " [('service_id','=',service_id)] " )
    resolution_comment = fields.Text(string="Comment")
    resolution_date = fields.Datetime(string='Resolution Date')
    pending_comment = fields.Text(string="Pending Comment")
    pending_date = fields.Datetime(string='Pending Date')
    pending_hour = fields.Char(string='Escalation Date')
    rating = fields.Selection([('very_satified', 'Very Satified'), ('satified', 'Satified'), ('disatified', 'Disatified')])
    closing_date = fields.Datetime(string='Close Date')
    created_by = fields.Many2one('res.users','Created By:',default=lambda self: self.env.user)
    user_id = fields.Many2one('res.users', string='User', track_visibility='onchange', readonly=True, default=lambda self: self.env.user.id)
    base_url = fields.Char('Base Url', compute='_get_url_id', store='True')
    current_agent = fields.Boolean('is current user ?', compute='_get_agent')
    current_user = fields.Boolean('is current user ?', compute='_get_user')
    #unique_field = fields.Char(string="Ref",compute='comp_name', store=True)
    pending_escalation =  fields.Date(string='Escalation')
        
    Inquire_comment = fields.Text(string="Inquire Comment")
    Inquire_date = fields.Datetime(string='Inquire Date ')
    Inquired_by = fields.Many2one('res.users','Inquired By:')
    Inquire_comment_response = fields.Text(string="Response Comment")
    Inquire_date_response = fields.Datetime(string='Response Date ')
    Inquired_by_response = fields.Many2one('res.users','Created By:')
    partner_id = fields.Many2one ('res.partner', 'Customer', default = lambda self: self.env.user.partner_id )
  


    
    @api.depends('start_date')
    def _get_url_id(self):
        for e in self:
            web_base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            action_id = self.env.ref('cclog.request_list_action', raise_if_not_found=False)
            e.base_url = """{}/web#id={}&view_type=form&model=cclog.request&action={}""".format(web_base_url,e.id,action_id.id)
    
    @api.depends('agent')
    def _get_agent(self):
        for e in self:
            partner = self.env['res.users'].browse(self.env.uid).partner_id
            e.current_agent = (True if partner.id == self.agent.id else False)

    
    @api.depends('created_by')
    def _get_user(self):
        for e in self:
            partner = self.env['res.users'].browse(self.env.uid).partner_id
            e.current_user = (True if partner.id == self.created_by.partner_id else False)
 

    def action_reopen(self):
        for rec in self:
            rec.state = 'RO'
            template_id = self.env.ref('cclog.email_template_reopen_request').id
            template =  self.env['mail.template'].browse(template_id)
            template.send_mail(rec.id,force_send=True)

    @api.model
    def _update_notified_ongoing_ticket(self):
        pending_conf = self.env['cclog.request'].search([('state', 'not in', ['R','C'])])
        for req in pending_conf:
            template_id = self.env.ref('cclog.email_template_ongoing_request').id
            template =  self.env['mail.template'].browse(template_id)
            template.send_mail(req.id,force_send=True)


   # @api.depends('start_date')
    #def comp_name(self):
        #for e in self:
        #self.unique_field =f'R-000{str(self.id)}' 

    @api.model
    def _update_expiration_pending(self):
        east_africa = timezone('Africa/Nairobi')
        now_date = datetime.now(east_africa).strftime('%Y-%m-%d')
        now_time = datetime.now(east_africa).strftime('%H:%M')
        self.search([('&'),('pending_escalation', '=', now_date),('pending_hour','>=',now_time),('state','=','P')]).write({'state': "E"})



        




    