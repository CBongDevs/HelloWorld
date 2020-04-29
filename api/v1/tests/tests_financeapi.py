import unittest
import financeapi
from unittest import mock

class TestFinanceApiMethods(unittest.TestCase):
    @unittest.skip("cannot set built-in attributes")
    def test_current_time(self):
        with mock.patch('financeapi.datetime.now', return_value='the current time'):
            model = financeapi.current_time()
            self.assertEqual(model['time'], 'the current time')
        
    def test_database_url(self):
        with mock.patch('financeapi.os.getenv', return_value='database-url'):
            model = financeapi.current_time()
            self.assertEqual(model['database_url'], 'database-url')
