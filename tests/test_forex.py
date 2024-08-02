import unittest
from forex_python.forex import hello_world

class TestModule1(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, world!")

if __name__ == '__main__':
    unittest.main()
