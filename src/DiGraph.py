from GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self, vertex, edges, mc):
        self.vertex = vertex
        self.edges = edges
        self.mc = mc
        self.edgesMap = {}
        self.nodesMap = {}

    # def __int__(self, src, dest, weight):
    #     self.src = src
    #     self.dest = dest
    #     self.weight = weight
    #
    # def __int__(self, node_id, pos: tuple):
    #     self.node_id = node_id
    #     self.pos = pos

    def v_size(self) -> int:
        return self.vertex

    def e_size(self) -> int:
        return self.edges

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        edge = self.edge(id1, id2, weight)
        self.edgesMap['src'] = {}
        self.edges += 1

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        Node = node(node_id, pos)

    def remove_node(self, node_id: int) -> bool:
        pass

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        pass

    def all_in_edges_of_node(self, id1: int) -> dict:
        pass

    def all_out_edges_of_node(self, id1: int) -> dict:
        pass

    def get_all_v(self) -> dict:
        pass


if __name__ == '__main__':
    my = dict() #//1->3
    temp = dict()
    edge = DiGraph(1,3,5)
    temp[3] = edge
    #my['two'] = '2'
    my[1] = temp
    print(my)
