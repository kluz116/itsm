from odoo import api, fields, models
from datetime import datetime

class ValidateChange(models.TransientModel):
    _name = "itsm.validate_change"
    _description = "Validate Change"
    _rec_name = 'validate_comment'

    

    state =  fields.Selection([('new','New'),('validate','Validate'),('assign','Assign'),('plan','Plan'),('approve','Approve'),('reject','Reject'),('implement','Implement'),('close','close')],string="Status", required=True, default="new")
    validate_comment = fields.Text(string="Comment")
    validate_date =  fields.Datetime(string='Validate Date', default=datetime.today())
 

    @api.multi
    def action_validate_change(self):
        self.write({'state': 'validate'})
        changes = self.env['itsm.change'].browse(self._context.get('active_ids'))
        for change in changes:
            change.state = self.state
            change.validate_comment = self.validate_comment
            change.validate_date = self.validate_date
            
        
