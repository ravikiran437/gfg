#User function Template for python3


#Function to check if any pair exists in BST whose sum is equal to given value.
def findPair(root,X):
    # code here    
    
    # code here    

    stack = [root]
    d = {}
    while stack:
        node = stack.pop()
        diff = X - node.key
        if diff in d:
            return True
        if node.key not in d:
            d[node.key] = 1
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return False
