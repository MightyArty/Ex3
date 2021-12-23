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
                self.graph.add_node(i["id"])
            print("Successfully loaded the json file")
            return True
        except():
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
        except():
            print("Error in writing the file!")
            return False
        finally:
            file.close()

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

        ans = List
        getNodes = List

        # getting all the nodes from the given list
        for node in node_lst:
            getNodes.append(node.id)

        # if there are only one node in the given list
        if len(getNodes) == 1:
            ans.append(node_lst[0])
            return ans

        first = getNodes[0]  # first node in the list
        second = getNodes[1]  # second node in the list

        while getNodes is not None:
            if (ans is not None) and (ans.index(len(ans) - 1).id == first):
                ans.remove(len(ans) - 1)

                arr = self.shortest_path(first, second)
                temp = List

                for n in arr:
                    temp.append(arr)
                getNodes.remove(temp)
                ans.append(arr)

                if getNodes is not None:
                    first = second
                    second = getNodes.index(0)

        return ans

    def centerPoint(self) -> (int, float):
        pass

    """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
    """

    def plot_graph(self) -> None:
        pass
