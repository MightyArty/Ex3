from Edge import Edge
from GraphInterface import GraphInterface
from Node import *


class DiGraph(GraphInterface):

    def __init__(self):
        self.vertexSize = 0
        self.edgeSize = 0
        self.mc = 0
        self.edgesMap = dict()
        self.reversEdges = dict()
        self.nodesMap = dict()

    def v_size(self) -> int:
        return len(self.nodesMap)

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.nodesMap

    def all_in_edges_of_node(self, id1: int) -> dict:
        nodes = dict()
        temp1 = self.reversEdges[id1]
        for e in temp1.values():
            nodes[e.src] = e.weight
        return nodes

    def all_out_edges_of_node(self, id1: int) -> dict:
        nodes = dict()
        nodeEdges = self.edgesMap[id1]
        for e in nodeEdges.values():
            nodes[e.dest] = e.weight
        return nodes

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if self.nodesMap.__contains__(id1) and self.nodesMap.__contains__(id2):
            e = Edge(id1, id2, weight)
            destMap = self.edgesMap.get(id1)
            if destMap is None:
                destMap = dict()
                destMap[id2] = e
                self.edgesMap[id1] = destMap
                reversTemp = dict()
                reversTemp[id1] = e
                self.reversEdges[id2] = reversTemp
                self.edgeSize += 1
                self.mc += 1
                return True
            elif not destMap.__contains__(id2):
                tempHas = self.edgesMap[id1]
                tempHas[id2] = e
                self.edgesMap[id1] = tempHas
                if not self.reversEdges.__contains__(id2):
                    reverseTemp = dict()
                    reverseTemp[id1] = e
                    self.reversEdges[id2] = reverseTemp
                else:
                    reverseTemp = self.reversEdges[id2]
                    reverseTemp[id1] = e
                    self.reversEdges[id2] = reverseTemp
                self.edgeSize += 1
                self.mc += 1
                return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        node = Node(node_id, pos)
        if not self.nodesMap.__contains__(node_id):
            self.nodesMap[node_id] = node
            self.mc += 1
            self.vertexSize += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        if self.nodesMap.__contains__(node_id):
            # self.nodesMap.pop(node_id)
            self.mc += 1
            self.vertexSize -= 1
            if self.edgesMap.__contains__(node_id):
                self.edgeSize = self.edgeSize - len(self.edgesMap.get(node_id))
                self.mc += len(self.edgesMap.get(node_id))
                Dict = self.edgesMap.pop(node_id)
                for e in Dict:
                    self.reversEdges.pop(e.src)
            if self.reversEdges.__contains__(node_id):
                self.edgeSize = self.edgeSize - len((self.reversEdges.get(node_id)))
                self.mc += len((self.reversEdges.get(node_id)))
                Dict = self.reversEdges.pop(node_id)
                for e in Dict:
                    self.edgesMap.pop(e.dest)
            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        tempMap = self.edgesMap.get(node_id1)
        if tempMap is not None:
            tempMap.pop(node_id2)
            self.edgesMap[node_id1] = tempMap
            reversedTempMap = self.reversEdges.get(node_id2)
            reversedTempMap.pop(node_id1)
            self.reversEdges[node_id2] = reversedTempMap
            self.edgeSize -= 1
            self.mc += 1
            return True
        else:
            return False

    def __str__(self):
        return str({self.nodesMap.values()})

    def __repr__(self):
        return f"The graph: {self.nodesMap.values()}"
