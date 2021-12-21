import json
from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from src import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph=DiGraph):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

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

    """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
    """
    def save_to_json(self, file_name: str) -> bool:
        if self.graph is None:
            return False

        ans = {"Edges": [], "Nodes": []}
        for line in self.graph.nodesMap.values():
            nodesArr = {"id": line.id}
            if line.location is None:
                ans["Nodes"].append(nodesArr)
            else:
                nodesArr["pos"] = line.location
            for edge in self.graph.all_out_edges_of_node(line.id):
                edgesArr = {"src": line.id, "w": self.graph.all_out_edges_of_node(line.id)[edge], "dest": edge}
                ans["Edges"].append(edgesArr)

        try:
            with open(file_name, "w") as file:
                file.write(json.dump(ans))
                return True
        except:
            print("Couldn't write to file")
            return False
        finally:
            file.close()

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        pass

    def plot_graph(self) -> None:
        pass
