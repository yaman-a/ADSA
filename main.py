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
# def levelOrder(root):


# Main
if __name__ == '__main__':
    print('yeah')

