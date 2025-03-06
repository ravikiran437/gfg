# your task is to complete this function
# function should return new head pointer

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

def deleteNode(head, x):
    # Code here
    if not head:  # If list is empty
        return None

    # If we need to delete the first node
    if x == 1:
        return head.next  # Move head to the next node

    cur = head
    count = 1  # 1-based index

    while cur and cur.next:
        if count == x - 1:  # Stop at the (x-1)th node
            cur.next = cur.next.next  # Skip the xth node
            break
        cur = cur.next
        count += 1

    return head


#{ 
 # Driver Code Starts
# Node Class
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:

    def __init__(self):
        self.head = None
        self.last = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.last = self.head
        else:
            self.last.next = new_node
            self.last = new_node


def print_list(head):
    temp = head
    while temp:
        print(temp.data, end=" ")
        temp = temp.next
    print('')


# Driver Program
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        list1 = LinkedList()
        values = list(map(int, input().strip().split()))
        for value in values:
            list1.insert(value)
        k = int(input())
        new_head = deleteNode(list1.head, k)
        print_list(new_head)
        print("~")
# } Driver Code Ends