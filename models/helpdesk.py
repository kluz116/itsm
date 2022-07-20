from odoo import models, fields, api
from datetime import datetime


class ticketrequest(models.Model):
    _name = "ticket.request"
    _description =""
    _rec_name ='title'

    title = fields.Char(string='Title', required=True)
    description  = fields.Text(string="Description", required=True)
    branch_id = fields.Many2one('cclog.branch',string ='Branch Or Department', required=True)
    agent = fields.Many2one('res.partner','Agent',domain="[('branch_id_cclog', '=', branch_id)]")
    state =  fields.Selection([('N','New'),('A','Assign'),('RA','Re Assign'),('P','Pending'),('R','Resolved'),('RO','Re Open'),('C','Closed')],string="Status", required=True, default="N")
    start_date = fields.Datetime(string='Start Date', default=datetime.today())
    end_date = fields.Datetime(string='Start Date')
    close_date = fields.Datetime(string='Close Date')
    client_id = fields.Many2one('cclog.client',ondelete='cascade',string='Client')
    service_id = fields.Many2one('services.services',ondelete='cascade',string='Disposition')
    service_subcategory_id = fields.Many2one('services.subcategory',ondelete='cascade', string="Disposition Sub Category",domain = [('request_type','=','R')]  )
    resolution_comment = fields.Text(string="Comment")
    resolution_date = fields.Datetime(string='Resolution Date', default=datetime.today())
    pending_comment = fields.Text(string="Pending Comment")
    pending_date = fields.Datetime(string='Pending Date Date', default=datetime.today())
    rating = fields.Selection([('very_satified', 'Very Satified'), ('satified', 'Satified'), ('disatified', 'Disatified')])
    closing_date = fields.Datetime(string='Close Date', default=datetime.today())

        
    def action_resolve(self):
        self.write({'state': 'R'})
        id = self.id
        return {
        'name': self.title,
        'res_model': 'ticket.request',
        'type': 'ir.actions.act_window',
        'res_id': self.id,
        'context': {},
        'view_type': 'form',
        'view_mode': 'form',
        'views': [(self.env.ref('cclog.resolve_ticket_request_form_view').id, 'form')],
        'view_id': self.env.ref('cclog.resolve_ticket_request_form_view').id,
        'target': 'new'
        }
    
    def action_reassign(self):
        for rec in self:
            rec.state = 'RA'

    def action_pending(self):
        self.write({'state': 'P'})
        id = self.id
        return {
        'name': self.title,
        'res_model': 'ticket.request',
        'type': 'ir.actions.act_window',
        'res_id': self.id,
        'context': {},
        'view_type': 'form',
        'view_mode': 'form',
        'views': [(self.env.ref('cclog.pending_ticket_request_form_view').id, 'form')],
        'view_id': self.env.ref('cclog.pending_ticket_request_form_view').id,
        'target': 'new'
        }

    def action_reopen(self):
        for rec in self:
            rec.state = 'RO'

    def action_close(self):
        self.write({'state': 'C'})
        id = self.id
        return {
        'name': self.title,
        'res_model': 'ticket.request',
        'type': 'ir.actions.act_window',
        'res_id': self.id,
        'context': {},
        'view_type': 'form',
        'view_mode': 'form',
        'views': [(self.env.ref('cclog.close_ticket_request_form_view').id, 'form')],
        'view_id': self.env.ref('cclog.close_ticket_request_form_view').id,
        'target': 'new'
        }

class TicketAssign(models.Model):
    _name ="cclog.ticketassign"
    _description = ""
    _rec_name ='team_id'

    team_id = fields.Many2one('cclog.team',ondelete='cascade', string="Team")
    agent_id = fields.Many2one('cclog.agent',ondelete='cascade', string="Agent", domain=[('team_id','in','team_id')])
    assign_date =  fields.Datetime(string='Assignment Date', default=datetime.today())

class TicketResolve(models.Model):
    _name ="cclog.ticketresolve"
    _description = ""
    _rec_name ='resolution_comment'

    resolution_comment = fields.Text(string="Comment", required=True)
    resolution_date =  fields.Datetime(string='Resolution Date', default=datetime.today())

class TicketPending(models.Model):
    _name ="cclog.ticketpending"
    _description = ""
    _rec_name ='pending_comment'

    pending_comment = fields.Text(string="Pending Comment", required=True)
    pending_date =  fields.Datetime(string='Pending Date Date', default=datetime.today())

class TicketClosing(models.Model):
    _name ="cclog.ticketclosed"
    _description = ""
    _rec_name ='rating'

    rating = fields.Selection([('very_satified','Very Satified'),('satified','Satified'),('disatified','Disatified')], default="satified")
    closing_date =  fields.Datetime(string='Close Date', default=datetime.today())


