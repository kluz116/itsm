from odoo import api, fields, models
from datetime import datetime

class ChangeClose(models.TransientModel):
    _name = "itsm.close_change"
    _description = "Close Incident"
    _rec_name = 'rating'

    state =  fields.Selection([('new','New'),('validate','Validate'),('assign','Assign'),('plan','Plan'),('approve','Approve'),('reject','Reject'),('implement','Implement'),('close','close')],string="Status", required=True, default="implement")
    rating = fields.Selection(
            [('very_satified', 'Very Satified'), ('satified', 'Satified'), ('disatified', 'Disatified')],
            default="satified")
    closing_date = fields.Datetime(string='Close Date', default=datetime.today())


    @api.multi
    def action_close_agent(self):
        self.write({'state': 'close'})
        incidents = self.env['itsm.change'].browse(self._context.get('active_ids'))
        for incident in incidents:
            incident.rating = self.rating
            incident.closing_date = self.closing_date
            incident.state = self.state
    

