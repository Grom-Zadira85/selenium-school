from flask import Flask, jsonify
import unittest


app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({"Hello": "World"})

class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"Hello": "World"})

if __name__ == "__main__":
    unittest.main()