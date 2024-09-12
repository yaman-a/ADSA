from collections import deque as queue

# Node class (struct)
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

# Function to get height of tree
def height(node):
    if not node:
        return 0
    return node.height

# Level order traversal, mainly for testing purposes
def levelOrder(root):
    if root == None:
        return
    
    q = queue()

    q.append(root)
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

def main():
    root = Node(5)
    root.left = Node(3)
    root.right = Node(7)

    levelOrder(root)
    

# Main
if __name__ == '__main__':
    main()

