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
    
    'depends': ['base'],
    'data': [],
    'demo': [
        'demo/academy_demo.xml',
    ],
    'assets': {},
    
    'installable': True,
    'application': True,
    'auto_install': False,
}