# -*- coding: utf-8 -*-
{
    'name': "rental_aparment",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'description': """
        Long description of module's purpose
    """,
    'author': "Edynson Coronado",
    'website': 'https://edynsoncoronado.wordpress.com',
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'account',
        'l10n_pe'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/journal_views.xml',
        'views/apartment_menus.xml',
        'views/apartment_views.xml',
        'report/apartment_reports.xml',
        'report/apartment_report_template.xml'
    ],
    'application': True
}
