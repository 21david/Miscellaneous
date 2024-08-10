# https://www.tryexponent.com/courses/swe-practice/largest-smaller-bst-key


# Let me take some time to read the question
##########################################################
# CODE INSTRUCTIONS:                                     #
# 1) The method findLargestSmallerKey you're asked       #
#    to implement is located at line 30.                 #
# 2) Use the helper code below to implement it.          #
# 3) In a nutshell, the helper code allows you to        #
#    to build a Binary Search Tree.                      #
# 4) Jump to line 70 to see an example for how the       #
#    helper code is used to test findLargestSmallerKey.  #
##########################################################

from typing import Optional
import math

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

    def find_largest_smaller_key(self, num: int) -> Optional[int]:
        '''
        I'll write my thoughts here.
        I think there are 2 cases to start with: the number is in the tree somewhere, or it's not.
        The prompt doesn't have any constraints on num, so I assume either one can happen.
        A brute force solution would be to traverse the tree with in-order DFS and create an array where all the numbers
        are sorted, then search for num. If it's in the list, return the number to the left. If it's not, return the number
        to the left of where it would be. A binary search would make the search O(logN). The DFS would be O(N).
        I think it can be solved without making an array. If we traverse the tree using the BST rules (go left if num is lesser,
        go right if num is greater), then we should get somewhere close to the answer. For the example input, we would land on 14,
        which is the answer.
        If num was 10, we would land on 11. So it seems we land on either the successor (next largest value) or predecessor (next
        smallest value). I think if we store a max, and we keep track of the maximum value that is less than num, it may find the
        predecessor.  If the num is in the tree and we find it, I think we can solve this 2 ways:
            1) Re run the algorithm with num-1. If it finds that, return that. If it doesn't, return the predecessor of num-1 which
               is the predecessor of num
            2) Write an algorithm which finds the predecessor of a node which I believe is possible.
        This would be an O(N) algorithm since it would traverse the entire tree at most once. If the tree is skewed, it could have
        N levels, so that's why the worst case is O(N). If it was balanced, the TC would be O(logN) because it would go through
        one node per level. The space complexity would be O(1) since it doesn't create any large data structures.
        '''
        if not self.root:
            return -1
        root = self.root
        def helper(root, num, rerun):
            # Traverse the tree
            pointer = root
            prev_node = None # This will be at the last node we visited
            max_predecessor = -math.inf
            while pointer:
                # Binary search for num
                prev_node = pointer
                if num < pointer.key:
                    pointer = pointer.left
                elif num > pointer.key:
                    max_predecessor = max(max_predecessor, pointer.key)
                    pointer = pointer.right
                else:
                    # If we found the num
                    if rerun:
                        return pointer.key
                    else:
                        return helper(root, num - 1, True)
                    
            if max_predecessor != -math.inf:
                return max_predecessor
            else:
                return -1

        return helper(self.root, num, False)

        # The purpose of rerun is that if we find num in the tree the first time, we want to run it again with num-1
        # If we are re-running it, it should return num-1 if it finds it, or the predecessor if it doesn't
        # But if we are running it the first time, it should return the predecessor, not num.
        
        """
        
         20
        /   \
        9   25
      /  \
    5    16
        /  \ 
      15     19 
      
      Lets say num is 14. 
        It compares with 20 and goes left
        It compares with 9 and goes right, max value becomes 9
        It compares with 16 and goes left
        It compares with 15 and goes left and stops
        Predecessor is 9
        Perfect. Sounds good.

        What if num = 17.
        
        It compares with 20 and goes left
        It compares with 9 and goes right, max becomes 9
        It compares with 16 and goes right, max becomes 16
        It compares with 19 and goes left and stops
        It would return 16
        """
        
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
                    currentNode.left = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.left
            else:
                if(currentNode.right is None):
                    currentNode.right = newNode
                    newNode.parent = currentNode
                    break
                else:
                    currentNode = currentNode.right

######################################### 
# Driver program to test above function #
#########################################
bst = BinarySearchTree()

# Create the tree given in the above diagram 
bst.insert(20)
bst.insert(9)
bst.insert(25)
bst.insert(5)
bst.insert(12)
bst.insert(11)
bst.insert(14)

result: Optional[int] = bst.find_largest_smaller_key(17)
print("Largest smaller number is %d " % (result if result is not None else -1))

# test cases
print("Largest smaller number is %d " % bst.find_largest_smaller_key(10)) # 9
print("Largest smaller number is %d " % bst.find_largest_smaller_key(12)) # 11 (rerun)
print("Largest smaller number is %d " % bst.find_largest_smaller_key(14)) # 12
print("Largest smaller number is %d " % bst.find_largest_smaller_key(5)) # -1
print("Largest smaller number is %d " % bst.find_largest_smaller_key(4)) # -1
print("Largest smaller number is %d " % bst.find_largest_smaller_key(25)) # 20
print("Largest smaller number is %d " % bst.find_largest_smaller_key(26)) # 25
print("Largest smaller number is %d " % bst.find_largest_smaller_key(22)) # 20

print()

# re runs
print("Largest smaller number is %d " % bst.find_largest_smaller_key(9)) # 5
print("Largest smaller number is %d " % bst.find_largest_smaller_key(11)) # 9
print("Largest smaller number is %d " % bst.find_largest_smaller_key(20)) # 14
