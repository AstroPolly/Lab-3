import unittest
import tornado.testing
import tornado.web
from main import FibonacciGiver, make_app

class TestFibonacciGiver(tornado.testing.AsyncHTTPTestCase):
    def get_app(self):
        return make_app()

    def test_valid_input(self):
        response = self.fetch("/fibonacci/10")
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'{"n": 10, "fibonacci": 55}')

    def test_zero_input(self):
        response = self.fetch("/fibonacci/0")
        self.assertEqual(response.code, 200)
        self.assertEqual(response.body, b'{"n": 0, "fibonacci": 0}')

    def test_negative_input(self):
        response = self.fetch("/fibonacci/-5")
        self.assertEqual(response.code, 400)
        self.assertEqual(response.body, b'{"error": "n must be a non-negative integer"}')

    def test_non_integer_input(self):
        response = self.fetch("/fibonacci/abc")
        self.assertEqual(response.code, 400)
        self.assertEqual(response.body, b'{"error": "n must be an integer"}')

    def test_large_input(self):
        response = self.fetch("/fibonacci/15000")
        self.assertEqual(response.code, 400)
        self.assertEqual(response.body, b'{"error": "n is too big"}')

if __name__ == "__main__":
    unittest.main()