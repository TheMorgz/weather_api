import unittest
from unittest.mock import patch, Mock
import json
from api_requests import get_weather

class TestGetWeather(unittest.TestCase):

    @patch('api_requests.os.environ.get')
    @patch('api_requests.requests.get')
    def test_get_weather_success(self, mock_get, mock_env_get):
        mock_env_get.return_value = 'fake_api'
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'name': 'Test City',
            'sys': {'country': 'TC', 'sunrise': 1600000000, 'sunset': 1600040000},
            'main': {'temp': 300, 'pressure': 1013, 'humidity': 80},
            'wind': {'speed': 5, 'deg': 90},
            'clouds': {'all': 20},
            'coord': {'lat': 10, 'lon': 20},
            'dt': 1600000000
        }
        mock_get.return_value = mock_response

        result = get_weather('Test City', 'TC')
        self.assertIn('location_name', result)
        self.assertIn('temperature', result)
        self.assertIn('wind', result)
        self.assertIn('cloudiness', result)
        self.assertIn('pressure', result)
        self.assertIn('humidity', result)
        self.assertIn('sunrise', result)
        self.assertIn('sunset', result)
        self.assertIn('geo_coordinates', result)
        self.assertIn('requested_time', result)

    @patch('api_requests.os.environ.get')
    def test_get_weather_no_api_key(self, mock_env_get):
        mock_env_get.return_value = None

        with self.assertRaises(ValueError):
            get_weather('Test City', 'TC')

    @patch('api_requests.os.environ.get')
    @patch('api_requests.requests.get')
    def test_get_weather_failed_api_call(self, mock_get, mock_env_get):
        mock_env_get.return_value = 'fake_api_key'
        mock_response = Mock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        result = get_weather('Test City', 'TC')
        self.assertEqual(result, {'error': 'Failed to retrieve data from the weather service.'})

    @patch('api_requests.os.environ.get')
    @patch('api_requests.requests.get')
    def test_get_weather_json_decode_error(self, mock_get, mock_env_get):
        mock_env_get.return_value = 'fake_api_key'
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = json.JSONDecodeError("Expecting value", "", 0)
        mock_get.return_value = mock_response

        result = get_weather('Test City', 'TC')
        self.assertIn('error', result)
        self.assertTrue(result['error'].startswith('Failed to parse weather data:'))

if __name__ == '__main__':
    unittest.main()
