#from collections import deque
class Node:
    def __init__(self,val):
        self.data=val
        self.left=None
        self.right=None

def create_BST(root,val):
    if root is None:
        return Node(val)
    else:
        if root.data==val:
            return root
        elif root.data<val:     
            root.right=create_BST(root.right,val)
        else:
            root.left=create_BST(root.left,val)
        return root
def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data,end=" ")
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ")
    inorder(root.right)
def levelorder(root):
    if root is None:
        return
    result=[]
    queue=[]
    queue.append(root)
    while queue:
        result.append(queue[0].data)
        root=queue.pop(0)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return result
def search_pre(root,val):
    if root is None:
        return False
    if root.data==val:
        return True
    return search_pre(root.left,val) or search_pre(root.right,val)
def search_post(root,val):
    if root is None:
        return False
    if root.left.data==val:
        return True
    return search_pre(root.right,val) or search_pre(root,val)
def search_in(root,val):
    if root is None:
        return False
    if root.left==val:
        return True
    return search_pre(root,val) or search_pre(root.right,val)

def search_levelorder(root,val):
    if root is None:
        return False
    queue=[]
    queue.append(root)
    while queue:
        root=queue.pop(0)
        if root.data==val:
            return True
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)
    return False
def find_min(root):
    while root.left is not None:
        root=root.left
    return root
def delete_node(root,key):
    if root is None:
        return root
    if key<root.data:
        root.left=delete_node(root.left,key)
    elif key>root.data:
        root.right=delete_node(root.right,key)
    else:
        #node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is NOne:
            return root.left
        #node with two children:get the in order successor
        temp=find_min(root.right)
        root.data=temp.data
        root.right=delete_node(root.right,temp.data)
    return root
def update_root(root,old_val,new_val):
    root=delete_node(root,old_val)
    root=create_BST(root,new_val)
    return root

    
#initial array   
arr=[3,5,6,7,8,4,12,45]
#create_BST
root=Node(arr[0])
for i in range(1,len(arr)):
    root=create_BST(root,arr[i])
    
#bst=create_BST(root,val)
print("Preorder:",end="")
preorder(root)
print()
print("postorder:",end="")
postorder(root)
print()
print("inorder:",end="")
inorder(root)
print()
print("levelorder:",end="")
print(levelorder(root))
print()
root=delete_node(root,6)
print("Inorder traversal after deleting 6:",end="")
inorder(root)
print()
#update a node
root=update_root(root,3,5)
print("Inorder Traversal after updating 3 to 5:",end="")
inorder(root)
print()
print(search_pre(root,45))
print(search_post(root,45))
print(search_in(root,45))
print(search_levelorder(root,8))
#print(find_min(root))


                      
                      
