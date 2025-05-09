{
    'name': 'Custom eAU Modul',
    'version': '1.0',
    'summary': 'Automatische eAU-Abfrage für Odoo',
    'description': 'Fügt einen Button hinzu, um Krankmeldungen automatisch abzurufen.',
    'category': 'Human Resources',
    'author': 'Milo Racz',
    'depends': ['hr'],
    'data': [
        'views/employee_view.xml',
        'views/eau_menu.xml',
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'assets': {
    'web.assets_backend': [
        'custom_eau/static/src/css/eau_style.css',
    ],
},
}