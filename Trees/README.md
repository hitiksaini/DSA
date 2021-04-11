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

### Types of Trees

#### `Binary Tree`
A binary tree is a tree data structure in which each parent node can have at most two children.A node of a binary tree is represented by a structure containing a data part and two pointers to other structures of the same type.

        struct node
        {
         int data;
         struct node *left;
         struct node *right;
        };

#### `Binary Search Tree`
Binary Search Tree (BST) is a binary tree extension with several optional restrictions. The left child value of a node should in BST be less than or equal to the parent value, and the right child value should always be greater than or equal to the parent’s value. It is called a search tree because it can be used to search for the presence of a number in **`O(log(n))`** time.
![bst](https://cdn.programiz.com/sites/tutorial2program/files/bst-vs-not-bst.png)

This Binary Search Tree property makes it ideal for search operations since we can accurately determine at each node whether the value is in the left or right sub-tree. This is why the Search Tree is named.
`The space complexity for all the operations is O(n).`

Binary Search Tree Applications
* In multilevel indexing in the database
* For dynamic sorting
* For managing virtual memory areas in Unix kernel

#### `AVL Tree`
AVL tree is a self-balancing binary search tree in which each node maintains extra information called a balance factor whose value is either -1, 0 or +1.

Balance factor of a node in an AVL tree is the difference between the height of the left subtree and that of the right subtree of that node.

            Balance Factor = (Height of Left Subtree - Height of Right Subtree) or (Height of Right Subtree - Height of Left Subtree)

The self balancing property of an avl tree is maintained by the balance factor. The value of balance factor should always be -1, 0 or +1.

![avl](https://cdn.programiz.com/sites/tutorial2program/files/avl-tree-final-tree-1_0_2.png)
