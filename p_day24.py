class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root=new_node
            return True
        temp = self.root
        while(True):
            if(temp.value==new_node.value):
                return False
            if(new_node.value < temp.value):
                if(temp.left is None):
                    temp.left=new_node
                    return True
                temp=temp.left
            else:
                if(temp.right is None):
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        if(self.root is None):
            return False
        temp = self.root
        while(temp):
            if(value < temp.value):
                temp = temp.left
            elif(value > temp.value):
                temp = temp.right
            else:
                return True
        return False

    def BFS(self):
        if(self.root is None):
            return False
        result = []
        q = []
        q.append(self.root)
        while(len(q) > 0):
            temp = q.pop(0)
            result.append(temp.value)
            if(temp.left is not None):
                q.append(temp.left)
            if(temp.right is not None):
                q.append(temp.right)
        return result

    def preorder(self):
        result = []
        def traverse(temp):
            result.append(temp.value)
            if(temp.left is not None):
                traverse(temp.left)
            if(temp.right is not None):
                traverse(temp.right)
        traverse(self.root)
        return result

    def postorder(self):
        result = []
        def traverse(temp):
            if(temp.left is not None):
                traverse(temp.left)
            if(temp.right is not None):
                traverse(temp.right)
            result.append(temp.value)
        traverse(self.root)
        return result

    def inorder(self):
        result=[]
        def traverse(temp):
            if(temp.left is not None):
                traverse(temp.left)
            result.append(temp.value)
            if(temp.right is not None):
                traverse(temp.right)
        traverse(self.root)
        return result

mybst = BinarySearchTree()
mybst.insert(10)
mybst.insert(5)
mybst.insert(15)
mybst.insert(20)
mybst.insert(2)
mybst.insert(25)

print(f"Breadth First Search - {mybst.BFS()}")

print(f"Preorder - {mybst.preorder()}")

print(f"Postorder - {mybst.postorder()}")

print(f"Inorder - {mybst.inorder()}")
