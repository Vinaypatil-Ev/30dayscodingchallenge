class Node:
    def __init__(self,val):
        self.data = val
        self.left = None
        self.right = None
        
#Function to serialize a tree and return a list containing nodes of tree.
def serialize(root, A):
    #code here
    if root is None:
        A.append(-1)
        return A
    A.append(root.data)
    serialize(root.left, A)
    serialize(root.right, A)
    

#Function to deserialize a list and construct the tree.
def dfs(A, i):
    if A[i] == -1:
        return i + 1, None
    root = Node(A[i])
    i += 1
    i, root.left = dfs(A, i)
    i, root.right = dfs(A, i)
    return i, root

def deSerialize(A):
    #code here
    if not A:
        return
    _, root, = dfs(A, 0)
    return root