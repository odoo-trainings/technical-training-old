{
    'name': 'Odoo Academy',
    'summary': """Academy app to manage Training""",

    'description': """
        Academy Module to manage Training:
        - Courses
        - Sessions
        - Attendees
        """,
    'license': 'OPL-1',
    'author': 'fsrs-odoo',
    'website': 'www.odoo.com',
    'category': 'Tech Training',
    
    'depends': ['mail'],
    'data': [
        'security/odoo_academy_groups.xml',
        'security/odoo_academy_security.xml',
        'security/ir.model.access.csv',
        'views/academy_menuitems.xml',
        'views/course_views.xml',
        'views/session_views.xml',
    ],
    'demo': [
        'demo/academy_demo.xml',
    ],
    'assets': {},
    
    'installable': True,
    'application': True,
    'auto_install': False,
}