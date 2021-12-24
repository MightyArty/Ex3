from unittest import TestCase
from DiGraph import *

graph = DiGraph()
a = (1,2,0)
b = (2,4,0)
c = (6,3,0)
graph.add_node(0,a)
graph.add_node(1,b)
graph.add_node(2,c)
graph.add_edge(0,1,5) # one edge 2 -- 4

class TestDiGraph(TestCase):
    def test_v_size(self):
        e = graph.v_size()
        self.assertTrue(e,3)

    def test_e_size(self):
        e = graph.e_size()
        self.assertTrue(e,1)


    def test_get_all_v(self):
        e = graph.get_all_v()
        self.assertTrue(e,graph.nodesMap)

    def test_all_in_edges_of_node(self):
        e = graph.all_in_edges_of_node(1)
        self.assertTrue(e,1)


    def test_all_out_edges_of_node(self):
        e = graph.all_out_edges_of_node(0) # 1 edge to 5
        self.assertTrue(e,1)


    def test_get_mc(self):
        e = graph.get_mc()
        self.assertTrue(e,4)


    def test_add_edge(self):
        before = graph.e_size()
        graph.add_edge(2,6,1)
        e = graph.e_size()
        self.assertNotEqual(before,e)


    def test_add_node(self):
        before = graph.v_size() #3
        temp = (10,10,0)
        graph.add_node(4,temp)
        e = graph.v_size() # 4
        self.assertNotEqual(before, e)


    def test_remove_node(self):
        before = graph.v_size() # 3
        graph.remove_node(2)
        e = graph.v_size() #2
        self.assertNotEqual(e,before)






    def test_remove_edge(self):
        before = graph.e_size() #1
        graph.remove_edge(0,1)
        e = graph.e_size() #0
        self.assertNotEqual(e,before)

