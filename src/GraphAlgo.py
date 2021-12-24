import json
from typing import List
from GraphAlgoInterface import GraphAlgoInterface
from DiGraph import DiGraph
from DiGraph import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g=DiGraph()):
        self.graph = g

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
                self.graph.add_node(i["id"], i["pos"])
            print("Successfully loaded the json file")
            return True
        except:
            print("Error in loading json file")
            return False

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
