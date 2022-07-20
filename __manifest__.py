# -*- coding: utf-8 -*-
{
    'name': "ITSM",

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
    'depends': ['base'],

    # always loaded
    'data': [
        'security/change_security.xml',
        'security/ir.model.access.csv',

        'wizard/Request_ticket_assign_view.xml',
        'wizard/Request_ticket_resolve_view.xml',
        'wizard/Request_ticket_close_view.xml',
        'wizard/Request_ticket_pending_view.xml',
        'wizard/change_validate_view.xml',
        'wizard/change_assign_view.xml',
        'wizard/change_plan_view.xml',
        'wizard/change_approve_view.xml',
        'wizard/change_reject_view.xml',
        'wizard/change_close_view.xml',

        'views/services.xml',
        'views/templates.xml',
        'views/helpdesk.xml',
        'views/config.inc.xml',
        'wizard/Incident_ticket_assign_view.xml',
        'wizard/incident.tickets.resolve.xml',
        'wizard/incidents_ticket_close.xml',
        'wizard/incident_tickets_pending.xml',
        'views/incidents.xml',
        'views/change.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}