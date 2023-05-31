import unittest
from flask import Flask, request
from main  import upload_file

app = Flask(__name__)
def setUp(self):
    self.app = Flask(__name__)
    self.app_context = self.app.test_request_context()
    self.app_context.push()

def tearDown(self):
    self.app_context.pop()

def test_upload_file(self):
    with self.app.test_request_context('/', data={'file': (open('example.txt', 'rb'), 'example.txt')}, method='POST'):
        response = upload_file()
    self.assertEqual(response.status_code, 200)

def test_most_common_word(self):
    with self.app.test_request_context('/', data={'file': (open('example.txt', 'rb'), 'example.txt')}, method='POST'):
        response = upload_file()
    self.assertEqual(response.status_code, 200)
    self.assertIn(b'most', response.data)

if __name__ == '__main__':
    app.run()