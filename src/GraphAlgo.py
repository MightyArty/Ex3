import json
from queue import Queue
from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from DiGraph import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    def get_graph(self) -> GraphInterface:
        """
        :return: the directed graph on which the algorithm works on.
        """
        pass

    def __init__(self, g=DiGraph()):
        self.graph = g

    def load_from_json(self, file_name: str) -> bool:
        try:
            file = open(file_name)
            data = json.load(file)
            edges = data["Edges"]
            nodes = data["Nodes"]
            for i in edges:
                self.graph.add_edge(i["src"], i["dest"], i["w"])
            for i in nodes:
                self.graph.add_node(i["id"], i["pos"])
            print("Successfully loaded the json file")
            return True
        except:
            print("Error in loading json file")
            return False

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        ans = dict()
        if self.graph.nodesMap[id1] is None or self.graph.nodesMap[id2] is None or self.graph is None:
            ans[float('inf')] = []
            return ans
        if id1 == id2:
            ans[0] = [id1]
            return ans
        tempGraph = self.graph
        curr = tempGraph.nodesMap[id1]
        curr.weight = 0
        ans[id1] = curr
        for n in tempGraph.nodesMap.values():
            tempNode = n
            if tempNode.id != id1:
                tempGraph.nodesMap[tempNode.id].weight = float('inf')  # set the weight
                tempGraph.nodesMap[tempNode.id].info = "Not Visited"
                tempGraph.nodesMap[tempNode.id].tag = -1
        curr.info = "Not Visited"
        pq = [curr]
        while len(pq) != 0:
            edges = tempGraph.all_out_edges_of_node(curr.id)
            for e in edges.values():
                if curr.id != e:
                    sumWeight = e.weight + tempGraph.nodesMap[e.dest].weight
                    if tempGraph.nodesMap[e.dest].weight > sumWeight:
                        tempGraph.nodesMap[e.dest].weight = sumWeight
                        tempGraph.nodesMap[e.dest].tag = curr.id
                        ans[e.dest] = curr.id
                tempNode = tempGraph.nodesMap[e]
                if tempNode.info != "Visited":
                    pq.append(tempGraph.nodesMap[e.dest])
            if pq[0] is not None:
                tempGraph.nodesMap[pq[0]].info = "Visited"
                pq.pop(0)
                curr = pq[0]
        minWeight = tempGraph.nodesMap[id2].weight
        return minWeight

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        pass

    def centerPoint(self) -> (int, float):
        size = len(self.graph.nodesMap)
        matrix = []
        for i in range(size):
            a = []
            for j in range(size):
                if i == j:
                    a.append(0)
                else:
                    a.append(float('inf'))
            matrix.append(a)
        for i in range(size):
            keys = self.graph.all_out_edges_of_node(i).keys()
            for j in range(size):
                if keys.__contains__(j):
                    Edge = self.graph.edgesMap[i]
                    matrix[i][j] = Edge[j].weight

        for k in range(size):
            for i in range(size):
                for j in range(size):
                    if matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
        ans = dict()
        min = float('inf')
        id = -1
        minMax = -1
        for i in range(size):
            max = -1
            for j in range(size):
                if matrix[i][j] > max:
                    max = matrix[i][j]
            if max == float('inf'):
                return float('inf')
            elif min > max:
                min = max
        if minMax < min:
            id = i
            tempMax = min
        ans[id] = tempMax
        return ans

    def plot_graph(self) -> None:
        pass
