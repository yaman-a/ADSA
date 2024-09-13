from collections import deque as queue
import sys
# Node class (struct)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

# Perform right rotation
def rightRotate(a):
    b = a.left
    c = b.right

    # Rotation
    b.right = a
    a.left = c

    # Adjust height
    a.height = 1 + max(height(a.left), height(a.right))
    b.height = 1 + max(height(b.left), height(b.right))

    # Return new node
    return b

# Perform left rotation
def leftRotate(x):
    y = x.right
    z = y.left

    # Rotation
    y.left = x
    x.right = z

    # Adjust height
    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    # Return new node
    return y

# Get height of tree
def height(node):
    if not node:
        return 0
    return node.height

# Get the balance factor of node
def getBalance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

# Insert new value
def insert(node, val):
    # Base case
    if not node:
        return Node(val)
    
    # Insert into left or right subtree using recursion
    if val < node.val:
        node.left = insert(node.left, val)
    elif val > node.val:
        node.right = insert(node.right, val)
    else:
        return node
    
    # Update height
    node.height = 1 + max(height(node.left), height(node.right))

    # Check balance of tree and perform rotations if unbalanced
    balance = getBalance(node)

    # Left left case
    if balance > 1 and val < node.left.val:
        return rightRotate(node)
    # Right right case
    if balance < -1 and val > node.right.val:
        return leftRotate(node)

    # Left right case
    if balance > 1 and val > node.left.val:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    
    # Right left case
    if balance < -1 and val < node.right.val:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node

# find the node with the max value (rightmost node)
def maxValueNode(node):
    current = node
    while current.right is not None:
        current = current.right

    return current

# Delete value from tree
def delete(node, val):
    # Base case
    if not node:
        return node
    
    # Search for value using recursion
    if val < node.val:
        node.left = delete(node.left, val)
    elif val > node.val:
        node.right = delete(node.right, val)
    else:
        # Node is found
        if not node.left or not node.right:
            temp = node.left if node.left else node.right

            if not temp:
                node = None # No child case
            else:
                node = temp # One child case

        else:
            # Node has two children, get max value from left subtree
            temp = maxValueNode(node.left)
            node.val = temp.val
            node.left = delete(node.left, temp.val)

    # If the tree only has one node
    if not node:
        return node
    
    # Update height
    node.height = 1 + max(height(node.left), height(node.right))

    # Get balance and perform rotations if unbalanced
    balance = getBalance(node)

    # Left left case
    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    # Right right case
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)
    
    # Left right case
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    # Right left case
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    

    return node


# For testing purposes only: Level order traversal (BFS)
def levelOrder(node):
    if not node:
        return
    
    q = queue()

    q.append(node)
    q.append(None)

    while(len(q) > 1):
        curr = q.popleft()

        if curr == None:
            q.append(None)
            print()
        else:
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)

            print(curr.val, end=" ")

# DFS methods
# Preorder traversal (node, left, right)
def preOrder(root):
    if not root:
        return []
    
    return [root.val] + postOrder(root.left) + postOrder(root.right)

# Postorder traversal (left, right, node)
def postOrder(root):
    if not root:
        return []
    
    return postOrder(root.left) + postOrder(root.right) + [root.val]

# Inorder traversal (left, node, right)
def inorder(root):
    if not root:
        return []
    
    return inorder(root.left) + [root.val] + inorder(root.right)

# Main code, handles input and creates tree
def main():
    # Empty tree
    root = None

    # Parse input and split commands
    inputLine = input().strip().split()

    # Loop through commands except the last one
    for command in inputLine[:-1]:
        if command[0] == 'A':
            val = int(command[1])
            root = insert(root, val)
        elif command[0] == 'D':
            val = int(command[1])
            root = delete(root, val)

    # Last input, which is traversal type
    traversal = inputLine[-1]

    
    if not root:
        print("EMPTY")
    else:
        if traversal == 'PRE':
            result = preOrder(root)
        elif traversal == 'POST':
            result = postOrder(root)
        elif traversal == 'IN':
            result = inorder(root)

        print(" ".join(map(str, result)))
    

# Main
if __name__ == '__main__':
    main()

