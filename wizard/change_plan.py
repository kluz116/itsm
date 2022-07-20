from odoo import api, fields, models
from datetime import datetime

class PlanChange(models.TransientModel):
    _name = "itsm.plan_change"
    _description = "Plan Change"
    _rec_name = 'fallback_plan'

    

    state =  fields.Selection([('new','New'),('validate','Validate'),('assign','Assign'),('plan','Plan'),('approve','Approve'),('reject','Reject'),('implement','Implement'),('close','close')],string="Status", required=True, default="new")
    fallback_plan = fields.Text(string="Flaback Plan")
    from_date =  fields.Datetime(string='From ', default=datetime.today())
    to_date =  fields.Datetime(string='To', default=datetime.today())


    @api.multi
    def action_plan_change(self):
        self.write({'state': 'approve'})
        changes = self.env['itsm.change'].browse(self._context.get('active_ids'))
        for change in changes:
            change.state = self.state
            change.fallback_plan = self.fallback_plan
            change.from_date = self.from_date
            change.to_date = self.to_date
            
        
