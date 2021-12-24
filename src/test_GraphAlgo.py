from unittest import TestCase
from GraphAlgo import *
import os
graph = GraphAlgo()
file = r"/Users/david/Desktop/Ex3-new/src/A0.json"

class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        e = graph.graph
        self.assertTrue(e,graph.get_graph())


    def test_load_from_json(self):
        e = graph.load_from_json(file)
        actual = graph.get_graph()
        self.assertTrue(e,actual)

    def test_save_to_json(self):
        e = graph.load_from_json(file)
        save = graph.save_to_json("testUnit.json")
        self.assertTrue(e,save)

    def test_shortest_path(self):
        graph.load_from_json(file)
        short = graph.shortest_path(0,2)
        print(short)


    def test_tsp(self):
        graph.load_from_json(file)
        test = graph.TSP([3,5,7])
        print(test)

    def test_center_point(self):
        graph.load_from_json(file)
        center = graph.centerPoint()
        self.assertTrue(center,6.806805834715163)


    def test_plot_graph(self):
        self.fail()
