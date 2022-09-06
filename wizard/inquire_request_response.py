from odoo import api, fields, models
from datetime import datetime

class RequestInquireResponse(models.TransientModel):
    _name = "cclog.inquire_response_wizard"
    _description = "Pending Requests"
    _rec_name = 'Inquire_comment_response'

    Inquire_comment_response = fields.Text(string="Inquire Comment", required=True)
    Inquire_date_response = fields.Datetime(string='Inquire Date ', default=datetime.today())
    Inquired_by_response = fields.Many2one('res.users','Inquired By:',default=lambda self: self.env.user)
  

    @api.multi
    def action_inquire_agent_resp(self):
        requests = self.env['cclog.request'].browse(self._context.get('active_ids'))
        for req in requests:
            req.Inquire_comment_response = self.Inquire_comment_response
            req.Inquire_date_response = self.Inquire_date_response
            req.Inquired_by_response = self.Inquired_by_response
        

            template_id = self.env.ref('cclog.email_template_inquire_request_response').id
            template =  self.env['mail.template'].browse(template_id)
            template.send_mail(req.id,force_send=True)
    
