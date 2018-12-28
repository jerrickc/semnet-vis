from __future__ import unicode_literals
import json
from django.db import models

# Create your models here.
class Graph(models.Model):
    graphName = models.CharField(max_length=200)
    def __str__(self):
        return self.graphName

class EdgeType(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    typeName = models.CharField(max_length=200)
    
    def jsonify(self):
        return json.dumps({"id": self.id, "typeName": self.typeName})
        
    def __str__(self):
        return self.typeName

class Node(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    data = models.CharField(max_length=200)
    x = models.FloatField()
    y = models.FloatField()
    
    def get_position(self):
        return self.x, self.y
        
    def jsonify(self):
        posx, posy = self.get_position()
        jsonobj = {"id": self.id, "name": self.name, "data": self.data, "x": posx, "y": posy}
        return json.dumps(jsonobj)
        
    def __str__(self):
        return self.name + "=>" + self.data

class Edge(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    node1 = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='outedges')
    node2 = models.ForeignKey(Node, on_delete=models.CASCADE, related_name='inedges')
    edgetype = models.ForeignKey(EdgeType, on_delete=models.CASCADE, null=True)
    
    def jsonify(self):
        jsonobj = {"id": self.id, "edgetype": self.edgetype.id, "from": self.node1.id, "to": self.node2.id}
        return json.dumps(jsonobj)
        
    def __str__(self):
        return self.node1.__str__()+" "+self.edgetype.__str__()+" "+self.node2.__str__()