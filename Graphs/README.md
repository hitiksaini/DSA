## Graph Data Stucture

#### `A graph data structure is a collection of nodes that have data and are connected to other nodes.`

It is a non-linear data structure consisting of nodes and edges. The nodes are sometimes also referred to as vertices and the edges are lines or arcs that connect any two nodes in the graph. 

Mathematically, `A Graph consists of a finite set of vertices(or nodes) and set of Edges which connect a pair of nodes.`

More precisely, a graph is a data structure (V, E) that consists of
* A collection of vertices V
* A collection of edges E, represented as ordered pairs of vertices (u,v)

### Facebook's example
Facebook use graphs to store data. Let's try to understand this through an example. On facebook, <b>*everything is a node*</b>. That includes User, Photo, Album, Event, Group, Page, Comment, Story, Video, Link, 

`Note: Anything that has data is a node.`

Every relationship is an edge from one node to another. Whether you post a photo, join a group, like a page, etc., a new edge is created for that relationship

<b>All of facebook is then a collection of these nodes and edges. This is because facebook uses a graph data structure to store its data. </b>

### Graph Representation 
Graphs are commonly represented in two ways:

* <b>Adjacency Matrix : </b> An adjacency matrix is a 2D array of V x V vertices. Each row and column represent a vertex. If the value of any element a[i][j] is 1, it represents that there is an edge connecting vertex i and vertex j.

The adjacency matrix for a graph is shown below
<img width="650px" src="https://cdn.programiz.com/sites/tutorial2program/files/adjacency-matrix_1.png" />

Since it is an undirected graph, for edge (0,2), we also need to mark edge (2,0); making the adjacency matrix symmetric about the diagonal.

Edge lookup(checking if an edge exists between vertex A and vertex B) is extremely fast in adjacency matrix representation but we have to reserve space for every possible link between all vertices(V x V), so it requires more space.

* <b>Adjacency List : </b> An adjacency list represents a graph as an array of linked lists. The index of the array represents a vertex and each element in its linked list represents the other vertices that form an edge with the vertex.

The adjacency list for the graph we made in the first example is as follows:

<img src="https://cdn.programiz.com/sites/tutorial2program/files/adjacency-list.png" width="850px" />

An adjacency list is efficient in terms of storage because we only need to store the values for the edges. For a graph with millions of vertices, this can mean a lot of saved space.

### Graph Operations
The most common graph operations are:

* Check if the element is present in the graph
* Graph Traversal
* Add elements(vertex, edges) to graph
* Finding the path from one vertex to another (Shortest path algorithms like BFS, DFS etc.,)
