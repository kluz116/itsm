from odoo import models, fields, api
from datetime import datetime

class Service(models.Model):
    _name = "services.services"
    _rec_name ='servicename'
    _description ="This is a description of a service"

    servicename = fields.Char(string="Disposition", required=True)
    

class Service_SubCategory(models.Model):
    _name = "services.subcategory"
    _rec_name ='service_subcategory_name'
    _description = "This is a description of a sub category"

    service_subcategory_name = fields.Char(string="Dispositions Sub - CategoryName",required=True)
    request_type =  fields.Selection([('R','Request'),('I','Incidents')],string="Request Type", required=True)
    service_id = fields.Many2one('services.services',ondelete='cascade',string='Disposition')
    
