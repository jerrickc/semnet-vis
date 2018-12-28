import unittest

from final_242.model.Graph import Graph
from final_242.model.Nodes import Node
from final_242.model.Edges import Edge, EDGETYPES


class TestGraphMethods(unittest.TestCase):
    def setUp(self):
        self.graph = Graph()
        self.graph.add_node(Node("test"))
        self.graph.add_node(Node("test2"))
        self.graph.add_edge(1, 2, None)

    def test_edge(self):
        self.assertEqual(self.graph.get_edge(0).get_type(), EDGETYPES(1))

    def test_nodes(self):
        self.assertEqual(self.graph.get_node(0).name, "test")
        self.assertEqual(self.graph.get_node(1).name, "test2")

    def test_metadata(self):
        self.assertEqual(self.graph.num_edges(), 1)
        self.assertEqual(self.graph.num_nodes(), 2)

    def test_json(self):
        print(self.graph.jsonify())
        #self.assertEqual(self.test_json(), )

if __name__ == '__main__':
        unittest.main()
