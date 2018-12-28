import json


class Node:
    def __init__(self, name):
        self.name = name
        self.data = None
        self.x = None
        self.y = None

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_position(self):
        return self.x, self.y

    def jsonify(self):
        posx, posy = self.get_position()
        jsonobj = {"name": self.name, "data": self.data, "x": posx, "y": posy}
        return json.dumps(jsonobj)
