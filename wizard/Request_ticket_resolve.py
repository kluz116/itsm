from odoo import api, fields, models
from datetime import datetime

class RequestResolveTicket(models.TransientModel):
    _name = "cclog.resolve_ticket"
    _description = "Resolve Requests"
    _rec_name = 'resolution_comment'

    state = fields.Selection(
        [('N', 'New'), ('A', 'Assign'), ('RA', 'Re Assign'), ('P', 'Pending'), ('R', 'Resolved'), ('RO', 'Re Open'),
         ('C', 'Closed')], string="Status", required=True, default="R")
    resolution_comment = fields.Text(string="Comment", required=True)
    resolution_date = fields.Datetime(string='Resolution Date', default=datetime.today())

    @api.multi
    def action_requests_resolve_agent(self):
        self.write({'state': 'R'})
        requests = self.env['cclog.request'].browse(self._context.get('active_ids'))
        for request in requests:
        
            requests.resolution_comment = self.resolution_comment
            requests.resolution_date = self.resolution_date
            requests.state = self.state

            template_id = self.env.ref('cclog.email_template_resolved_request').id
            template =  self.env['mail.template'].browse(template_id)
            template.send_mail(request.id,force_send=True)
    
