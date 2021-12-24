import sys
from GraphAlgo import *
from matplotlib import pyplot as plt
from Edge import *

from matplotlib.patches import ConnectionPatch
from DiGraph import *
from Node import Node
fig, (ax1) = plt.subplots(figsize=(5, 5))
graph = DiGraph()
graphAgo = GraphAlgo()
load = graphAgo.load_from_json("A0.json")
get = graphAgo.get_graph()

t = (41, 82, 0)  # loc(x,y,z)
b = (44, 50, 0)  # loc(x,y,z)
c = (97, 55, 0)  # loc(x,y,z)
graph.add_node(1, t)  # add node (id,tuple)
graph.add_node(2, b)
graph.add_node(3, c)
locations = []
nodes = get.get_all_v()
id = []
keys = get.graph.nodesMap.keys()

# set the id & loc into keys
for i in keys:
    id.append(graph.nodesMap.get(i).id)
    locations.append(graph.nodesMap.get(i).pos)

x_list = [loc[0] for loc in locations]  # store x values
y_list = [loc[1] for loc in locations]  # store y values
z_list = [loc[2] for loc in locations]  # store z values

xyA = (x_list[0], y_list[0])
xyB = (x_list[1], y_list[1])
xyC = (x_list[2], y_list[2])

plt.scatter(x_list, y_list, color='green')  # green node dot
for i in range(3):
    plt.text(x_list[i], y_list[i], f'{id[i]}', ha='center', fontsize=12) # add node id

# for i in keys:
#     childes = graph.all_out_edges_of_node(id[i]).values(i)


coordsA = "data"
coordsB = "data"

plt.xlim(0, 100)  # limit X
plt.ylim(0, 100)  # limit Y

# con = ConnectionPatch(xyA, xyB, coordsA, coordsB, arrowstyle="<|-|>", shrinkA=3,shrinkB=3, )  # make arrows between nodes
# con1 = ConnectionPatch(xyB, xyC, coordsA, coordsB, arrowstyle="<|-|>", shrinkA=3,shrinkB=3, )  # make arrows between node

# ax1.add_artist(con)
# ax1.add_artist(con1)
plt.show()

if __name__ == '__main__':
    # graph.add_edge(1,2,5)
    # graph.add_edge(1, 3, 15)
    # print(graph.all_out_edges_of_node(1).keys())
    # print (childes)
    # print(childes)
    print(nodes)
    # print(get.get_all_v())

