from Edge import Edge
from GraphInterface import GraphInterface
from Node import Node
from Location import Location


class DiGraph(GraphInterface):

    """Constructor"""
    def __init__(self, vertex, edges, mc):
        self.vertexSize = vertex
        self.edgeSize = edges
        self.mc = mc
        self.edgesMap = dict()
        self.reversEdges = dict()
        self.nodesMap = dict()

    def v_size(self) -> int:
        return self.vertexSize

    def e_size(self) -> int:
        return self.edgeSize

    def get_all_v(self) -> dict:
        return self.nodesMap

    def all_in_edges_of_node(self, id1: int) -> dict:
        nodes = dict()
        for e in self.reversEdges[id1]:
            nodes[e.dest] = e.weight
        return nodes

    def all_out_edges_of_node(self, id1: int) -> dict:
        nodes = dict()
        nodeEdges = self.edgesMap[id1]
        for e in nodeEdges:
            nodes[e.dest] = e.weight

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        e = Edge(id1, id2, weight)
        if self.edgesMap.__contains__(id1):
            tempHas = self.edgesMap[id1]
            tempHas[id2] = e
            self.edgesMap[id1] = tempHas
            reverseTemp = dict()
            reverseTemp[id1] = e
            self.reversEdges[id2] = reverseTemp
            self.edgeSize += 1
            self.mc += 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        node = Node(node_id, pos)
        if self.nodesMap.__contains__(node_id):
            self.nodesMap[node_id] = node
            self.mc += 1
            self.vertexSize += 1
            return True
        else:
            return False

    def remove_node(self, node_id: int) -> bool:
        if self.nodesMap.__contains__(node_id):
            self.nodesMap.pop(node_id)
            if self.edgesMap.__contains__(node_id):
                self.edgeSize = self.edgeSize - len(self.edgesMap.get(node_id))
                Dict = self.edgesMap.pop(node_id)
                for e in Dict:
                    self.reversEdges.pop(e.src)
            if self.reversEdges.__contains__(node_id):
                self.edgeSize = self.edgeSize - len((self.reversEdges.get(node_id)))
                Dict = self.reversEdges.pop(node_id)
                for e in Dict:
                    self.edgesMap.pop(e.dest)
            self.vertexSize -= 1
            self.mc += 1

            return True
        else:
            return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        tempMap = self.edgesMap.get(node_id1)
        tempMap.pop(node_id2)
        reversedTempMap = self.reversEdges.get(node_id1)
        reversedTempMap.pop(node_id1)
        self.edgeSize -= 1
        self.mc += 1


if __name__ == '__main__':
    my = dict()  # //1->3
    temp = dict()
    edge = DiGraph(1, 3, 5)
    temp[3] = edge
    temp.pop(3)
    if temp[3]!=None:
        print(temp[3])
    # print(temp)
    # temp.pop(3)
    # print(temp)
    # print(len(temp))
    my['two'] = '2'
    my[1] = temp
    keys = my.keys()
   # print(len(keys))
