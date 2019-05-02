from app import app
import unittest
import json

class BlueApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_customer(self):
        response = self.app.get('/customers/1')
        string = response.data.decode('utf-8')
        json_obj = json.loads(string)
        assert "[{'customer_id': 1, 'first_name': 'Jai', 'last_name': 'Khanna'}, {'accounts': [{'account_id': 1, 'balance': 150, 'customer_id': 1}, {'account_id': 3, 'balance': 120, 'customer_id': 1}]}, {'transactions': [{'transaction_id': 1, 'account_id': 1, 'amount': 200}, {'transaction_id': 2, 'account_id': 1, 'amount': -50}, {'transaction_id': 4, 'account_id': 3, 'amount': 120}]}]" in str(json_obj)

    def test_create_account(self):
        response = self.app.put('/customers/1', data=dict(initial_balance=20))
        string = response.data.decode('utf-8')
        json_obj = json.loads(string)
        assert "[{'customer_id': 1, 'first_name': 'Jai', 'last_name': 'Khanna'}, {'accounts': [{'account_id': 1, 'balance': 150, 'customer_id': 1}, {'account_id': 3, 'balance': 120, 'customer_id': 1}, {'account_id': 4, 'balance': 20, 'customer_id': 1}]}, {'transactions': [{'transaction_id': 1, 'account_id': 1, 'amount': 200}, {'transaction_id': 2, 'account_id': 1, 'amount': -50}, {'transaction_id': 4, 'account_id': 3, 'amount': 120}, {'transaction_id': 4, 'account_id': 4, 'amount': 20}]}]" in str(json_obj)

if __name__ == '__main__':
    unittest.main()