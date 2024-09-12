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

    return b

def leftRotate(x):
    y = x.right
    z = y.left

    y.left = x
    x.right = z

    x.height = 1 + max(height(x.left), height(x.right))
    y.height = 1 + max(height(y.left), height(y.right))

    return y

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

    if balance > 1 and val < node.left.val:
        return rightRotate(node)
    if balance < -1 and val > node.right.val:
        return leftRotate(node)


    if balance > 1 and val > node.left.val:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    
    if balance < -1 and val < node.right.val:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    
    return node

def maxValueNode(node):
    current = node
    while current.right is not None:
        current = current.right

    return current

def delete(node, val):
    if not node:
        return node
    
    if val < node.val:
        node.left = delete(node.left, val)
    elif val > node.val:
        node.right = delete(node.right, val)
    else:
        if not node.left or not node.right:
            temp = node.left if node.left else node.right

            if not temp:
                node = None
            else:
                node = temp

        else:
            temp = maxValueNode(node.left)
            node.val = temp.val
            node.left = delete(node.left, temp.val)

    if not node:
        return node
    
    node.height = 1 + max(height(node.left), height(node.right))

    balance = getBalance(node)

    if balance > 1 and getBalance(node.left) >= 0:
        return rightRotate(node)
    if balance > 1 and getBalance(node.left) < 0:
        node.left = leftRotate(node.left)
        return rightRotate(node)
    
    if balance < -1 and getBalance(node.right) <= 0:
        return leftRotate(node)
    
    if balance < -1 and getBalance(node.right) > 0:
        node.right = rightRotate(node.right)
        return leftRotate(node)
    

    return node


# Level order traversal, mainly for testing purposes
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

# actual main code
def main():
    root = None

    vals = [10,20,30,40,50,25]

    for i in vals:
        root = insert(root, i)

    print("Level order:")
    levelOrder(root)
    print("\n")

    deletions = [20, 30]
    for j in deletions:
        root = delete(root, j)

    print("Level order after deletions:")
    levelOrder(root)
    print("\n")
    

# Main
if __name__ == '__main__':
    main()

