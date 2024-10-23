#########################################################
# CODE INSTRUCTIONS:                                    #
# 1) The method findInOrderSuccessor you're asked      #
#    to implement is located at line 30.                #
# 2) Use the helper code below to implement it.         #
# 3) In a nutshell, the helper code allows you to       #
#    to build a Binary Search Tree.                     #
# 4) Jump to line 88 to see an example for how the      #
#    helper code is used to test findInOrderSuccessor.  #
#########################################################
"""
My notes:
1. If the node has a right subtree, the successor is the leftmost node of that subtree
2. If the node doesn't have a right subtree, the successor is found by traversing the parents
   in an upward-left direction as far as possible, then returning the parent (which is in the upward-right direction)
3. If the node doesn't have a parent, or no such parent is found, there is no successor

Algorithm:
1. Check for a right subtree
    a. If there is, find the leftmode node and return it
2. If there is no right subtree
    a. Traverse all the parents until the node is a left child of its parent, then return that parent
3. If there is no parent either at first, or after traversing parents, return None

TC: O(N). In the worst case, the whole BST is traversed once.
SC: O(1). Only a pointer is used.
"""
from typing import Optional

# A node 
class Node:
    # Constructor to create a new node
    def __init__(self, key: int):
        self.key: int = key 
        self.left: Optional['Node'] = None
        self.right: Optional['Node'] = None
        self.parent: Optional['Node'] = None

# A binary search tree 
class BinarySearchTree:
    
    # Constructor to create a new BST
    def __init__(self):
        self.root: Optional[Node] = None 

    # MY CODE:
    def find_in_order_successor(self, inputNode: Node) -> Optional[Node]:
        # 1
        if inputNode.right:
            temp = inputNode.right
            while temp.left:
                temp = temp.left
            return temp

        # 2
        if inputNode.parent:
            temp = inputNode
            while temp.parent and temp == temp.parent.right:
                temp = temp.parent
            return temp.parent

        # 3
        return None

    # Given a binary search tree and a number, inserts a
    # new node with the given number in the correct place
    # in the tree. Returns the new root pointer which the
    # caller should then use(the standard trick to avoid 
    # using reference parameters)
    def insert(self, key: int) -> None:
    
        # 1) If tree is empty, create the root
        if (self.root is None):
            self.root = Node(key)
            return
        
        # 2) Otherwise, create a node with the key
        #    and traverse down the tree to find where to
        #    to insert the new node
        currentNode = self.root
        newNode = Node(key)
        while(currentNode is not None):
      
            if(key < currentNode.key):
                if(currentNode.left is None):
                    currentNode.left = newNode;
                    newNode.parent = currentNode;
                    break
                else:
                    currentNode = currentNode.left;
            else:
                if(currentNode.right is None):
                    currentNode.right = newNode;
                    newNode.parent = currentNode;
                    break
                else:
                    currentNode = currentNode.right;

    # Return a reference to a node in the BST by its key.
    # Use this method when you need a node to test your
    # findInOrderSuccessor function on
    def getNodeByKey(self, key: int) -> Optional[Node]:
    
        currentNode = self.root
        while(currentNode is not None):
            if(key == currentNode.key):
                return currentNode
            
            if(key < currentNode.key):
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right
            
        return None
        
######################################### 
# Driver program to test above function #
#########################################

# Create a Binary Search Tree
bst = BinarySearchTree()
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)  
bst.insert(14)    

# Get a reference to the node whose key is 9
node: Optional[Node] = bst.getNodeByKey(9)

# Find the in order successor of test
succ: Optional[Node] = bst.find_in_order_successor(node)

# Print the key of the successor node
if succ is not None:
    print(f"\nInorder Successor of {node.key} is {succ.key}")
else:
    print("\nInorder Successor doesn't exist")

'''
Example: 
       8
    /    \
   5      9
  / \      \
 4   7      11
/            \
1             12
 \
  3
 / \
2  3.5
'''
