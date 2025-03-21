from odoo import models, fields, api
import requests

class EmployeeEAU(models.Model):
    _inherit = 'hr.employee'

    def action_get_eau(self):
        """ Fake eAU-Anfrage (später durch echte API ersetzen) """
        response = requests.get('https://jsonplaceholder.typicode.com/todos/1')  # Dummy API
        if response.status_code == 200:
            eau_data = response.json()
            self.env['hr.leave'].create({
                'employee_id': self.id,
                'holiday_status_id': 1,  # MUSS mit eurer Odoo-Abwesenheitsart übereinstimmen
                'date_from': fields.Date.today(),
                'date_to': fields.Date.today(),
                'state': 'validate',
            })
        return True