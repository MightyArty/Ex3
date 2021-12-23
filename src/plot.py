import sys
from GraphAlgo import *
from matplotlib import pyplot as plt
from matplotlib.patches import ConnectionPatch
from DiGraph import *
from Node import Node
fig, (ax1) = plt.subplots(figsize=(5, 5))
graph = DiGraph()
# load = GraphAlgo.load_from_json("A0.json") #load file from json
t = (41, 82, 0)  # loc(x,y,z)
b = (44, 50, 0)  # loc(x,y,z)
c = (97, 55, 0)  # loc(x,y,z)
graph.add_node(1, t)  # add node (id,tuple)
graph.add_node(2, b)
graph.add_node(3, c)
locations = []
nodes = graph.get_all_v().values()
id = []
keys = graph.nodesMap.keys()

# set the id & loc into keys
for i in keys:
    id.append(graph.nodesMap.get(i).id)
    locations.append(graph.nodesMap.get(i).location)

x_list = [loc[0] for loc in locations]  # store x values
y_list = [loc[1] for loc in locations]  # store y values
z_list = [loc[2] for loc in locations]  # store z values

xyA = (x_list[0], y_list[0])
xyB = (x_list[1], y_list[1])
xyC = (x_list[2], y_list[2])

plt.scatter(x_list, y_list, color='green')  # green node dot
for i in range(3):
    plt.text(x_list[i], y_list[i], f'{id[i]}', ha='center', fontsize=12) # add node id

for i in keys:
    childes = graph.all_out_edges_of_node(id[i]).values(i)

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
    print(childes)
