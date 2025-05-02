# Portfolio Assessment Task 4 - Knowledge Questions

## Step 1 - Knowledge Question (20-50 words)
In your own words, describe what a Binary Search Tree (BST) is.

In addition, describe two important properties of a BST: depth and height. How are they different?

> A Binary Search Tree (BST) is a type of graph data structure that consists of nodes, with each node consisting of
> a value. Each node has at most two children, with a left and right child. As a minimum, a valid BST would consist of
> 1 root node with two children as described previously. The left child (or subtree) is always less than the root node, whereas
> the right node is always more than the root node.
> 
> The height of a BST is described as the maximum number of edges from a particular node to a leaf node in one of its subtrees.
> The depth of a BST is described as the number of edges from the root node to a particular node.

## Step 2 - Knowledge Question (50-80 words)
In your own words, describe how an algorithm to find an item in a Binary Search Tree works.

> To find an item in a BST, the algorithm would look like the following:
> 1. Start the search at the root node and compare the item against the value in the root node.
> 2. If they are the same, end the search.
> 3. Else, if the item is less than the value of the root node, move down to the left child of the root node and compare the values. The left child will now be set as the root node.
> 4. Else, if the item is more than the value of the root node, move down to the right child of the root node and compare the values. The right child will now be set as the root node.
> 5. Repeat steps 1 - 5 until the item is found.

## Step 3 - Knowledge Question (20-60 words)
In your own words, describe what a balanced BST is.

> A balanced BST means that the difference between in heights between the left and right subtrees is at most 1 for every node in the tree.

## Step 8 - Knowledge Question
With the newly balanced BST, how many steps does it take <span style="color: red">*at* *most*</span> to find an existing item in the search tree?

> Answer here...