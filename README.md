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
</br>`e_size()` - return the number of edges in the graph (|E|)
 
 v_size, e_size, get_all_v, all_in_edges_of_node, all_out_edges_of_node, get_mc, add_edge, add_node, remove_node, remove_edge
  

# Part II - GraphAlgo class (implements GraphAlgoInterface):
  **In this class we have the next functions :**
  
  get_graph, load_from_json, save_to_json, shortest_path, TSP, centerPoint, plot_graph
  
  
  
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

## PYTHON test results
