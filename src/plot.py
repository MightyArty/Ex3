import sys
from GraphAlgo import *
from matplotlib import pyplot as plt
from Edge import *

from matplotlib.patches import ConnectionPatch
from DiGraph import *
from Node import Node

fig, (ax1) = plt.subplots(figsize=(7, 7)) # set image dimensions

graph = DiGraph()
graphAgo = GraphAlgo()

load = graphAgo.load_from_json("A0.json") #loading json
get = graphAgo.get_graph() #get graph
srcDest = []
nodes = get.get_all_v()
keys = graph.nodesMap.keys()
posList = []

for i in nodes: # looping all the positions into posList
        posList.append(nodes[i].pos)

xList = [x[0] for x in posList] # the python way to loop x's into xList
yList = [y[1] for y in posList] # same for y

id = [ids for ids in nodes]  # the python way to loop al the ids into the list

# xyA = (xList[0], yList[0])
# xyB = (x_list[1], y_list[1])
# xyC = (x_list[2], y_list[2])
# plt.plot(xList, yList, color='b', marker='o', markersize=5)
plt.scatter(xList, yList, color='green')  # green node dot
for i in id:
    plt.text(xList[i], yList[i], f'{id[i]}', ha='center', fontsize=12)  # add node id

coordsA = "data"
coordsB = "data"

# ax1.annotate('arrow', xy=(xList[0],yList[0]), xytext=(xList[0],yList[0]),
#             arrowprops={'arrowstyle': '<->'}, va='center')

# con = ConnectionPatch(xyA, xyB, coordsA, coordsB, arrowstyle="<|-|>", shrinkA=3,shrinkB=3, )  # make arrows between nodes
# con1 = ConnectionPatch(xyB, xyC, coordsA, coordsB, arrowstyle="<|-|>", shrinkA=3,shrinkB=3, )  # make arrows between node

# ax1.add_artist(con)
# ax1.add_artist(con1)
plt.tight_layout()
plt.show()

if __name__ == '__main__':
    # print(locations)
    pass
