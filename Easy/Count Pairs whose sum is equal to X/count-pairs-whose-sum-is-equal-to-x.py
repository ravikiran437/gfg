#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
    
        


# } Driver Code Ends
#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def countPair(self, head1, head2, n1, n2, x):
        l1 ,l2 = set(),set()
        while head1:
            l1.add(head1.data)
            head1 = head1.next 
        while head2:
            l2.add(head2.data)
            head2 = head2.next
        c = 0
        for i in l1:
            sub = x - i
            if sub in l2:
                c +=  1
                l2.remove(sub)
        return c
    

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    t=int(input())
    for cases in range(t):
        
        n1=int(input())
        ll1 = LinkedList() # create a new linked list 'll1'.
        nodes_ll1 = list(map(int, input().strip().split()))
        for nodes in nodes_ll1:
            ll1.append(nodes)  # add to the end of the list
        
        n2=int(input())
        ll2=LinkedList()  #create a new linked list 'll1'.
        nodes_ll2 = list(map(int, input().strip().split()))
        for nodes in nodes_ll2:
            ll2.append(nodes)  # add to the end of the list
        
        x=int(input())
        
        
        print(Solution().countPair(ll1.head,ll2.head,n1,n2,x))


# } Driver Code Ends