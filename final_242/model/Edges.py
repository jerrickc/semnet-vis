import json
from enum import Enum


class EDGETYPES(Enum):
    REQUIRES = 1
    FOLLOWS = 2
    PROVES = 3


class Edge:
    def __init__(self, from_n, to_n, edg_typ):
        self.edgetype = edg_typ
        self.nodeFrom = from_n
        self.nodeTo = to_n

    def set_type(self, edgetype):
        self.edgetype = edgetype

    #this depends on implementation, may want to split into multiple functions later
    def get_type(self):
        return self.edgetype

    def set_to_from(self, node_from, node_to):
        self.nodeFrom = node_from
        self.nodeTo = node_to

    def jsonify(self):
        jsonobj = {"edgetype": self.edgetype.value, "from": self.nodeFrom, "to": self.nodeTo}
        return json.dumps(jsonobj)
