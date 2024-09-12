from collections import deque as queue

# Node class (struct)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

def rightRotate(a):
    b = a.left
    c = b.right

    b.right = a
    a.left = c

    a.height = 1 + max(height(a.left), height(a.right))
    b.height = 1 + max(height(b.left), height(b.right))

    return a

def leftRotate(x):
    y = x.right
    z = y.left

    y.left = x
    x.right = z

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

# Function to get height of tree
def height(node):
    if not node:
        return 0
    return node.height

# Function to get the balance of node
def getBalance(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)

# Insert new value
def insert(node, val):
    if not node:
        return Node(val)
    
    if val < node.val:
        node.left = insert(node.left, val)
    elif val > node.val:
        node.right = insert(node.right, val)
    else:
        return node
    
    node.height = 1 + max(height(node.left), height(node.right))

    balance = getBalance(node)


# Level order traversal, mainly for testing purposes
def levelOrder(node):
    if node == None:
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

# actual main code
def main():
    node = Node(5)
    node.left = Node(3)
    node.right = Node(7)

    levelOrder(node)
    

# Main
if __name__ == '__main__':
    main()

