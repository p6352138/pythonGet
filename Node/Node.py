class TreeNode :
    id = 0
    leftNode = {}
    rightNode = {}
    def toData(self) :
        return id


class Tree :
    root = None
    # 中序遍历
    def inOrder(self,node):
        if node == None : 
            return
        
        self.inOrder(node.leftNode)
        node.toData()
        self.inOrder(node.rightNode)
    
    #前序遍历
    def preOder(self,node):
        if node == None : return
        node.toData()
        self.inOrder(node.leftNode)
        self.inOrder(node.rightNode)
    
    #后序遍历
    def postOder(self,node):
        if node == None : return
        self.inOrder(node.leftNode)
        self.inOrder(node.rightNode)
        node.toData()

    #前序
    def preSearch(self,node,id):
        if node == None : return
            
        if(node.toData() == id) :
            return node

        self.inOrder(node.leftNode)
        self.inOrder(node.rightNode)

    def searchNode(self,id):
        if self.root != None :
           return self.preSearch(self.root,id)
        else :
            return None


    
        


