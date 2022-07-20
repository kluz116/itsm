from odoo import api, fields, models
from datetime import datetime

class ChangeReject(models.TransientModel):
    _name = "itsm.reject_change_wizard"
    _description = "Approve Change"
    _rec_name = 'reject_comment'

    
    state =  fields.Selection([('new','New'),('validate','Validate'),('assign','Assign'),('plan','Plan'),('approve','Approve'),('reject','Reject'),('implement','Implement'),('close','close')],string="Status", required=True, default="validate")
    reject_comment = fields.Text(string="Reject Comment")
    reject_date =  fields.Datetime(string='Reject Date', default=datetime.today())
    
    @api.multi
    def change_reject_agent(self):
        self.write({'state': 'reject'})
        changes = self.env['itsm.change'].browse(self._context.get('active_ids'))
        for change in changes:
            change.state = self.state
            change.reject_comment = self.reject_comment
            change.reject_date = self.reject_date
        
