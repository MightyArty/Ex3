import sys
from GraphAlgo import *
from matplotlib import pyplot as plt
from Edge import *

from matplotlib.patches import ConnectionPatch
from DiGraph import *
from Node import Node

fig, (ax1) = plt.subplots(figsize=(10, 10)) # set image dimensions

graph = DiGraph()
graphAgo = GraphAlgo()

graphAgo.load_from_json("/Users/david/Desktop/Ex3-new/data/A5.json") #loading json
get = graphAgo.get_graph() #get graph

graphAgo.plot_graph()

srcDest = []
nodes = get.get_all_v() # dict (int, tuple)
keys = graph.nodesMap.keys()
posList = []
outEdge = []
outID = []
for i in nodes.keys():
    outEdge.append(get.all_out_edges_of_node(i))
    outID.append(outEdge[i].keys())

for i in nodes: # looping all the positions into posList
        posList.append(nodes[i].pos)

xList = [x[0] for x in posList] # the python way to loop x's into xList
yList = [y[1] for y in posList] # same for y

id = [ids for ids in nodes]  # the python way to loop al the ids into the list

pos = []
# for i in pos:
#     pos[i].append(xList[i],yList[i])
# xyC = (x_list[2], y_list[2])
# for i in range(len(outID)):
# plt.plot(xList,yList, color='b', marker='o', markersize=5)
plt.scatter(xList, yList, color='green')  # green node dot
for i in id:
    plt.text(xList[i], yList[i], f'{id[i]}', ha='center', fontsize=12)  # add node id

con = []

# ax1.annotate('arrow', xy=(outID[0],outID[1]), xytext=(outID[0],outID[1]),
#             arrowprops={'arrowstyle': '<->'}, va='center')
# for i in range(len(xList)):



#
# xyA = (xList[0], yList[0])
# xyB = (xList[1], yList[1])
# coordsA = "data"
# coordsB = "data"
# con = ConnectionPatch(xyA, xyB, coordsA, coordsB, arrowstyle="<|-|>", shrinkA=3,shrinkB=3, )  # make arrows between nodes
# # con1 = ConnectionPatch(xyB, xyC, coordsA, coordsB, arrowstyle="<|-|>", shrinkA=3,shrinkB=3, )  # make arrows between node
#
# ax1.add_artist(con)
# # ax1.add_artist(con1)
# plt.tight_layout()
# plt.show()

if __name__ == '__main__':
    # print(outID)
    # print(nodes)
    # out = nodes["pos"].split(',')
    # pos1 = (float(out[0]), float(out[1]),float(out[2]))
    # print(pos1)

    print(nodes)

    # print(xList)
    # print(posList)
    # x = posList[0][0]
    # y = posList[0][1]
    # print(x)
    # print(y)
    # for i in range((len(outEdge))):
        # outID.append(outEdge[i].keys())
        # temp = [x for x in outID[i]]
    # print(temp)
    # print(outID)

    # for i in outID:
    #     temp.append(outID[i])

    # print(temp)


    # print(outID)
    # for i in range(outEdge):
    #     outID = outEdge.values()


    # print(outID)


