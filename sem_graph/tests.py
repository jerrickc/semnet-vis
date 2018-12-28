from django.test import TestCase
from .models import Node, Edge, EdgeType, Graph
from django.core.urlresolvers import reverse
import views
# Create your tests here.
class stringifyTests(TestCase):
    def testGraph(self):
        testGraph = Graph(graphName="testg")
        self.assertEqual(testGraph.__str__(), "testg")
        
    def testEdgeType(self):
        testEdgeType = EdgeType(typeName="testtype")
        self.assertEqual(testEdgeType.__str__(), "testtype")
        
    def testNode(self):
        testnode = Node(name="test1",data="test2",x=100.25,y=-100.25)
        self.assertEqual(testnode.__str__(), "test1=>test2")
        
    def testEdge(self):
        testnode = Node(name="test1",data="test2",x=100.25,y=-100.25)
        testnode2 = Node(name="test3",data="test4",x=100.25,y=-100.25)
        testEdge = Edge(node1=testnode,node2=testnode2)
        self.assertEqual(testEdge.__str__(), "test1=>test2 None test3=>test4")

class APITests(TestCase):
    def setUp(self):
        testGraph = Graph(graphName="testg")
        testGraph.save()
        testEdgeType = EdgeType(graph=testGraph,typeName="testtype")
        testEdgeType.save()
        testnode = Node(graph=testGraph,name="test1",data="test2",x=100.25,y=-100.25)
        testnode2 = Node(graph=testGraph,name="test3",data="test4",x=100.25,y=-100.25)
        testnode.save()
        testnode2.save()
        testEdge = Edge(graph=testGraph,node1=testnode,node2=testnode2,edgetype=testEdgeType)
        testEdge.save()
    
    def testgetNodes(self):
        response = self.client.get(reverse('getNodes'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test1")
        self.assertContains(response, "test2")
        self.assertContains(response, "100.25")
        self.assertContains(response, "-100.25")
    
    def testgetEdges(self):
        response = self.client.get(reverse('getEdges'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "edgetype")
        self.assertContains(response, "2")
        self.assertContains(response, "1")