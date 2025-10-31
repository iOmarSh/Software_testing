import unittest
from unittest.mock import patch, Mock

import requests
from employee_repository import EmployeeRepository


class TestEmployeeRepository(unittest.TestCase):

    def setUp(self):
        self.repository = EmployeeRepository(api_url="http://dummy-api.com/employees")

        self.unsorted_data = [
            {"id": 3, "name": "Alice", "position": "Developer"},
            {"id": 1, "name": "Bob", "position": "Manager"},
            {"id": 2, "name": "Charlie", "position": "Designer"}
        ]

        self.sorted_data = [
            {"id": 1, "name": "Bob", "position": "Manager"},
            {"id": 2, "name": "Charlie", "position": "Designer"},
            {"id": 3, "name": "Alice", "position": "Developer"}
        ]
    @patch('employee_repository.requests.get')
    def test_get_employees_success_and_sorting(self, mock_get):

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = self.unsorted_data

        mock_get.return_value = mock_response

        employees = self.repository.get_employees()

        mock_get.assert_called_with("http://dummy-api.com/employees")

        self.assertEqual(employees, self.sorted_data)
        print("Test 1 (Success & Sort) Passed.")

    @patch('employee_repository.requests.get')
    def test_get_employees_error_handling(self, mock_get):

        mock_response = Mock()
        mock_response.status_code = 500

        mock_get.return_value = mock_response

        employees = self.repository.get_employees()

        self.assertIsNone(employees)
        print("Test 2 (Error Handling) Passed.")

    @patch('employee_repository.requests.get')
    def test_get_employees_network_exception(self, mock_get):

        mock_get.side_effect = requests.RequestException

        employees = self.repository.get_employees()

        self.assertIsNone(employees)
        print("Test 3 (Network Exception) Passed.")


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)