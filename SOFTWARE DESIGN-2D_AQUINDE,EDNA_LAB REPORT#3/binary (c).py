class newNode():

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Function to get the count of
# full Nodes in a binary tree
def getfullCount(root):
    if (root == None):
        return 0

    res = 0
    if (root.left and root.right):
        res += 1

    res += (getfullCount(root.left) +
            getfullCount(root.right))
    return res


# Driver code
if __name__ == '__main__':
    """ 2
    / \
    7 5
    \ \
    6 9
    / \ /
    1 11 4
    Let us create Binary Tree as shown
    """

    root = newNode(2)
    root.left = newNode(7)
    root.right = newNode(5)
    root.left.right = newNode(6)
    root.left.right.left = newNode(1)
    root.left.right.right = newNode(11)
    root.right.right = newNode(9)
    root.right.right.left = newNode(4)

    print(getfullCount(root))