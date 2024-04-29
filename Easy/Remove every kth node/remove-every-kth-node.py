
class node:
    def __init__(self,x):
        self.data = x
        self.next = None


class Solution:
    def deleteK(self, head, n):
        #code here  
        k = []
        l = []
        while head:
            k.append(head.data)
            head = head.next 
        for  i in range(len(k)):
            if (i+1) %n!=0 :
                l.append(k[i])
        if not l:
            return None
        ll = node(l[0])
        t = ll 
        for i in l[1:]:
            nn = node(i)
            t.next = nn 
            t = nn
        return ll


#{ 
 # Driver Code Starts
class node:

    def __init__(self, x):
        self.data = x
        self.next = None


def createLinkedList(arr):
    head = node(arr[0])
    curr = head
    for i in range(1, len(arr)):
        new_node = node(arr[i])
        curr.next = new_node
        curr = curr.next

    return head


def printlist(ptr):
    while ptr != None:
        print(ptr.data, end=" ")
        ptr = ptr.next
    print()


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())

        obj = Solution()
        head = createLinkedList(arr)
        new_head = obj.deleteK(head, k)
        printlist(new_head)

# } Driver Code Ends