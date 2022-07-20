from odoo import api, fields, models
from datetime import datetime

class ChangeApprove(models.TransientModel):
    _name = "itsm.approve_change_wizard"
    _description = "Approve Change"
    _rec_name = 'approval_comment'

    
    state =  fields.Selection([('new','New'),('validate','Validate'),('assign','Assign'),('plan','Plan'),('approve','Approve'),('reject','Reject'),('implement','Implement'),('close','close')],string="Status", required=True, default="validate")
    approval_comment = fields.Text(string="Comment")
    approval_date =  fields.Datetime(string='Approval Date', default=datetime.today())

    @api.multi
    def change_approve_agent(self):
        self.write({'state': 'approve'})
        changes = self.env['itsm.change'].browse(self._context.get('active_ids'))
        for change in changes:
            change.state = self.state
            change.approval_comment = self.approval_comment
            change.approval_date = self.approval_date
        
