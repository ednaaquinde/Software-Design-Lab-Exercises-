import math


# Link list node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Function to find the second last
# node of the linked list
def findSecondLastNode(head):
    temp = head

    # If the list is empty or
    # contains less than 2 nodes
    if (temp == None or temp.next == None):
        return -1

    # Traverse the linked list
    while (temp != None):

        # Check if the current node is the
        # second last node or not
        if (temp.next.next == None):
            return temp.data

        # If not then move to the next node
        temp = temp.next


# Function to push node at head
def push(head, new_data):
    new_node = Node(new_data)
    # new_node.data = new_data
    new_node.next = head
    head = new_node
    return head


# Driver code
if __name__ == '__main__':
    # Start with the empty list
    head = None

    # Use push() function to construct
    # the below list 16 . 27 . 7 . 21 . 9
    head = push(head, 16)
    head = push(head, 27)
    head = push(head, 7)
    head = push(head, 21)
    head = push(head, 9)

    print(findSecondLastNode(head))

