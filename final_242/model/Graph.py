from final_242.model import Edges
from final_242.model.Edges import Edge
import json


class Graph:
    def __init__(self):
        self.nodes = []
        self.edges = []
        self.metadata = {}

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, node1, node2, edge_type):
        if edge_type:
            self.edges.append(Edge(node1, node2, edge_type))
        else:
            self.edges.append(Edge(node1, node2, Edges.EDGETYPES(1)))

    def get_node(self, idx):
        return self.nodes[idx]

    def get_edge(self, idx):
        return self.edges[idx]

    def num_edges(self):
        return len(self.edges)

    def num_nodes(self):
        return len(self.nodes)

    def jsonify(self):
        temp_obj = {"nodes": [], "edges": []}
        for node in self.nodes:
            temp_obj["nodes"].append(node.jsonify())
        for edge in self.edges:
            temp_obj["edges"].append(edge.jsonify())
        temp_obj["metadata"] = json.dumps(self.metadata)
        return json.dumps(temp_obj)
