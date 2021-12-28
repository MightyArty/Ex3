from unittest import TestCase
from GraphAlgo import *

algo = GraphAlgo()
file = r"C:\Users\97252\Ex3\data\A5.json"  # Enter your path here


class TestGraphAlgo(TestCase):
    def test_get_graph(self):
        e = algo.graph
        self.assertTrue(e, algo.get_graph())

    def test_load_from_json(self):
        e = algo.load_from_json(file)
        actual = algo.get_graph()
        self.assertTrue(e, actual)

    def test_save_to_json(self):
        e = algo.load_from_json(file)
        save = algo.save_to_json("testUnit.json")  # name of the output file
        self.assertTrue(e, save)

    def test_shortest_path(self):
        algo.load_from_json(file)
        short = algo.shortest_path(0, 2)
        self.assertTrue(short, [0, 1, 2])
        short2 = algo.shortest_path(0, 3)
        self.assertTrue(short2, [0, 1, 2, 3])

    def test_tsp(self):
        algo.load_from_json(file)
        test = algo.TSP([1, 3, 7])
        self.assertTrue(test[0], [1, 2, 3, 6, 7])

    def test_center_point(self):
        algo.load_from_json(file)
        print(algo.centerPoint())


    def test_plot_graph(self):
        algo.load_from_json(file)
        algo.plot_graph()
