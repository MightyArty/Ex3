import copy
import json
import random
from typing import List

from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph

    def get_graph(self) -> GraphInterface:
        return self.graph

    def copy(self):
        graph = DiGraph()
        for node in self.graph.nodesMap.values():
            graph.add_node(node.id, node.pos)
            for edge in self.graph.all_out_edges_of_node(node.id):
                weight = self.graph.edgesMap[node.id][edge]
                graph.add_edge(node.id, edge, weight)
        return graph

    """
        Loads a graph from a json file.
        @param file_name: The path to the json file
        @returns True if the loading was successful, False o.w.
    """

    def load_from_json(self, file_name: str) -> bool:
        graph = DiGraph()
        Edges: list
        Nodes: list
        try:
            with open(file_name, 'r') as f:
                r = json.load(f)
                Edges = r["Edges"]
                Nodes = r["Nodes"]

                for node in Nodes:
                    try:
                        out = node["pos"].split(',')
                        pos = (float(out[0]), float(out[1]), float(out[2]))
                    except Exception:
                        pointX = random.randint(5, 50)
                        pointY = random.randint(5, 50)
                        pos = (pointX, pointY, 0.0)

                    graph.add_node(node["id"], pos)

                for edge in Edges:
                    graph.add_edge(edge["src"], edge["dest"], edge["w"])
                self.graph = graph
                print("Successfully loaded from json format")
                return True
        except():
            print("Error in loading from json format")
            return False

    """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, False o.w.
    """

    def save_to_json(self, file_name: str) -> bool:
        output = {"Edges": [], "Nodes": []}
        for node in self.graph.nodesMap.values():
            dict1 = {"id": node.id}
            if node.pos is not None:
                dict1["pos"] = node.pos
            output["Nodes"].append(dict1)

            for edge in self.graph.all_out_edges_of_node(node.id):
                dict2 = {"src": node.id, "w": self.graph.all_out_edges_of_node(node.id)[edge], "dest": edge}
                output["Edges"].append(dict2)
        try:
            with open(file_name, "w") as f:
                f.write(json.dumps(output))
                print("Successfully saved to json format")
                return True
        except():
            print("Error in saving to json format")
            return False

    """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Notes:
            If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
            More info:
            https://en.wikipedia.org/wiki/Dijkstra's_algorithm
    """

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        vertexDirection = dict()
        if self.graph.nodesMap[id1] is None or self.graph.nodesMap[id2] is None or self.graph is None:
            vertexDirection[float('inf')] = []
            return vertexDirection
        if id1 == id2:
            vertexDirection[0] = [id1]
            return vertexDirection
        tempGraph = self.graph
        curr = tempGraph.nodesMap[id1]
        curr.weight = 0
        vertexDirection[id1] = curr
        for n in tempGraph.nodesMap.values():
            tempNode = n
            if tempNode.id != id1:
                tempGraph.nodesMap[tempNode.id].weight = float('inf')  # set the weight
                tempGraph.nodesMap[tempNode.id].info = "Not Visited"
                tempGraph.nodesMap[tempNode.id].tag = -1
        curr.info = "Not Visited"
        pq = [curr]
        while len(pq) != 0:
            if curr.id != id2:
                tempDict = self.graph.edgesMap[curr.id]
            for e in tempDict.values():
                if curr.id != e.dest:
                    sumWeight = e.weight + tempGraph.nodesMap[e.src].weight
                    if tempGraph.nodesMap[e.dest].weight > sumWeight:
                        tempGraph.nodesMap[e.dest].weight = sumWeight
                        tempGraph.nodesMap[e.dest].tag = curr.id
                        vertexDirection[e.dest] = curr
                tempNode = tempGraph.nodesMap[e.dest]
                if tempNode.info != "Visited":
                    pq.append(tempGraph.nodesMap[e.dest])
            if pq[0] is not None:
                tempGraph.nodesMap[pq[0].id].info = "Visited"
                pq.pop(0)
            if len(pq) != 0:
                curr = pq[0]
        minWeight = tempGraph.nodesMap[id2].weight
        ansArr = list()
        ansArr.append(tempGraph.nodesMap[id2].id)
        index = id2
        while index != id1:
            ansArr.append(vertexDirection[index].tag)
            index = vertexDirection[index].tag
        ansArr.reverse()
        return minWeight, ansArr

    """
        Finds the shortest path that visits all the nodes in the list
        param: node_lst: A list of nodes id's
        return: A list of the nodes id's in the path, and the overall distance
    """

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        if node_lst is None:
            print("The list should not be empty !")

        ans = []
        destination = 0
        temp = copy.deepcopy(node_lst)  # copy of the given list
        ans.append(temp[0])  # first
        temp.remove(temp[0])  # remove the first

        while len(temp) > 0:
            currentNode = 0
            currentDist = 0
            for node in temp:
                dist = 0
                arr = self.shortest_path(ans[-1], node)
                if dist < currentDist:
                    currentDist = dist
                    currentNode = arr[-1]
            destination = destination + currentDist
            ans.append(currentNode)
        return ans, destination

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

    """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
    """

    def plot_graph(self) -> None:
        pass


if __name__ == '__main__':
    g = GraphAlgo()
    file = '/Users/valhalla/PycharmProjects/Ex3/data/A1.json'
    g.load_from_json(file)
    g.save_to_json("outputTEST.json")
