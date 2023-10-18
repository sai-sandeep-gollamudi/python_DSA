
class rbst:
    def _contains(self,c_node,value):
        if(c_node==None):
            return False
        if(c_node==value):
            return True
        elif(c_node>value):
            return self._contains(c_node.left,value)
        else:
            return self._contains(c_node.right,value)

    def contains(self,value):
        return self._contains(self.root,value)

    def _insert(self,c_node,value):
        if(c_node==None):
            return Node(value)
        elif(value<c.node):
            c_node.left = self._insert(c.node.left,value)
        else:
            c_node.right=self._insert(c.node.right,value)
        return c_node

    def insert(self,value):
        if(self.root==None):
            self.root=Node(value)
        self._insert(self.root,value)
