from flask_interface import Flask, render_template, request
import unittest
from unittest.mock import MagicMock

class TestFlaskInterface(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.testing = True
        self.client = self.app.test_client()

    def test_home(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), render_template('index.html'))

    def test_schedule(self):
        with self.app.test_request_context('/schedule', method='POST', data={'event_name': 'Test Event', 'event_date': '2022-01-01'}):
            response = self.client.post('/schedule')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.data.decode('utf-8'), render_template('schedule.html', event_name='Test Event', event_date='2022-01-01'))

    def test_insights(self):
        response = self.client.get('/insights')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), render_template('insights.html'))

    def test_knowledge_graph(self):
        response = self.client.get('/knowledge_graph')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), render_template('knowledge_graph.html'))

    def test_time_travel(self):
        response = self.client.get('/time_travel')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), render_template('time_travel.html'))

    def test_multimodality(self):
        response = self.client.get('/multimodality')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), render_template('multimodality.html'))

if __name__ == '__main__':
    unittest.main()
