 ![GitHub contributors](https://img.shields.io/github/contributors/MightyArty/Ex3?style=plastic) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/MightyArty/Ex3?style=plastic)
# Autores: David Yosopov, Artem Shabalin and Lior Patael

This project is a implementation to  directed weighted data structure and graph algorithms using Python Programming language. We will devide the README to 3 parts - 
DiGraph class,GraphAlgo class and comparisons between this assignment (using Python) to the previous (using Java)

# We used this algorithms in order to complete the task
- [Graph Center](https://en.wikipedia.org/wiki/Graph_center)
- [Travelling salesman problem](https://en.wikipedia.org/wiki/Travelling_salesman_problem)
- [Shortest Path Problem](https://en.wikipedia.org/wiki/Shortest_path_problem)
- [Dijkstra's algorithm](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)
- [Floyd Warshall algorithm](https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm)

# Part I - DiGraph class (implements GraphInterface):
 **In this class we have the next functions :**
</br>`v_size()` - return the number of nodes in the graph (|V|)
</br>`e_size()` - return the number of edges in the graph (|E|)
</br>`get_all_v()` - return a dictionary of graph nodes {(node_id : NodeData)}
</br>`all_in_edges_of_node()` - return a dictionary of all the nodes connected to node {(parent_id, weight)}
</br>`all_in_edges_of_node()` - return a dictionary of all the nodes connected from the node {(child_id, weight)}
</br>`get_mc()` - return graph mode count
</br>`add_edge()` - connect between two nodes with weight
</br>`add_node()` - adding node to the graph
</br>`remove_node()` - remove node from the graph and all the connections with other nodes
</br>`remove_edge()` -- removing connection between 2 nodes
 
  

# Part II - GraphAlgo class (implements GraphAlgoInterface):
  **In this class we have the next functions :**
  
 </br>`get_graph()` - return the init graph
</br>`load_from_json()` - save the graph to a json file with the given file name
</br>`save_to_json()` - load the graph from a json file by the give file name
</br>`shortest_path()` - compute the shortest path between to nodes using Dijkstra's algorithm, and return (weight, path)
</br>`TSP()` - Finds the shortest path that visits all the nodes in the list
</br>`centerPoint()` - Finds the node that has the shortest distance to it's farthest node.
</br>`plot_graph()` - plot the graph to a window using matplotlib
  
  
  
  
# Part III - Comparisons:
In this part we compare our algorithms between our Ex2 assignment algorithms that we build in java - [CLICK HERE TO SEE THE PREVIOUS ASSIGNMENT](https://github.com/MightyArty/Ex2_Graphs)
## JAVA test results 

| Algorithms    | G1  | G2  | G3 | 1000 NODES | 10000 NODES
| ------------- |:---:| ---:|:---:|:---------:|:---------:|
| isConnected   | 16 ms | 5 ms | 11 ms | 101 ms | 300 ms 
| shortestPathDist| 61 ms | 3 ms | 3 ms | 112 ms | 331 ms
| shortestPat | 125 ms | 65 ms | 65 ms | 152 ms | 497 ms
| center | 6 ms | 46 ms | 21 ms | 3 sec 58 ms  | 14 min 43 sec
| tsp | 11 ms | 6 ms | 10 ms | 158 ms | 553 ms

For full comparisons please follow the link to our Wiki - [CLICK HERE ](https://github.com/MightyArty/Ex3/wiki/Comparison-between-JAVA-results-and-Python-results)

# GUI (Graph Plot)
![A0.json](https://i.ibb.co/CV00dK2/image.png)
Here we can see our implementation of our algorithm using Matplotlib. The location of the nodes is their actual postion (X,Y) on the grid with the following IDS.
The edges correlated with `all_in_edges_of_node()` function and due to that we can see the edge arrow (One way or two way)

