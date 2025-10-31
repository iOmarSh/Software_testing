import requests

class EmployeeRepository:
    def __init__(self, api_url):
        self._api_url = api_url

    def get_employees(self):

        try:
            response = requests.get(self._api_url)

            if response.status_code == 200:
                employees = response.json()
                sorted_employees = sorted(employees, key=lambda x: x['id'])
                return sorted_employees
            else:
                return None
        except requests.RequestException:
            return None