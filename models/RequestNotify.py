from odoo import models, fields, api
 
class RequestNotify(models.Model):
    _inherit = 'cclog.request'

    @api.model
    def create(self, values):
        res = super(RequestNotify, self).create(values)
    
        template_id = self.env.ref('itsm.email_template_create_request').id
        template =  self.env['mail.template'].browse(template_id)
        template.send_mail(res.id,force_send=True)
        return res
