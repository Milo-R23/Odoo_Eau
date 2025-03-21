{
    'name': 'Custom eAU Modul',
    'version': '1.0',
    'summary': 'Automatische eAU-Abfrage für Odoo',
    'description': 'Fügt einen Button hinzu, um Krankmeldungen automatisch abzurufen.',
    'category': 'Human Resources',
    'author': 'Dein Name',
    'depends': ['hr'],
    'data': [
        'views/employee_view.xml',
    ],
    'installable': True,
    'application': False,
}