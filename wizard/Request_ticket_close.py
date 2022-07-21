from odoo import api, fields, models
from datetime import datetime

class RequestCloseTicket(models.TransientModel):
    _name = "cclog.close_tickets_wizard"
    _description = "Close Request"
    _rec_name = 'rating'

    state = fields.Selection(
        [('N', 'New'), ('A', 'Assign'), ('RA', 'Re Assign'), ('P', 'Pending'), ('R', 'Resolved'), ('RO', 'Re Open'),
         ('C', 'Closed')], string="Status", required=True, default="R")
    rating = fields.Selection(
            [('very_satified', 'Very Satified'), ('satified', 'Satified'), ('disatified', 'Disatified')],
            default="satified")
    closing_date = fields.Datetime(string='Close Date', default=datetime.today())


    @api.multi
    def action_close_request_agent(self):
        self.write({'state': 'C'})
        requests = self.env['cclog.request'].browse(self._context.get('active_ids'))
        for request in requests:
            request.rating = self.rating
            request.closing_date = self.closing_date
            request.state = self.state
    

