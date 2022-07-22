# -*- coding: utf-8 -*-
{
    'name': "CallCentre Log",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Finance Trust Bank",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail','base'],

    # always loaded
    'data': [
        'security/change_security.xml',
        'security/ir.model.access.csv',
        'data/email_template_cash_managment.xml',
        'wizard/Request_ticket_resolve_view.xml',
        'wizard/Request_ticket_close_view.xml',
        'wizard/incident.tickets.resolve.xml',
        'wizard/Request_ticket_pending_view.xml',
        'wizard/incidents_ticket_close.xml',
        'wizard/Incident_ticket_assign_view.xml',
        'views/services.xml',
        'views/helpdesk.xml',
        'views/client.xml',
        'views/branch.xml',
        'views/spots_user.xml'
        ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}