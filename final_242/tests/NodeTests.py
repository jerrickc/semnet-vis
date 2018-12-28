import unittest
from final_242.model.Nodes import Node


class TestNodeMethods(unittest.TestCase):
    def setUp(self):
        self.newNode = Node("test")

    def test_data(self):
        self.newNode.set_data("testdata")
        self.assertEqual(self.newNode.get_data(), "testdata")

    def test_position(self):
        self.newNode.set_position(1, 1)
        self.assertEqual(self.newNode.get_position(), (1, 1))

    def test_json(self):
        self.newNode.set_data("testdata")
        self.newNode.set_position(1, 1)
        print(self.newNode.jsonify())
        self.assertEqual(self.newNode.jsonify(), "{\"name\": \"test\", \"data\": \"testdata\", \"x\": 1, \"y\": 1}")


if __name__ == '__main__':
        unittest.main()
