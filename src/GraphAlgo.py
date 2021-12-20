import json
from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph):
        self.graph = graph

    def load_from_json(self, file_name: str) -> bool:
        try:
            file = open(file_name)
            data = json.load(file)
            edges = data["Edges"]
            nodes = data["Nodes"]
            for i in edges:
                self.graph.add_edge(i["src"], i["dest"], i["w"])
            for i in nodes:
                self.graph.add_node(i["id"])
            print("Successfully loaded the json file")
            return True
        except:
            print("Error in loading json file")
            return False

    def save_to_json(self, file_name: str) -> bool:
        try:


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass
