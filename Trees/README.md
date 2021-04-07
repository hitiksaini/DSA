## Tree Data Structure
A tree is a nonlinear hierarchical data structure that consists of `nodes` connected by `edges`.

### Why we use them?
Other data structures such as arrays, linked list, stack, and queue are linear data structures that store data sequentially. In order to perform any operation in a linear data structure, the time complexity increases with the increase in the data size. But, it is not acceptable in today's computational world. Different tree data structures allow quicker and easier access to the data as it is a non-linear data structure. Linear DS allows us to understand the data manipulations but to achieve complex solution we need more advanced DS therefore we use non-linear data structure to surpass complexity issues.

### Terminologies

* Node : A node is an entity that contains a key or value and pointers to its child nodes. The last nodes of each path are called leaf nodes or external nodes that do not contain a link/pointer to child nodes. The node having at least a child node is called an internal node.

* Edge : It is the link between any two nodes.
* Root : It is the topmost node of a tree.
* Height of a Node : The height of a node is the number of edges from the node to the deepest leaf (ie. the longest path from the node to a leaf node
* Depth of a Node : The depth of a node is the number of edges from the root to the node.
* Height of a Tree : The height of a Tree is the height of the root node or the depth of the deepest node.
* Degree of a Node : The degree of a node is the total number of branches of that node.
* Forest : A collection of disjoint trees is called a forest.You can create a forest by cutting the root of a tree.

Remember that our goal is to visit each node, so we need to visit all the nodes in the subtree, visit the root node and visit all the nodes in the right subtree as well. Depending on the order in which we do this, there can be three types of traversal.

### Tree Traversal

#### `Inorder traversal`
First, visit all the nodes in the left subtree -> Then the <b>root</b> node -> Visit all the nodes in the right subtree

#### `Preorder traversal`
Visit <b>root</b> node -> Visit all the nodes in the left subtree -> Visit all the nodes in the right subtree

#### `Postorder traversal`
Visit all the nodes in the left subtree -> Visit all the nodes in the right subtree -> Visit the <b>root</b> node

