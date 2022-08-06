from odoo import api, fields, models
from datetime import datetime

class RequestInquire(models.TransientModel):
    _name = "cclog.inquire_wizard"
    _description = "Pending Requests"
    _rec_name = 'Inquire_comment'

    Inquire_comment = fields.Text(string="Inquire Comment", required=True)
    Inquire_date = fields.Datetime(string='Inquire Date ', default=datetime.today())
    Inquired_by = fields.Many2one('res.users','Inquired By:',default=lambda self: self.env.user)
  

    @api.multi
    def action_inquire_agent(self):
        requests = self.env['cclog.request'].browse(self._context.get('active_ids'))
        for req in requests:
            req.Inquire_comment = self.Inquire_comment
            req.Inquire_date = self.Inquire_date
            req.Inquired_by = self.Inquired_by
        

            template_id = self.env.ref('cclog.email_template_inquire_request').id
            template =  self.env['mail.template'].browse(template_id)
            template.send_mail(req.id,force_send=True)
    
