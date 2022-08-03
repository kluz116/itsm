from odoo import api, fields, models
from datetime import datetime,timedelta
from pytz import timezone 

class RequestsPendingTicket(models.TransientModel):
    _name = "cclog.pending_tickets_wizard"
    _description = "Pending Requests"
    _rec_name = 'pending_comment'

    state = fields.Selection(
        [('N', 'New'), ('A', 'Assign'), ('RA', 'Re Assign'), ('P', 'Pending'), ('R', 'Resolved'), ('RO', 'Re Open'),
         ('C', 'Closed')], string="Status", required=True, default="A")
    
    pending_comment = fields.Text(string="Pending Comment", required=True)
    pending_date = fields.Datetime(string='Pending Date Date', default=datetime.today())
    pending_escalation =  fields.Char(string='Excalation', compute='comp_time_hod')

    @api.depends('pending_date')
    def comp_time_hod(self):
        east_africa = timezone('Africa/Nairobi')
        date_time = datetime.now(east_africa)+ + timedelta(hours=24)
        self.pending_escalation = format(date_time, '%Y-%m-%d %H:%M') 

    @api.multi
    def action_pending_agent(self):
        self.write({'state': 'P'})
        requests = self.env['cclog.request'].browse(self._context.get('active_ids'))
        for req in requests:
            req.pending_comment = self.pending_comment
            req.pending_date = self.pending_date
            req.state = self.state

            template_id = self.env.ref('cclog.email_template_pending_request').id
            template =  self.env['mail.template'].browse(template_id)
            template.send_mail(req.id,force_send=True)
    
