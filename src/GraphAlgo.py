import json
from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
    """

    def load_from_json(self, file_name: str) -> bool:
        try:
            file = open(file_name)
            data = json.load(file)
            edges = data["Edges"]
            nodes = data["Nodes"]
            for i in edges:
                self.graph.add_edge(i["src"], i["dest"], i["w"])
            for i in nodes:
                self.graph.add_node(i["id"],i["pos"])
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
        ans = {"Edges": [], "Nodes": []}
        try:
            with open(file_name, "w") as file:
                for node in self.graph.nodesMap.values():
                    nodesArr = {"id": node.id}
                    if node.location is None:
                        ans["Nodes"].append(nodesArr)
                    else:
                        nodesArr["pos"] = node.location_toString()
                    for edge in self.graph.all_out_edges_of_node(node.id):
                        edgesArr = {"src": node.id, "w": self.graph.all_out_edges_of_node(node.id)[edge], "dest": edge}
                        ans["Edges"].append(edgesArr)
                file.write(json.dumps(ans))
                return True
        except:
            print("Error in writing the file!")
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
