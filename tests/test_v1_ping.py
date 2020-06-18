from api.v1.controllers import ping
from unittest.mock import patch
from datetime import datetime

class TestV1PingMethods:
    @patch('api.v1.controllers.ping.get_current_time')
    def test_ping(self, mock_now):
        mock_now.return_value = datetime(1969, 7, 21, 2, 56)
        result = ping.ping()
        assert str(mock_now.return_value) in result