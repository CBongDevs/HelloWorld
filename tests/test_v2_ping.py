from api.v2.controllers.ping import Ping
from unittest.mock import patch


class TestFinanceApiMethods:
    @patch('api.v2.controllers.ping.getenv')
    @patch('api.v2.controllers.ping.db')
    def test_database_url(self, db, mock_getenv):
        mock_version_num = db.engine.execute.return_value.fetchone.return_value.__getitem__
        mock_version_num.return_value = 'v-abc123'
        mock_getenv.return_value = 'postgres:///localhost/my-database-url'
        model = Ping().get()
        assert model['database_url'] == mock_getenv.return_value
        mock_getenv.assert_called_with('DATABASE_URL')
        assert model['db']['revision'] == mock_version_num.return_value
